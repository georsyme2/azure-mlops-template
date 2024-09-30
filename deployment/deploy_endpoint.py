import json
from azureml.core import Workspace
from azureml.core.model import Model
from azureml.core.environment import Environment
from azureml.core.webservice import AciWebservice, Webservice
from azureml.core.model import InferenceConfig

# Load configuration from config.json
with open("deployment/config.json") as f:
    config = json.load(f)

# Connect to the Azure ML Workspace
ws = Workspace.from_config()

# Retrieve the model by name
model = Model(ws, name=config['model_name'])

# Set up environment from a conda specification
env = Environment.from_conda_specification(name='env-name', file_path='environment/env.yml')

# Configure inference with scoring script
inference_config = InferenceConfig(entry_script="deployment/predict.py", environment=env)

# Create deployment configuration (CPU, Memory, etc.)
aci_config = AciWebservice.deploy_configuration(cpu_cores=config['deployment_config']['cpu_cores'],
                                                memory_gb=config['deployment_config']['memory_gb'])

# Deploy the model (assumes endpoint is created manually in Azure ML Studio)
service = Webservice.deploy_from_model(workspace=ws,
                                       name=config['endpoint_name'],  # The manually created endpoint name
                                       models=[model],
                                       inference_config=inference_config,
                                       deployment_config=aci_config)

service.wait_for_deployment(show_output=True)

print(f"Service deployed at: {service.scoring_uri}")
