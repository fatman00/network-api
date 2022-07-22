from fastapi import FastAPI
from .endpoints import get_device_facts, get_device_interfaces

# Instantiate FastAPI Class
app = FastAPI(
    title="network-api",
    description="An API endpoint for interacting with your network",
    version=1.0,
    licence_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

# Home page
@app.get("/")
def home():
    return {"message": "Welcome to the network-api"}


# API end point to get the device facts
app.include_router(get_device_facts.router)

# API end point to get the device interfaces
app.include_router(get_device_interfaces.router)
