import joblib

from features import extract_features


model = joblib.load("model/phishing_model.pkl")


def predict_url(url):

    features = extract_features(url)

    prediction = model.predict([features])[0]
    probabilities = model.predict_proba([features])[0]

    phishing_probability = probabilities[0]
    legitimate_probability = probabilities[1]

    print("\n------------------------------")
    print("URL:", url)

    if prediction == 0:
        print("Prediction: PHISHING")
    else:
        print("Prediction: LEGITIMATE")

    print(
        f"Phishing Probability: "
        f"{phishing_probability * 100:.2f}%"
    )

    print(
        f"Legitimate Probability: "
        f"{legitimate_probability * 100:.2f}%"
    )

    print("------------------------------")


if __name__ == "__main__":

    url = input("Enter URL: ")

    predict_url(url)