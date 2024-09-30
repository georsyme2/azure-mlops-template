import requests
import json

# Load configuration from config.json
with open("deployment/config.json") as f:
    config = json.load(f)

# Azure ML endpoint URL (replace with the actual endpoint URL)
endpoint_url = 'https://<your-endpoint-url>.azurewebsites.net/score'

# Sample data for testing the model (adjust based on your model input format)
input_data = {
    "data": [[0.1, 0.2, 0.3, 0.4]]  # Replace with actual input data
}

# Headers for the request
headers = {'Content-Type': 'application/json'}

# Send a POST request to the endpoint with the input data
response = requests.post(endpoint_url, data=json.dumps(input_data), headers=headers)

# Check the response from the model
if response.status_code == 200:
    print("Prediction:", response.json())
else:
    print(f"Request failed with status code: {response.status_code}")
    print(f"Error: {response.text}")