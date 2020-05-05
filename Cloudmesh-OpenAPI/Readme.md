# Time Series Forecast using Multi Cloud AI Services

Prafull Porwal, [sp20-516-255](https://github.com/cloudmesh-community/sp20-516-255/blob/master/Cloudmesh-OpenAPI/Readme.md)

* [Contributors](https://github.com/cloudmesh-community/sp20-516-255/graphs/contributors)
* [Insights](https://github.com/cloudmesh-community/fa19-516-147/pulse)
* [Project Code](https://github.com/cloudmesh-community/sp20-516-255/tree/master/Cloudmesh-OpenAPI/AWSForecast)

## Objective

Develop Open API for time series forecasting on multiple clouds

## Introduction

Many cloud providers have introduced machine learning capabilities on their infrastructure. The project aims to provide an open API for timeseries forecasting for AWS using Forecast Services and S3 

### AWS AI Service : Forecast Open API Service Features

* Upload the data file to ./cloudmesh/upload-file location
* Upload the json schema file to ./cloudmesh/upload-file location
* Validate the data for missing and less than 0 values
* Split the dataset into Train and test by specifying split percentge.
* Provide list of Multi Cloud supported for Timeseries Forecasting
* Initialize the cloud service 
* Create a Dataset Group
* Create a Target Time Series Dataset
* Import data into Forecast from AWS Storage S3
* Create a Predictor
* Generate Forecast
* Query the Forecast

### Environment Connfiguration

* Python 3.8.2 Python or newer.
* Use a venv (see developer install)
* MongoDB installed as regular program not as service
* AWS boto3 library
* Open API package installed

Make sure that cloudmesh is properly installed on your machine and you have mongodb setup to work with cloudmesh.
More details can be found in the [Cloudmesh Manual](https://cloudmesh.github.io/cloudmesh-manual/installation/install.html)

###  OpenAPI package installation 
Make sure you use a python venv before installing. Users can install the code with

```bash
$ pip install cloudmesh-openapi
```

### Quick Forecast API reference Commands
* Start the open API server for the forecast service
```bash
cms openapi server start .//forecast.yaml
```
* Check for supported AI services
```bash
curl http://localhost:8080/cloudmesh/forecast
```
e.g. output: 
{"model":"Supported Time Series Forecast Services AWS : Forecast Azure : Auto ML"} 

* Upload file to the server from location 
```bash
curl "http://localhost:8080/cloudmesh/forecast/upload" -F "upload=@<file_path>\countries-aggregated.csv"
```
e.g. output: 
countries-aggregated.csv uploaded successfully

* Validate data file 
```bash
curl "http://localhost:8080/cloudmesh/forecast/validate_data" -F "upload=@<file_path>\countries-aggregated.csv"
```
e.g. output: 
countries-aggregated.csv validated successfully

5. Initialize aws parameters 

curl -X GET "http://localhost:8080/cloudmesh/forecast/aws" -H "accept: application/json"

## References
https://swagger.io/specification/

https://docs.aws.amazon.com/forecast/latest/dg/forecast.dg.pdf

https://github.com/aws-samples/amazon-forecast-samples


