import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

from features import extract_features


print("Loading dataset...")

df = pd.read_csv("data/phishing.csv")

# We only need the raw URL and its correct label
df = df[["URL", "label"]].dropna()

print("Total URLs:", len(df))


print("Extracting features...")

X = df["URL"].apply(extract_features).tolist()

# Dataset:
# 1 = Legitimate
# 0 = Phishing
y = df["label"]


print("Splitting dataset...")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


print("Training Random Forest...")

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)


print("Testing model...")

predictions = model.predict(X_test)


print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))


print("\nClassification Report:")
print(
    classification_report(
        y_test,
        predictions,
        target_names=["Phishing", "Legitimate"]
    )
)


print("Saving model...")

joblib.dump(
    model,
    "model/phishing_model.pkl"
)

print("Model saved successfully!")