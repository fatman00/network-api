from fastapi import APIRouter, HTTPException
from ..std_errors import CLIENT_NOT_REACHABLE_404, UNAUTHORIZED_401

router = APIRouter()

# Define a API endpoint for getting device facts.
@router.get(
    "/{hostname}/facts",
    summary="Retrieve device facts",
    )
def get_running_config(hostname: str):
    from napalm import get_network_driver
    from netmiko import NetmikoAuthenticationException
    from napalm.base.exceptions import ConnectionException
    import json
    import yaml

    with open('app/device_inventory.yaml', 'r') as f:
        device_inventory = yaml.safe_load(f)

    target_device = device_inventory[hostname]

    driver = get_network_driver(target_device['device_type'])
    device = driver(target_device['ip'], target_device['username'], target_device['password'])

    try:
        ssh_conn = device.open()
    except NetmikoAuthenticationException as e:
        raise HTTPException(status_code=401, detail=UNAUTHORIZED_401) from e
    except ConnectionException as e:
        raise HTTPException(status_code=404, detail=CLIENT_NOT_REACHABLE_404) from e

    else:
        return json.dumps(device.get_facts())