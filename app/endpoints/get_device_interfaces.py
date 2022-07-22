from fastapi import APIRouter, HTTPException
from ..std_errors import CLIENT_NOT_REACHABLE_404, UNAUTHORIZED_401

from napalm import get_network_driver
from netmiko import NetmikoAuthenticationException
from napalm.base.exceptions import ConnectionException
import yaml

# Instantiate an instance of APIRouter
router = APIRouter()

# Define a API endpoint for getting device facts.
@router.get(
    "/{hostname}/interfaces",
    summary="Retrieve device interfaces",
)
def get_running_config(hostname: str):


    # Read local Inventory file
    with open("app/device_inventory.yaml", "r") as f:
        device_inventory = yaml.safe_load(f)

    # Select target device from Inventory file
    target_device = device_inventory[hostname]

    # Define the NAPALM driver and the device connection parameters
    driver = get_network_driver(target_device["device_type"])
    device = driver(
        target_device["ip"], target_device["username"], target_device["password"]
    )

    # Attempt to connect to device and handle any exceptions.
    try:
        device.open()
    except NetmikoAuthenticationException as e:
        raise HTTPException(status_code=401, detail=UNAUTHORIZED_401) from e
    except ConnectionException as e:
        raise HTTPException(status_code=404, detail=CLIENT_NOT_REACHABLE_404) from e

    # If connection was successful, return the device interfaces.
    else:
        return device.get_interfaces()
