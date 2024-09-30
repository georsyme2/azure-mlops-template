import joblib
import numpy as np
from azure.ai.ml import MLClient
from azure.ai.ml.entities import Model
from azure.identity import DefaultAzureCredential
import json
import time

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

    # Start timing for inference
    start_time = time.time()

    # Perform prediction
    result = model.predict(input_data)

    # End timing and log inference time
    inference_time = time.time() - start_time
    print(f"Inference time: {inference_time:.4f} seconds")

    # Log prediction (you can log this via a custom method)
    print(f"Prediction: {result}")

    # Return the result
    return result.tolist()


