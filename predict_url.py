import joblib
import pandas as pd

from feature_extraction import extract_features


# Load trained model
model = joblib.load("phishing_model.pkl")


print("======================================")
print("     PHISHING URL DETECTION SYSTEM")
print("======================================")


# Get URL
url = input("\nEnter URL to check: ").strip()


# Extract features
features = extract_features(url)

# Convert to DataFrame
features_df = pd.DataFrame([features])


# Predict
prediction = model.predict(features_df)[0]

probabilities = model.predict_proba(features_df)[0]

phishing_probability = probabilities[0]
legitimate_probability = probabilities[1]


# Display result
print("\n======================================")
print("              RESULT")
print("======================================")


print(f"\nURL: {url}")


if prediction == 0:

    print("\n🚨 PHISHING URL")

    risk_score = phishing_probability * 100

    print(f"Risk Score: {risk_score:.2f}%")

else:

    print("\n✅ LEGITIMATE URL")

    risk_score = phishing_probability * 100

    print(f"Risk Score: {risk_score:.2f}%")


print("\nFeature Analysis:")
print("--------------------------------------")

for feature, value in features.items():
    print(f"{feature}: {value}")

print("\n======================================")