FROM python:3.10.5

# Set currnet working directory to /network-api
WORKDIR /network-api

# Copy the requirements.txt file to the container
COPY ./requirements.txt /network-api/requirements.txt

# Install poetry dependencies
RUN pip install --no-cache-dir --upgrade -r /network-api/requirements.txt

# Copy the application folder
COPY ./app /network-api/app

# start the uvidorn server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]