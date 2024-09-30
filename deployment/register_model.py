import json
from azure.ai.ml import MLClient
from azure.ai.ml.entities import Model
from azure.identity import DefaultAzureCredential

# Load configuration from config.json
with open("deployment/config.json") as f:
    config = json.load(f)

# Authenticate and connect to Azure ML Workspace
credential = DefaultAzureCredential()
ml_client = MLClient(
    credential=credential,
    subscription_id=config['subscription_id'],
    resource_group=config['resource_group'],
    workspace_name=config['workspace_name']
)

# Register the model in the workspace
model = ml_client.models.create_or_update(
    Model(
        name=config['model_name'],
        path=config['model_path'],
        description="Model registration template"
    )
)

print(f"Model {config['model_name']} registered successfully!")

