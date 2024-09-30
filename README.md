# azure-mlops-template

The Stracture of the Repository can be sawn bellow:

azure-mlops-template/
│
├── .github/
│   └── workflows/
│       └── ci-cd-pipeline.yml           # GitHub Actions pipeline (optional)
│
├── deployment/
│   ├── deploy_endpoint.py               # Deploy the model to Azure ML endpoint
│   ├── predict.py                       # Prediction scoring script for inference
│   └── register_model.py                # Register model to Azure ML
│
├── environment/
│   └── env.yml                          # Conda environment specification file
│
├── notebooks/
│   └── eda.ipynb                        # Exploratory Data Analysis notebook (optional)
│
├── training/
│   ├── train_azure.py                   # Azure ML training script
│   └── train_local.py                   # Local training script
│
├── testing/
│   └── test_local.py                    # Script to test the local prediction-scoring script
│
├── .gitignore                           # Files and directories to be ignored by git
└── README.md                            # Project documentation

Adjust config file in the deployment folder based on the comments bellow.

{
    "model_name": "my_model",          // Name of the model to be registered and deployed 
    "endpoint_name": "my-endpoint",    // Azure ML endpoint name (must match the endpoint created manually)
    "model_path": "models/model.pkl",  // Path to the model file for registration
    "compute_instance": "STANDARD_DS2_V2", // Azure ML compute instance for deployment
    "deployment_config": {
        "cpu_cores": 1,         // Number of CPU cores allocated for the deployment (increase if your model is complex)
        "memory_gb": 1          // Memory (RAM) in gigabytes allocated for the deployment (adjust based on model size)
    }
}