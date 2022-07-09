# Introduction

network-api is a tool that can be used to interact with your network using REST API calls.
It can be used to expose your network to developers who are more comfortable with the REST API
without having to understand the underlying protocol and complexities of interacting with the network programmatically.

# Technology Stack

The tool uses the following technology stack to provide a simple and intuitive interface for interacting with the network.

- **FastAPI** as a web framework for building APIs.
- **NAPALM** to interact with the actual network devices.

# Application Architecture

The application architecture can be illustrated in the below diagram.

The application is divided into two parts

- **Frontend** - The frontend is a FastAPI application that provides a REST API interface for interacting with the network.
- **Backend** - The backend is a Python script that uses NAPALM to interact with the network.

# Folder Structure and Files

The below screenshot illustrates the folder structure and files in the application.

The files are as follows

- **main.py** - The main file that contains the FastAPI application.
- **std_errors.py** - A file that contains the standard error messages that are usedby the application.
- **device_inventory.yaml** - A file that contains the details of the devices thatare part of the network and how to connect to them.
- **endpoints/get_device_facts.py** - A file that contains the code for the GET {hostname}/facts endpoint. It also contains the
  NAPALM code to fetch the device facts.
- **endpoints/get_device_interfaces.py** - A file that contains the code for theGET /{hostname}/interfaces endpoint. It also contains the
  NAPALM code to fetch the device interfaces.


