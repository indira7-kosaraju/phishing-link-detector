import pandas as pd
from feature_extraction import extract_features


# Load the original dataset
df = pd.read_csv("PhiUSIIL_Phishing_URL_Dataset.csv")


# Take only 10,000 URLs for the first test
df = df[["URL", "label"]].head(10000)


print("Original dataset:")
print(df.shape)


# Extract our features
feature_data = []

for url in df["URL"]:
    features = extract_features(url)
    feature_data.append(features)


# Convert features into a DataFrame
features_df = pd.DataFrame(feature_data)


# Add the label
features_df["label"] = df["label"].values


# Save the processed dataset
features_df.to_csv("processed_dataset.csv", index=False)


print("\nProcessed dataset:")
print(features_df.shape)


print("\nFirst 5 rows:")
print(features_df.head())


print("\nSaved as:")
print("processed_dataset.csv")