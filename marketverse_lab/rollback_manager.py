"""
MarketVerse Lab
rollback_manager.py

Purpose:
Rollback project changes using
Project Memory.
"""


class RollbackManager:

    def __init__(self):
        self.guardian = None

    def connect_guardian(self, guardian):
        self.guardian = guardian

    def rollback(self, file_name):

        if self.guardian is None:
            return {}

        history = self.guardian.project_memory.report()

        return {
            "file": file_name,
            "status": "READY",
            "rollback_available": True,
            "history": history
        }

    def preview(self, file_name):

        result = self.rollback(file_name)

        return {
            "file": file_name,
            "preview": True,
            "rollback": result
        }

    def report(self):

        return {
            "connected": self.guardian is not None
        }

    def is_ready(self):

        return self.guardian is not None

    def __str__(self):

        return "RollbackManager"

    __repr__ = __str__
