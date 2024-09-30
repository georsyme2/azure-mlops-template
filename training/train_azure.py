from azureml.core import Workspace, Dataset, Model
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Connect to your Azure ML Workspace
ws = Workspace.from_config()

# Load dataset from Azure (replace with actual dataset name)
dataset = Dataset.get_by_name(ws, 'your_dataset_name')
data = dataset.to_pandas_dataframe()

# Prepare features and target
X = data.drop(columns=['target_column'])
y = data['target_column']

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

# Save the model to Azure output folder
model_output = 'outputs/model.pkl'
joblib.dump(model, model_output)

# Register the model in Azure ML
Model.register(workspace=ws, model_name='my_model', model_path=model_output, description='A trained RandomForest model')
print("Model registered in Azure ML!")
