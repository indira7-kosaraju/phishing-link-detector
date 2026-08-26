import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib


# 1. Load our processed dataset
df = pd.read_csv("processed_dataset.csv")

print("Dataset loaded:")
print(df.shape)


# 2. Separate features and labels
X = df.drop("label", axis=1)
y = df["label"]


# 3. Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))


# 4. Create Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# 5. Train the model
print("\nTraining model...")

model.fit(X_train, y_train)

print("Training completed!")


# 6. Make predictions
y_pred = model.predict(X_test)


# 7. Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy)


# 8. Detailed performance report
print("\nClassification Report:")
print(classification_report(
    y_test,
    y_pred,
    target_names=["Phishing", "Legitimate"]
))


# 9. Confusion matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))


# 10. Save the trained model
joblib.dump(model, "phishing_model.pkl")

print("\nModel saved as: phishing_model.pkl")