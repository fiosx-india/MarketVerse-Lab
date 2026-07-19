"""
MarketVerse Lab
metrics_manager.py

Purpose:
Metrics Manager for GuardianCore.

Responsibilities:
- Collect system metrics.
- Track metric history.
- Generate metric reports.
"""

from datetime import datetime


class MetricsManager:

    def __init__(self):
        self.guardian = None
        self.data = {
            "cpu": 0,
            "memory": 0,
            "disk": 0,
            "modules": 0
        }
        self.history = []

    # ----------------------------------------
    # Connect Guardian
    # ----------------------------------------

    def connect_guardian(self, guardian):
        self.guardian = guardian

    # ----------------------------------------
    # Collect Metrics
    # ----------------------------------------

    def metrics(self):

        if self.guardian:
            blueprint = getattr(self.guardian, "blueprint", None)

            if blueprint:
                self.data["modules"] = len(
                    getattr(blueprint, "modules", {})
                )
            else:
                self.data["modules"] = 0
        else:
            self.data["modules"] = 0

        snapshot = dict(self.data)
        snapshot["timestamp"] = datetime.now().isoformat()

        self.history.append(snapshot)

        return dict(snapshot)

    # ----------------------------------------
    # Last Metrics
    # ----------------------------------------

    def last_metrics(self):

        if not self.history:
            return None

        return self.history[-1]

    # ----------------------------------------
    # Total Samples
    # ----------------------------------------

    def total_samples(self):
        return len(self.history)

    # ----------------------------------------
    # Metrics History
    # ----------------------------------------

    def metrics_history(self):
        return list(self.history)

    # ----------------------------------------
    # Clear Metrics
    # ----------------------------------------

    def clear(self):

        self.history.clear()

        self.data = {
            "cpu": 0,
            "memory": 0,
            "disk": 0,
            "modules": 0
        }

        return {
            "status": "SUCCESS",
            "message": "Metrics history cleared."
        }

    # ----------------------------------------
    # Statistics
    # ----------------------------------------

    def statistics(self):

        return {
            "total_samples": self.total_samples(),
            "latest_modules": self.data["modules"]
        }

    # ----------------------------------------
    # Report
    # ----------------------------------------

    def report(self):

        return {
            "connected": self.guardian is not None,
            "ready": self.is_ready(),
            "statistics": self.statistics(),
            "last_metrics": self.last_metrics(),
            "metrics": dict(self.data),
            "history": self.metrics_history()
        }

    # ----------------------------------------
    # Ready Check
    # ----------------------------------------

    def is_ready(self):
        return self.guardian is not None
