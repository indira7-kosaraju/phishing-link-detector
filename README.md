# 🛡️ PhishGuard – Phishing URL Detection System

PhishGuard is a machine-learning-based cybersecurity application that detects whether a URL is potentially **phishing or legitimate**.

The system extracts security-related features from a URL, analyzes them using a trained **Random Forest classification model**, calculates a phishing risk score, and provides an explanation of suspicious URL characteristics.

The application also provides **scan history and a security dashboard** using Flask and SQLite.

---

## 🚀 Project Overview

Phishing attacks are one of the most common cybersecurity threats. Attackers often create malicious URLs that look similar to legitimate websites and use them to steal credentials, financial information, or personal data.

PhishGuard aims to provide a simple way for users to analyze URLs before visiting them.

### Main Workflow

```text
User enters URL
       ↓
URL Feature Extraction
       ↓
Machine Learning Model
       ↓
Random Forest Prediction
       ↓
Phishing Probability
       ↓
Risk Score
       ↓
Security Analysis
       ↓
Store Scan in SQLite
       ↓
History / Dashboard



📁 Project Structure

phishing-link-detector/
│
├── templates/
│   ├── index.html
│   ├── history.html
│   └── dashboard.html
│
├── static/
│   └── style.css
│
├── app.py
├── feature_extraction.py
├── url_analysis.py
├── database.py
├── check_dataset.py
├── prepare_dataset.py
├── train_model.py
├── predict_url.py
│
├── phishing_model.pkl
├── processed_dataset.csv
├── phishing_scans.db
├── PhiUSIIL_Phishing_URL_Dataset.csv
│
├── requirements.txt
├── .gitignore
└── README.md



🛠️ Technology Stack

Programming
    Python 3
Machine Learning
    Pandas
    NumPy
    Scikit-learn
    Random Forest
    Joblib  
Web Development
    Flask
    HTML5
    CSS3
    Jinja2
Database
    SQLite




⚙️ Installation


1. Clone the Repository
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd phishing-link-detector

2. Create Virtual Environment
python3 -m venv venv

3. Activate Virtual Environment
macOS/Linux:
source venv/bin/activate

Windows:
venv\Scripts\activate

4. Install Dependencies
pip install -r requirements.txt
▶️ Run the Application
Activate the virtual environment:
source venv/bin/activate

Start Flask:
python3 app.py

Open the application in a browser:
http://127.0.0.1:5001


🧪 Model Training

To recreate the processed dataset:
python3 prepare_dataset.py

To train the model:
python3 train_model.py

The trained model will be saved as:
phishing_model.pkl



📊 Application Workflow
1. Enter URL

The user enters a URL into the PhishGuard scanner.

2. Extract Features

The system extracts URL characteristics.

3. Predict

The Random Forest model predicts whether the URL is phishing or legitimate.

4. Calculate Risk

The phishing probability is converted into a percentage.

5. Analyze

Additional rules identify suspicious URL characteristics.

6. Store

The scan result is stored in SQLite.

7. Monitor

The user can view scan history and dashboard statistics.






🔐 Security Considerations

PhishGuard performs URL-based analysis and does not need to open the submitted URL for the basic prediction process.

Users should avoid opening suspicious URLs directly.

The current system is a cybersecurity assistance tool and should not be considered a replacement for professional security products or threat-intelligence systems.




⚠️ Limitations
The current model primarily uses URL-based features.
It does not currently inspect complete webpage content.
It does not use live threat-intelligence services.
It does not currently perform domain reputation or domain-age checks.
The current model was trained using a 10,000-sample processed dataset.
Machine learning predictions are not guaranteed to be correct for every real-world URL.




🔮 Future Improvements
Real-time threat intelligence integration
Domain age and reputation analysis
SSL certificate analysis
Webpage content analysis
Advanced machine learning model comparison
User authentication
Browser extension
Email phishing detection
Cloud deployment
Explainable AI using SHAP or LIME


## Live Demo
🚀 Live Demo:https://phishing-link-detector-36nh.onrender.com
