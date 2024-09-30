import json
from azureml.core import Workspace, Model

# Load configuration from config.json
with open("deployment/config.json") as f:
    config = json.load(f)

# Connect to Azure ML Workspace
ws = Workspace.from_config()

# Register the model in the workspace
model = Model.register(workspace=ws,
                       model_name=config['model_name'],      # Name of the model in Azure ML
                       model_path=config['model_path'],      # Path to the model file
                       description="Model registration template")  # Add a description if needed

print(f"Model {config['model_name']} registered successfully!")
