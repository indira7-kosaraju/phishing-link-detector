from urllib.parse import urlparse


def analyze_url(features):

    warnings = []

    if features["has_https"] == 0:
        warnings.append("⚠️ URL does not use HTTPS")

    if features["has_ip_address"] == 1:
        warnings.append("⚠️ URL uses an IP address instead of a domain name")

    if features["has_at_symbol"] == 1:
        warnings.append("⚠️ URL contains an @ symbol")

    if features["has_suspicious_word"] == 1:
        warnings.append("⚠️ URL contains suspicious keywords")

    if features["num_hyphens"] >= 2:
        warnings.append("⚠️ URL contains multiple hyphens")

    if features["num_special_chars"] >= 6:
        warnings.append("⚠️ URL contains many special characters")

    if features["url_length"] >= 75:
        warnings.append("⚠️ URL is unusually long")

    if features["num_dots"] >= 3:
        warnings.append("⚠️ URL contains multiple subdomains")

    if not warnings:
        warnings.append("✅ No obvious suspicious URL characteristics detected")

    return warnings