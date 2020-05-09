class AIServices:

    def __init__(self,cloudname='None'):
        print("Time Series Service initialized")

    def init_cloud_params(self,cloudname):

        from cloudmesh.configuration.Config import Config
        self.conf = Config()["cloudmesh"]
        self.user = Config()["cloudmesh"]["profile"]["user"]
        self.spec = self.conf["cloud"][cloudname]
        self.cloudname = cloudname
        print(self.spec)
        self.default = self.spec["default"]
        self.cloudtype = self.spec["cm"]["kind"]

        if self.cloudtype=='aws':
            self.bucket_name = self.spec["cm"]["bucket_name"]
            self.region_name = self.spec["cm"]["region_name"]
            self.forecast = self.spec["cm"]["forecast_srv"]
            self.forecastquery_srv = self.spec["cm"]["forecastquery_srv"]
            self.s3_srv = self.spec["cm"]["s3_srv"]
            self.role_arn = self.spec["cm"]["iam_role_arn"]
            self.algorithmArn = self.spec["cm"]["algorithmArn"]

            import boto3
            self.session = boto3.Session(region_name=self.region_name)
            self.forecast_srv = self.session.client(service_name=self.forecast)
            self.forecastquery = self.session.client(service_name=self.forecastquery_srv)

            print("AWS Cloud was requested")
        elif self.cloudname == 'azure':
            print("Azure cloud was requested")
        else :
            print("Supported cloud services at this time : ")


    def createDatasetGroup(self):
        from cloudmesh.common.StopWatch import StopWatch
        from StatusIndicator import StatusIndicator
        import time

        def create_uuid(project_name):
            import random
            id=random.randrange(100000)
            return project_name + '_' + str(id)

        self.DATASET_FREQUENCY = "D"
        self.TIMESTAMP_FORMAT = "yyyy-MM-dd hh:mm:ss"
        proj = 'timeseries'
        self.project=create_uuid(proj)
        print(self.project)
        self.datasetName = self.project + '_ds'
        self.datasetGroupName = self.project + '_dsg'
        self.s3DataPath = "s3://" + self.bucket_name + "/" + self.key

        StopWatch.start('to_dsg')
        create_dataset_group_response = self.forecast_srv.create_dataset_group(DatasetGroupName=self.datasetGroupName,
                                                                          Domain="CUSTOM", )
        datasetGroupArn = create_dataset_group_response['DatasetGroupArn']
        self.datasetGroupArn=datasetGroupArn
        StopWatch.stop('to_dsg')
        print(StopWatch.get('to_dsg'))
        return self.datasetGroupArn

    def createDataset(self):
        import json

        with open('schema.json') as json_file:
            schema = json.load(json_file)

        response = self.forecast_srv.create_dataset(
            Domain="CUSTOM",
            DatasetType='TARGET_TIME_SERIES',
            DatasetName=self.datasetName,
            DataFrequency=self.DATASET_FREQUENCY,
            Schema=schema
        )
        datasetArn = response['DatasetArn']
        self.datasetArn=datasetArn
        self.forecast_srv.update_dataset_group(DatasetGroupArn=self.datasetGroupArn, DatasetArns=[self.datasetArn])

        return self.datasetArn

    def createDatsetImport(self):
        from StatusIndicator import StatusIndicator
        import time

        datasetImportJobName = self.project + '_IMPORT_JOB'
        ds_import_job_response = self.forecast_srv.create_dataset_import_job(DatasetImportJobName=datasetImportJobName,
                                                                    DatasetArn=self.datasetArn,
                                                                    DataSource={
                                                                        "S3Config": {
                                                                            "Path": self.s3DataPath,
                                                                            "RoleArn": self.role_arn
                                                                        }
                                                                    },
                                                                    TimestampFormat=self.TIMESTAMP_FORMAT
                                                                    )
        ds_import_job_arn = ds_import_job_response['DatasetImportJobArn']
        status_indicator = StatusIndicator()
        while True:
            status = self.forecast_srv.describe_dataset_import_job(DatasetImportJobArn=ds_import_job_arn)['Status']
            print('Checking')
            status_indicator.update(status)
            if status in ('ACTIVE', 'CREATE_FAILED'): break
            time.sleep(10)
        status_indicator.end()

        self.ds_import_job_arn=ds_import_job_arn
        return self.ds_import_job_arn

    def createPredictor(self):
        self.predictorName = self.project + '_deeparp_algo'
        forecastHorizon = 24
        create_predictor_response = self.forecast_srv.create_predictor(PredictorName=self.predictorName,
                                                              AlgorithmArn=self.algorithmArn,
                                                              ForecastHorizon=forecastHorizon,
                                                              PerformAutoML=False,
                                                              PerformHPO=False,
                                                              EvaluationParameters={"NumberOfBacktestWindows": 1,
                                                                                    "BackTestWindowOffset": 24},
                                                              InputDataConfig={"DatasetGroupArn": self.datasetGroupArn},
                                                              FeaturizationConfig={"ForecastFrequency": "D",
                                                                                   "Featurizations":
                                                                                       [
                                                                                           {
                                                                                               "AttributeName": "target_value",
                                                                                               "FeaturizationPipeline":
                                                                                                   [
                                                                                                       {
                                                                                                           "FeaturizationMethodName": "filling",
                                                                                                           "FeaturizationMethodParameters":
                                                                                                               {
                                                                                                                   "frontfill": "none",
                                                                                                                   "middlefill": "zero",
                                                                                                                   "backfill": "zero"}
                                                                                                           }
                                                                                                   ]
                                                                                               }
                                                                                       ]
                                                                                   }
                                                              )
        predictor_arn = create_predictor_response['PredictorArn']
        from StatusIndicator import StatusIndicator
        import time
        status_indicator = StatusIndicator()

        while True:
            status = self.forecast_srv.describe_predictor(PredictorArn=predictor_arn)['Status']
            status_indicator.update(status)
            if status in ('ACTIVE', 'CREATE_FAILED'): break
            time.sleep(10)

        status_indicator.end()

        self.predictor_arn=predictor_arn
        return self.predictor_arn

    def createForecast(self):

        forecastName = self.project + '_deeparp_algo_forecast'
        create_forecast_response = self.forecast_srv.create_forecast(ForecastName=forecastName,
                                                            PredictorArn=self.predictor_arn)
        forecast_arn = create_forecast_response['ForecastArn']

        from StatusIndicator import StatusIndicator

        import time

        status_indicator = StatusIndicator()

        while True:
            status = self.forecast_srv.describe_forecast(ForecastArn=forecast_arn)['Status']
            status_indicator.update(status)
            if status in ('ACTIVE', 'CREATE_FAILED'): break
            time.sleep(10)

        status_indicator.end()
        self.forecast_arn=forecast_arn
        return self.forecast_arn

    def queryForecast(self,countryname):

        forecastResponse = forecastquery_srv.query_forecast(
            ForecastArn=self.forecast_arn,
            Filters={"item_id": countryname}
        )
        self.forecastResponse=forecastResponse
        self.countryname=countryname
        return self.forecastResponse

    '''
    def compareResults(self):

        import pandas as pd
        import dateutil.parser

        #get actual test data
        actual_df = pd.read_csv("aiservices-test.csv", names=['timestamp', 'item_id', 'Confirmed', 'target_value','Deaths'])
        actual_df = actual_df[(actual_df['timestamp'] >= '2020-05-01') & (actual_df['timestamp'] < '2020-05-31')]
        actual_df = actual_df[(actual_df['item_id'] == self.countryname)]

        #get predicted data
        self.pred_df_p10 = pd.DataFrame.from_dict(self.forecastResponse['Forecast']['Predictions']['p10'])
        self.pred_df_p50 = pd.DataFrame.from_dict(self.forecastResponse['Forecast']['Predictions']['p50'])
        self.pred_df_p90 = pd.DataFrame.from_dict(self.forecastResponse['Forecast']['Predictions']['p90'])

        # create a results data frame to show compared data set
        results_df = pd.DataFrame(columns=['timestamp', 'target_value', 'source'])



        #insert actua data
        for index, row in actual_df.iterrows():
            clean_timestamp = dateutil.parser.parse(row['timestamp'])
            print('ABC')
            results_df = results_df.append({'timestamp': clean_timestamp, 'target_value': row['target_value'], 'source': 'actual'},
                                           ignore_index=True)


        #insert predicted data
        for index, row in self.pred_df_p10.iterrows():
            clean_timestamp = dateutil.parser.parse(row['timestamp'])
            results_df = results_df.append({'timestamp': clean_timestamp, 'target_value': row['target_value'], 'source': 'p10'},
                                           ignore_index=True)

        for index, row in self.pred_df_p50.iterrows():
            clean_timestamp = dateutil.parser.parse(row['timestamp'])
            results_df = results_df.append({'timestamp': clean_timestamp, 'target_value': row['target_value'], 'source': 'p50'},
                                           ignore_index=True)
        for index, row in self.pred_df_p90.iterrows():
            clean_timestamp = dateutil.parser.parse(row['timestamp'])
            results_df = results_df.append({'timestamp': clean_timestamp, 'target_value': row['target_value'], 'source': 'p90'},
                                           ignore_index=True)



        pivot_df = results_df.pivot(columns='source', values='target_value', index="timestamp")
        pivot_df.plot()

        return 'success'
    '''

    def deleteForecastStack(self):
        self.forecast_srv.delete_forecast(ForecastArn=self.forecast_arn)
        self.forecast_srv.delete_predictor(PredictorArn=self.predictor_arn)
        self.forecast_srv.delete_dataset_import_job(DatasetImportJobArn=self.ds_import_job_arn)
        self.forecast_srv.delete_dataset(DatasetArn=self.datasetArn)
        self.forecast_srv.delete_dataset_group(DatasetGroupArn=self.datasetGroupArn)
        boto3.Session().resource('s3').Bucket(self.bucket_name).Object(self.key).delete()

        return "Data Stack deleted"