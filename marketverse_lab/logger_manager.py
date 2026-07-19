"""
MarketVerse Lab
logger_manager.py

Purpose:
Logger Manager for GuardianCore.

Responsibilities:
- Store log entries.
- Track log statistics.
- Generate log reports.
"""

from datetime import datetime


class LoggerManager:

    def __init__(self):
        self.guardian = None
        self.logs = []

    # ----------------------------------------
    # Connect Guardian
    # ----------------------------------------

    def connect_guardian(self, guardian):
        self.guardian = guardian

    # ----------------------------------------
    # Add Log
    # ----------------------------------------

    def log(self, level, message):

        entry = {
            "id": len(self.logs) + 1,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "level": level.upper(),
            "message": message
        }

        self.logs.append(entry)

        return {
            "status": "SUCCESS",
            "log": entry
        }

    # ----------------------------------------
    # Log History
    # ----------------------------------------

    def history(self):
        return list(self.logs)

    # ----------------------------------------
    # Last Log
    # ----------------------------------------

    def last_log(self):

        if not self.logs:
            return None

        return self.logs[-1]

    # ----------------------------------------
    # Total Logs
    # ----------------------------------------

    def total_logs(self):
        return len(self.logs)

    # ----------------------------------------
    # Statistics
    # ----------------------------------------

    def statistics(self):

        levels = {}

        for log in self.logs:
            level = log["level"]
            levels[level] = levels.get(level, 0) + 1

        return {
            "total_logs": self.total_logs(),
            "levels": levels
        }

    # ----------------------------------------
    # Clear Logs
    # ----------------------------------------

    def clear(self):

        self.logs.clear()

        return {
            "status": "SUCCESS",
            "message": "Logs cleared."
        }

    # ----------------------------------------
    # Report
    # ----------------------------------------

    def report(self):

        return {
            "connected": self.guardian is not None,
            "ready": self.is_ready(),
            "statistics": self.statistics(),
            "last_log": self.last_log(),
            "logs": self.history()
        }

    # ----------------------------------------
    # Ready Check
    # ----------------------------------------

    def is_ready(self):
        return self.guardian is not None
