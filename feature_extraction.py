import re
from urllib.parse import urlparse


def extract_features(url):

    parsed_url = urlparse(url)
    domain = parsed_url.netloc

    suspicious_words = [
        "login",
        "verify",
        "account",
        "update",
        "secure",
        "bank",
        "password",
        "signin",
        "confirm"
    ]

    features = {
        "url_length": len(url),

        "domain_length": len(domain),

        "num_dots": url.count("."),

        "num_slashes": url.count("/"),

        "num_hyphens": url.count("-"),

        "num_special_chars": len(
            re.findall(r"[^a-zA-Z0-9]", url)
        ),

        "has_https": 1 if parsed_url.scheme == "https" else 0,

        "has_at_symbol": 1 if "@" in url else 0,

        "has_ip_address": 1 if re.match(
            r"^\d+\.\d+\.\d+\.\d+$",
            domain
        ) else 0,

        "has_suspicious_word": 1 if any(
            word in url.lower()
            for word in suspicious_words
        ) else 0
    }

    return features