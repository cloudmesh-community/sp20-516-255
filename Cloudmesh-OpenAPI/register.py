from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand
from cloudmesh.common.debug import VERBOSE
import sys
import connexion
from importlib import import_module
import os

class Register:
    openAPITemplate = """
openapi: 3.0.0
info:
  title: register
  description: API Endpoint Registration
  version: "1.0"
servers:
  - url: http://localhost/cloudmesh
    description: Adds a new endpoint, Validate existing end point
paths:
  /tests/register/:
     get:
      summary: Get list of valid end point for the server.
      description:
      operationId: cloudmesh.register.get_server_endpoint
        parameters:
        - in: path
          name: name
          schema:
            type: string
          description: not yet available, you can read it from docstring
        - in: query
          name: y
          schema:
            type: number
          description: not yet available, you can read it from docstring
      responses:
        '200':
          description: OK
          content:
            text/plain:
              schema:
                type: number
    put:
      summary: add new End Point on provided Server
      description:
      operationId: cloudmesh.register.add_server_endpoint
      parameters:
        - in: query
          name: x
          schema:
            type: integer
          description: not yet available, you can read it from docstring
        - in: query
          name: y
          schema:
            type: number
          description: not yet available, you can read it from docstring
      responses:
        '200':
          description: OK
          content:
            text/plain:
              schema:
                type: number
    delete:
      summary: Remove an End Point from the provided Server
      description:
      operationId: cloudmesh.register.remove_server_endpoint
      parameters:
        - in: query
          name: x
          schema:
            type: integer
          description: not yet available, you can read it from docstring
        - in: query
          name: y
          schema:
            type: number
          description: not yet available, you can read it from docstring
      responses:
        '200':
          description: OK
          content:
            text/plain:
              schema:
                type: number

"""
   
     def __init__(self,
                 endpoint="getApi",
                 cloud="AWS",
                 version="1.0.0",
                 code=0,
                 status=0
                 ):

        print("Paramater Initialization Code Here")
        
def add_server_endpoint(self, _type) :

    print("AWS CLoud API Registry Request")
      
    if cloud="AWS" :
    table = boto3.resource('dynamodb',
                           region_name='us-east-1').Table('Services')
    table.put_item(
           Item={
                'name': api_parameters["service_name"],
                'version': api_parameters["service_version"],
                'endpoint_url': api_parameters["endpoint_url"],
                'ttl': int(api_parameters["ttl"]),
                'status': api_parameters["status"],
            }
        )

  elif cloud="Azure" :
    print ("Azure API Registry Requested")

  else :
      print ("Cloud not Supported")

def get_server_endpoint(self, _type):

def remove_server_endpoint(self, _type):
