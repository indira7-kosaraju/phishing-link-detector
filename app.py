from flask import Flask, render_template, request
import joblib
import pandas as pd

from feature_extraction import extract_features
from database import (
    create_database,
    save_scan,
    get_scans,
    get_dashboard_stats
)
from url_analysis import analyze_url


# Create Flask application
app = Flask(__name__)


# Load trained ML model
model = joblib.load("phishing_model.pkl")


# Create SQLite database/table if it doesn't exist
create_database()


# ==========================================
# HOME / URL SCANNER
# ==========================================

@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    risk_score = None
    warnings = []

    if request.method == "POST":

        # Get URL entered by user
        url = request.form["url"].strip()

        # Extract URL features
        features = extract_features(url)

        # Convert features into DataFrame
        features_df = pd.DataFrame([features])

        # Make prediction
        prediction = model.predict(features_df)[0]

        # Get prediction probabilities
        probabilities = model.predict_proba(features_df)[0]

        # Probability of phishing class
        phishing_probability = probabilities[0]

        # Convert probability to percentage
        risk_score = round(
            phishing_probability * 100,
            2
        )

        # Determine result
        if prediction == 0:
            result = "🚨 PHISHING URL"
        else:
            result = "✅ LEGITIMATE URL"

        # Analyze URL characteristics
        warnings = analyze_url(features)

        # Save scan to database
        save_scan(
            url,
            result,
            risk_score
        )

    return render_template(
        "index.html",
        result=result,
        risk_score=risk_score,
        warnings=warnings
    )


# ==========================================
# SCAN HISTORY
# ==========================================

@app.route("/history")
def history():

    # Get previous scans
    scans = get_scans()

    return render_template(
        "history.html",
        scans=scans
    )


# ==========================================
# SECURITY DASHBOARD
# ==========================================

@app.route("/dashboard")
def dashboard():

    # Get dashboard statistics
    (
        total_scans,
        phishing_scans,
        legitimate_scans,
        high_risk_scans,
        recent_scans
    ) = get_dashboard_stats()

    return render_template(
        "dashboard.html",
        total_scans=total_scans,
        phishing_scans=phishing_scans,
        legitimate_scans=legitimate_scans,
        high_risk_scans=high_risk_scans,
        recent_scans=recent_scans
    )


# ==========================================
# START APPLICATION
# ==========================================

if __name__ == "__main__":
    import os

    port = int(os.environ.get("PORT", 5001))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )