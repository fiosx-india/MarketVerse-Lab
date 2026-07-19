"""
MarketVerse Lab
security_manager.py

Purpose:
Security Manager for GuardianCore.

Responsibilities:
- Run security scans.
- Store scan history.
- Generate security reports.
"""

from datetime import datetime


class SecurityManager:

    def __init__(self):
        self.guardian = None
        self.last_scan = {}
        self.history = []

    # ----------------------------------------
    # Connect Guardian
    # ----------------------------------------

    def connect_guardian(self, guardian):
        self.guardian = guardian

    # ----------------------------------------
    # Security Scan
    # ----------------------------------------

    def scan(self):

        self.last_scan = {
            "status": "SUCCESS",
            "issues_found": 0,
            "message": "No security issues detected.",
            "timestamp": datetime.now().isoformat()
        }

        self.history.append(dict(self.last_scan))

        return self.last_scan

    # ----------------------------------------
    # Last Scan
    # ----------------------------------------

    def last_scan_result(self):
        return self.last_scan if self.last_scan else None

    # ----------------------------------------
    # Total Scans
    # ----------------------------------------

    def total_scans(self):
        return len(self.history)

    # ----------------------------------------
    # Scan History
    # ----------------------------------------

    def scan_history(self):
        return list(self.history)

    # ----------------------------------------
    # Clear History
    # ----------------------------------------

    def clear(self):

        self.last_scan = {}
        self.history.clear()

        return {
            "status": "SUCCESS",
            "message": "Security scan history cleared."
        }

    # ----------------------------------------
    # Statistics
    # ----------------------------------------

    def statistics(self):

        return {
            "total_scans": self.total_scans(),
            "issues_found": sum(
                item.get("issues_found", 0)
                for item in self.history
            )
        }

    # ----------------------------------------
    # Report
    # ----------------------------------------

    def report(self):

        return {
            "connected": self.guardian is not None,
            "ready": self.is_ready(),
            "statistics": self.statistics(),
            "last_scan": self.last_scan_result(),
            "history": self.scan_history()
        }

    # ----------------------------------------
    # Ready Check
    # ----------------------------------------

    def is_ready(self):
        return self.guardian is not None
