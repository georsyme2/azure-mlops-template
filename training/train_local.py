import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load dataset (replace with your actual dataset path)
data = pd.read_csv('path_to_your_data.csv')

# Prepare features and target
X = data.drop(columns=['target_column'])
y = data['target_column']

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("Data loaded and prepared!")

# Create and train the model
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)
print("Model trained!")

# Make predictions and evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy * 100:.2f}%")

# Save the model locally
joblib.dump(model, 'models/model.pkl')
print("Model saved locally!")
