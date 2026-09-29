# ML-Based Phishing URL Detection

A machine learning project that detects whether a URL is **phishing or legitimate** based on characteristics extracted from the URL.

The project uses a Random Forest classifier and provides a FastAPI REST API for URL prediction.

## Project Flow

```text
URL
 ↓
Feature Extraction
 ↓
Machine Learning Model
 ↓
Phishing / Legitimate
 ↓
Risk Probability
```

## Dataset

The project uses the PhiUSIIL Phishing URL Dataset.

The dataset contains 235,795 URLs:

- 134,850 legitimate URLs
- 100,945 phishing URLs

For this project, the raw URL and label were used. URL features were extracted separately instead of directly using the pre-generated features in the dataset.

Labels:

```text
0 = Phishing
1 = Legitimate
```

## Features

The following features are extracted from each URL:

- URL length
- Number of dots
- Number of hyphens
- Number of digits
- Number of special characters
- Presence of `@`
- HTTPS usage
- IP address usage
- Suspicious words
- URL path length

Examples of suspicious words include:

```text
login
verify
secure
account
password
banking
update
```

## Machine Learning

The dataset is divided into:

```text
80% Training Data
20% Testing Data
```

The project uses a **Random Forest Classifier** with 100 decision trees.

The trained model is saved as:

```text
model/phishing_model.pkl
```

## Model Results

The model was tested using 47,159 URLs.

Confusion Matrix:

```text
[[19993   196]
 [   23 26947]]
```

Results:

- Phishing URLs correctly detected: 19,993
- Phishing URLs incorrectly classified as legitimate: 196
- Legitimate URLs incorrectly classified as phishing: 23
- Legitimate URLs correctly detected: 26,947

The model achieved approximately 99% recall for phishing URLs on the test dataset.

## Feature Importance

The most important features identified by the Random Forest were:

```text
Uses HTTPS                0.4411
Path Length               0.3320
Special Character Count   0.0789
Digit Count               0.0750
URL Length                0.0414
Dot Count                 0.0170
Hyphen Count              0.0120
Suspicious Word Count     0.0026
Contains IP               0.0000
Contains @                0.0000
```

The model relies heavily on HTTPS usage and path length. This may indicate dataset bias, so the current model should be considered a learning/project implementation rather than a production phishing detection system.

## API

The project provides a FastAPI REST API.

Start the API:

```bash
uvicorn main:app --reload
```

Open the API documentation:

```text
http://127.0.0.1:8000/docs
```

Example request:

```json
{
  "url": "https://www.google.com"
}
```

Example response:

```json
{
  "url": "https://www.google.com",
  "prediction": "legitimate",
  "phishing_probability": 2.5,
  "legitimate_probability": 97.5
}
```

## Project Structure

```text
phishing-url-detector/
│
├── data/
│   └── phishing.csv
│
├── model/
│   └── phishing_model.pkl
│
├── features.py
├── train.py
├── predict.py
├── check_model.py
├── main.py
├── requirements.txt
└── README.md
```

## Technologies

- Python
- Pandas
- Scikit-learn
- Random Forest
- FastAPI
- Joblib

## Run the Project

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Train the model:

```bash
python train.py
```

Test a URL from the command line:

```bash
python predict.py
```

Start the API:

```bash
uvicorn main:app --reload
```

## Limitations

This is an educational cybersecurity and machine learning project.

The current version mainly uses lexical URL features. It does not currently use live domain reputation, DNS information, WHOIS data, SSL certificate analysis, or external threat intelligence.

Future improvements could include these features and testing the model against additional independent phishing datasets.