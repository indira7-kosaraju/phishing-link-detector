import pandas as pd

df = pd.read_csv("PhiUSIIL_Phishing_URL_Dataset.csv")

print("Label 0 examples:")
print(df[df["label"] == 0]["URL"].head(10))

print("\nLabel 1 examples:")
print(df[df["label"] == 1]["URL"].head(10))