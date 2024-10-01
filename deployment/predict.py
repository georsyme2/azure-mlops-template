import joblib
import numpy as np
from azure.ai.ml import MLClient
from azure.ai.ml.entities import Model
from azure.identity import DefaultAzureCredential
import json
import time
import logging  # Using Python's logging module for logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load configuration
with open("deployment/config.json") as f:
    config = json.load(f)

def init():
    global model

    # Load model from config file
    credential = DefaultAzureCredential()
    ml_client = MLClient(credential, config['subscription_id'], config['resource_group'], config['workspace_name'])

    # Get the latest version of the registered model
    model = ml_client.models.get(name=config['model_name'], version='latest')
    model_path = model.path

    # Load the model
    model = joblib.load(model_path)

def run(data):
    # Parse input data
    input_data = np.array(data['data'])

    # Perform prediction
    result = model.predict(input_data)


    # Log inference time and prediction using the built-in logging
    logger.info(f"Input Data: {input_data.tolist()}")
    logger.info(f"Prediction: {result.tolist()}")

    # Return the result
    return result.tolist()



