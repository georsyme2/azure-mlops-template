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

