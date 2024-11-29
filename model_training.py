import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load sentiment data
df = pd.read_csv('data/sentiment_data.csv')

# Simulate stock movement (1: increase, 0: decrease)
# Replace this with actual stock data in a real-world scenario
df['stock_movement'] = [1 if score > 0 else 0 for score in df['sentiment']]

# Prepare features and target
X = df[['sentiment']]  # Feature
y = df['stock_movement']  # Target

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print("Model Accuracy:", accuracy_score(y_test, y_pred))
