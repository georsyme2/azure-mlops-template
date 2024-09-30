# Azure MLOps Template

## Overview
This repository is a template for setting up an Azure Machine Learning (Azure ML) workflow with MLOps principles, enabling automated training, deployment, and monitoring.

### Key Features
- Train models locally or on Azure
- Automate model deployment via GitHub Actions
- Flexible configuration for Azure ML workspace and model parameters
- Supports SDK v2 for Azure ML

---

## Steps to Use This Template

1. **Use This Template**:
   - Click on "Use this template" on GitHub to create your own repository based on this structure.

2. **Setup Conda Environment Locally**:
   - After cloning or creating the repository, run the following to create and activate a Conda environment:
     ```bash
     conda env create -f environment.yml
     conda activate azure-mlops-env
     ```

3. **Azure ML Workspace Configuration**:
   - Make sure to create an Azure ML workspace and add the `config.json` file in the `deployment` folder with the following structure:
     ```json
      {   
      "subscription_id": "your-subscription-id",
      "resource_group": "your-resource-group",
      "workspace_name": "your-workspace-name",
      "model_name": "my_model",          
      "endpoint_name": "my-endpoint",    
      "model_path": "models/model.pkl", 
      "compute_instance": "STANDARD_DS2_V2", 
      "deployment_config": {
         "cpu_cores": 1,        
         "memory_gb": 1          
      }
      }
   ```

4. **Local Training**:
   - To train your model locally, run the following command:
     ```bash
     python training/train_local.py
     ```

5. **Azure Training**:
   - Train your model on Azure using:
     ```bash
     python training/train_azure.py
     ```

6. **Model Deployment**:
   - Deploy the model to a managed endpoint on Azure:
     ```bash
     python deployment/deploy_endpoint.py
     ```

7. **Automate with GitHub Actions**:
   - Enable GitHub Actions for automated model training and deployment by pushing your changes. Modify the `.yml` file under `.github/workflows/` for scheduling and triggering.

---

## Customization

### Training Script (`train_local.py`, `train_azure.py`)
- Modify the scripts in the `training/` folder to update your dataset, features, or model as per your project needs.

### Deployment Script (`deploy_endpoint.py`)
- Update the `deploy_endpoint.py` to modify the endpoint's compute resources and environment.

---

## Monitoring
- Follow Azure ML best practices to set up monitoring and metrics logging for your deployed models.
- Integrate Application Insights or custom logging tools if necessary.

---

## Additional Information
- The project uses **Azure ML SDK v2**.
- All necessary dependencies are listed in `environment.yml` and `requirements.txt`.

---

## FAQ
1. **How do I switch to another Azure ML workspace?**
   - Modify the `config.json` file with the new subscription ID, resource group, and workspace name.
2. **How do I update the Conda environment?**
   - Run `conda env update --file environment.yml` to update the environment.

---

Happy MLOps!
