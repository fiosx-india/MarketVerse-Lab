"""
MarketVerse Lab
session_manager.py

Purpose:
Manage project sessions.
Save and restore active working sessions.
"""

from datetime import datetime


class SessionManager:

    def __init__(self):
        self.guardian = None
        self.sessions = {}
        self.active_session = None

    def connect_guardian(self, guardian):
        self.guardian = guardian

    def create_session(self, name="Default"):

        session = {
            "name": name,
            "created": datetime.now().isoformat(),
            "status": "ACTIVE"
        }

        self.sessions[name] = session
        self.active_session = name

        return {
            "status": "SUCCESS",
            "session": session
        }

    def load_session(self, name):

        if name not in self.sessions:
            return {
                "status": "FAILED",
                "message": "Session not found"
            }

        self.active_session = name

        return {
            "status": "SUCCESS",
            "session": self.sessions[name]
        }

    def active(self):
        return self.active_session

    def list_sessions(self):
        return {
            "count": len(self.sessions),
            "active": self.active_session,
            "sessions": list(self.sessions.keys())
        }

    def report(self):
        return {
            "connected": self.guardian is not None,
            "session_count": len(self.sessions),
            "active_session": self.active_session
        }

    def is_ready(self):
        return self.guardian is not None

    def __str__(self):
        return "SessionManager"

    __repr__ = __str__
