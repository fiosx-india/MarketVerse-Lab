"""
MarketVerse Lab
state_manager.py

Purpose:
Maintain current project state.
"""

from datetime import datetime


class StateManager:

    def __init__(self):
        self.guardian = None
        self.current_state = "IDLE"
        self.history = []

    def connect_guardian(self, guardian):
        self.guardian = guardian

    def set_state(self, state):

        self.current_state = state

        self.history.append({
            "state": state,
            "time": datetime.now().isoformat()
        })

        return {
            "status": "SUCCESS",
            "state": state
        }

    def get_state(self):
        return {
            "current_state": self.current_state
        }

    def state_history(self):
        return {
            "count": len(self.history),
            "history": self.history
        }

    def report(self):
        return {
            "connected": self.guardian is not None,
            "current_state": self.current_state,
            "history_count": len(self.history)
        }

    def is_ready(self):
        return self.guardian is not None

    def __str__(self):
        return "StateManager"

    __repr__ = __str__
