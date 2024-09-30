import json
import numpy as np
from deployment.predict import run  # Import the predict function from your predict.py script

# Sample input data (replace with actual test data format)
input_data = {
    'data': np.random.rand(5, 4).tolist()  # Example data (adjust dimensions and values for your model)
}

# Convert the input data to JSON format
input_json = json.dumps(input_data)

# Call the prediction function (this should match your `run()` in predict.py)
predictions = run(input_data)

# Print the prediction results
print(f"Predictions: {predictions}")
