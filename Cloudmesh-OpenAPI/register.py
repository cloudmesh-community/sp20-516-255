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
def get_server_endpoint(self, _type):

def add_server_endpoint(self, _type) :

def remove_server_endpoint(self, _type):


