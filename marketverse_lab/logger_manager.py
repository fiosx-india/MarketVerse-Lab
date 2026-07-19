"""
MarketVerse Lab
logger_manager.py

Purpose:
Logger Manager for GuardianCore.
"""


from datetime import datetime


class LoggerManager:

    def __init__(self):
        self.guardian = None
        self.logs = []

    def connect_guardian(self, guardian):
        self.guardian = guardian

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

    def history(self):
        return list(self.logs)

    def clear(self):
        self.logs.clear()

        return {
            "status": "SUCCESS",
            "message": "Logs cleared."
        }

    def report(self):
        return {
            "connected": self.guardian is not None,
            "ready": self.is_ready(),
            "total_logs": len(self.logs),
            "logs": self.history()
        }

    def is_ready(self):
        return self.guardian is not None
