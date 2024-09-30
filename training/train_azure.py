import json
from azure.ai.ml import MLClient
from azure.ai.ml.entities import Data, Model
from azure.identity import DefaultAzureCredential
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import os

# Load configuration from config.json
with open("deployment/config.json") as f:
    config = json.load(f)

# Connect to Azure ML Workspace using SDK v2
credential = DefaultAzureCredential()
ml_client = MLClient(
    credential=credential,
    subscription_id=config['subscription_id'],
    resource_group=config['resource_group'],
    workspace_name=config['workspace_name']
)

# Load dataset from Azure (replace with actual dataset name)
data_asset = ml_client.data.get(name='your_dataset_name', version='latest')
data = data_asset.download(target_path='data/', unpack=True)
df = pd.read_csv(os.path.join('data', 'your_dataset.csv'))

# Prepare features and target
X = df.drop(columns=['target_column'])
y = df['target_column']

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("Data loaded from Azure!")

# Create and train the model
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)
print("Model trained on Azure!")

# Make predictions and evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy on Azure: {accuracy * 100:.2f}%")

# Log accuracy (Custom logging should be handled differently in SDK v2 during training)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Save the model to a local folder
model_output = 'outputs/model.pkl'
os.makedirs('outputs', exist_ok=True)
joblib.dump(model, model_output)

# Register the model in Azure ML
ml_client.models.create_or_update(
    Model(
        name=config['model_name'],
        path=model_output,
        description="A trained RandomForest model"
    )
)
print("Model registered in Azure ML!")


