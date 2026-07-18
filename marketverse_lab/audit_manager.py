"""
MarketVerse Lab
audit_manager.py

Purpose:
Maintain audit logs for Guardian.
"""

from datetime import datetime


class AuditManager:

    def __init__(self):
        self.guardian = None
        self.logs = []

    def connect_guardian(self, guardian):
        self.guardian = guardian

    def log(self, action, details=""):

        entry = {
            "time": datetime.now().isoformat(),
            "action": action,
            "details": details
        }

        self.logs.append(entry)

        return entry

    def history(self):
        return self.logs

    def clear(self):
        self.logs.clear()

        return {
            "status": "SUCCESS"
        }

    def report(self):

        return {
            "connected": self.guardian is not None,
            "total_logs": len(self.logs),
            "last_log": self.logs[-1] if self.logs else None
        }

    def is_ready(self):
        return self.guardian is not None
