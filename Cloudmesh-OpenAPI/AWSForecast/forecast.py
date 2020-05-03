#!/usr/bin/python
import boto3
from time import sleep
import subprocess
import pandas as pd
from AIServices import AIServices
#from Config_copy import Location
from cloudmesh.configuration.Config import Config
import configparser
import os

def get_supported_times_series_services():
    from flask import jsonify
    req_info = "Supported Time Series Forecast Services AWS : Forecast "  \
               "Azure : Auto ML"
    pinfo = {"model": req_info}
    return jsonify(pinfo)


AIServObj=AIServices('aws')


'''
Initialize the AI Service to be used and set the parameters
'''
#AIServObj=aiservices('aws')

'''
List forecast services supported
'''
#AIServObj.get_forecast_services()
