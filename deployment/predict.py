import joblib
import numpy as np
from azureml.core.model import Model
from azureml.core import Run
import time

def init():
    global model
    # Load the registered model
    model_path = Model.get_model_path('my_model')  # The model name registered in Azure ML
    model = joblib.load(model_path)
    # Get the current run context for logging
    global run
    run = Run.get_context()

def run(data):
    # Parse input data
    input_data = np.array(data['data'])
    
    # Perform prediction
    result = model.predict(input_data)

    # Example of logging a metric (e.g., the actual prediction)
    run.log("prediction", result)  # Log custom metric

    # Return the result in a list format
    return result.tolist()
