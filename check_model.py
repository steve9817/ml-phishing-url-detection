import joblib


model = joblib.load("model/phishing_model.pkl")

feature_names = [
    "URL Length",
    "Dot Count",
    "Hyphen Count",
    "Digit Count",
    "Special Character Count",
    "Contains @",
    "Uses HTTPS",
    "Contains IP",
    "Suspicious Word Count",
    "Path Length"
]

importances = model.feature_importances_

results = sorted(
    zip(feature_names, importances),
    key=lambda x: x[1],
    reverse=True
)

print("\nFeature Importance")
print("------------------------------")

for feature, importance in results:
    print(f"{feature:25} {importance:.4f}")