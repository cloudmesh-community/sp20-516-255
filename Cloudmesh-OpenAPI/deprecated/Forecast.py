#!/usr/bin/python
#!/usr/bin/python
import boto3
from time import sleep
import subprocess
import pandas as pd
import configparser

#Read the AWS Parameters
config = configparser.RawConfigParser()
config.read('AITimeSeries.cfg')

bucket_name=config.get('AWS Configuration','bucket_name')
region_name=config.get('AWS Configuration', 'region_name')
service_name1=config.get('AWS Configuration', 'service_name1')
service_name2=config.get('AWS Configuration', 'service_name2')

#Connect Session
session = boto3.Session(region_name=region_name)
forecast = session.client(service_name=service_name1)
forecastquery = session.client(service_name=service_name2)
s3 = session.client('s3')

df = pd.read_csv("electricityusagedata.csv", dtype = object, names=['timestamp','value','item'])

# Select January to November for one dataframe.
jan_to_oct = df[(df['timestamp'] >= '2014-01-01') & (df['timestamp'] <= '2014-10-31')]

# Select the month of December for another dataframe.
df = pd.read_csv("electricityusagedata.csv", dtype = object, names=['timestamp','value','item'])
remaining_df = df[(df['timestamp'] >= '2014-10-31') & (df['timestamp'] <= '2014-12-01')]

jan_to_oct.to_csv("item-demand-time-train.csv", header=False, index=False)
remaining_df.to_csv("item-demand-time-validation.csv", header=False, index=False)

key="item-demand-time-train.csv"
boto3.Session().resource('s3').Bucket(bucket_name).Object(key).upload_file("item-demand-time-train.csv")

DATASET_FREQUENCY = "H"
TIMESTAMP_FORMAT = "yyyy-MM-dd hh:mm:ss"

project = 'util_power_forecastdemo_pp'
datasetName= project+'_ds'
datasetGroupName= project +'_dsg'
s3DataPath = "s3://"+bucket_name+"/"+key

create_dataset_group_response = forecast.create_dataset_group(DatasetGroupName=datasetGroupName,
                                                             Domain="CUSTOM",
                                                            )
datasetGroupArn = create_dataset_group_response['DatasetGroupArn']
forecast.describe_dataset_group(DatasetGroupArn=datasetGroupArn)

schema ={
   "Attributes":[
      {
         "AttributeName":"timestamp",
         "AttributeType":"timestamp"
      },
      {
         "AttributeName":"target_value",
         "AttributeType":"float"
      },
      {
         "AttributeName":"item_id",
         "AttributeType":"string"
      }
   ]
}

response=forecast.create_dataset(
                    Domain="CUSTOM",
                    DatasetType='TARGET_TIME_SERIES',
                    DatasetName=datasetName,
                    DataFrequency=DATASET_FREQUENCY,
                    Schema = schema
)
datasetArn = response['DatasetArn']
forecast.describe_dataset(DatasetArn=datasetArn)
forecast.update_dataset_group(DatasetGroupArn=datasetGroupArn, DatasetArns=[datasetArn])
datasetImportJobName = 'EP_DSIMPORT_JOB_TARGET'
role_arn='arn:aws:iam::514439120157:role/ForecastRolePP'
ds_import_job_response=forecast.create_dataset_import_job(DatasetImportJobName=datasetImportJobName,
                                                          DatasetArn=datasetArn,
                                                          DataSource= {
                                                              "S3Config" : {
                                                                 "Path":s3DataPath,
                                                                 "RoleArn": role_arn
                                                              }
                                                          },
                                                          TimestampFormat=TIMESTAMP_FORMAT
                                                         )
ds_import_job_arn=ds_import_job_response['DatasetImportJobArn']
forecast.describe_dataset_import_job(DatasetImportJobArn=ds_import_job_arn)

print(ds_import_job_arn)

print("Data Import Completed")
