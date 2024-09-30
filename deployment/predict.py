import joblib
import numpy as np
from azureml.core.model import Model

def init():
    global model
    # Load the registered model
    model_path = Model.get_model_path('my_model')  # The model name registered in Azure ML
    model = joblib.load(model_path)

def run(data):
    # Parse input data
    input_data = np.array(data['data'])
    
    # Perform prediction
    result = model.predict(input_data)

    # Return the result in a list format
    return result.tolist()
