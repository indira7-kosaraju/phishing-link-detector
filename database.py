import sqlite3
from datetime import datetime
from zoneinfo import ZoneInfo


def create_database():

    connection = sqlite3.connect("phishing_scans.db")

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS scans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT NOT NULL,
            result TEXT NOT NULL,
            risk_score REAL NOT NULL,
            scan_time TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def save_scan(url, result, risk_score):

    connection = sqlite3.connect("phishing_scans.db")

    cursor = connection.cursor()

    # Get current Indian Standard Time
    india_time = datetime.now(
        ZoneInfo("Asia/Kolkata")
    ).strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO scans (url, result, risk_score, scan_time)
        VALUES (?, ?, ?, ?)
    """, (
        url,
        result,
        risk_score,
        india_time
    ))

    connection.commit()
    connection.close()


def get_scans():

    connection = sqlite3.connect("phishing_scans.db")

    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, url, result, risk_score, scan_time
        FROM scans
        ORDER BY id DESC
    """)

    scans = cursor.fetchall()

    connection.close()

    return scans
def get_dashboard_stats():

    connection = sqlite3.connect("phishing_scans.db")

    cursor = connection.cursor()

    # Total number of scans
    cursor.execute("""
        SELECT COUNT(*) FROM scans
    """)
    total_scans = cursor.fetchone()[0]

    # Number of phishing scans
    cursor.execute("""
        SELECT COUNT(*)
        FROM scans
        WHERE result LIKE '%PHISHING%'
    """)
    phishing_scans = cursor.fetchone()[0]

    # Number of legitimate scans
    cursor.execute("""
        SELECT COUNT(*)
        FROM scans
        WHERE result LIKE '%LEGITIMATE%'
    """)
    legitimate_scans = cursor.fetchone()[0]

    # High-risk scans
    cursor.execute("""
        SELECT COUNT(*)
        FROM scans
        WHERE risk_score >= 70
    """)
    high_risk_scans = cursor.fetchone()[0]

    # Recent scans
    cursor.execute("""
        SELECT id, url, result, risk_score, scan_time
        FROM scans
        ORDER BY id DESC
        LIMIT 10
    """)
    recent_scans = cursor.fetchall()

    connection.close()

    return (
        total_scans,
        phishing_scans,
        legitimate_scans,
        high_risk_scans,
        recent_scans
    )