"""
MarketVerse Lab
automation_engine.py

Purpose:
Automation Engine for GuardianCore.

Responsibilities:
- Run automation tasks.
- Store automation execution history.
- Generate automation reports.
"""

from datetime import datetime


class AutomationEngine:

    def __init__(self):
        self.guardian = None
        self.history = []

    # ----------------------------------------
    # Connect Guardian
    # ----------------------------------------

    def connect_guardian(self, guardian):
        self.guardian = guardian

    # ----------------------------------------
    # Run Automation
    # ----------------------------------------

    def run(self, name, data=None):

        result = {
            "status": "SUCCESS",
            "automation": name,
            "data": data,
            "message": f"Automation '{name}' completed.",
            "timestamp": datetime.now().isoformat()
        }

        self.history.append(result)

        return result

    # ----------------------------------------
    # Automation History
    # ----------------------------------------

    def automation_history(self):
        return list(self.history)

    # ----------------------------------------
    # Last Automation
    # ----------------------------------------

    def last_automation(self):

        if not self.history:
            return None

        return self.history[-1]

    # ----------------------------------------
    # Total Automations
    # ----------------------------------------

    def total_automations(self):
        return len(self.history)

    # ----------------------------------------
    # Statistics
    # ----------------------------------------

    def statistics(self):

        return {
            "total_automations": self.total_automations()
        }

    # ----------------------------------------
    # Clear History
    # ----------------------------------------

    def clear_history(self):

        self.history.clear()

        return {
            "status": "SUCCESS",
            "message": "Automation history cleared."
        }

    # ----------------------------------------
    # Report
    # ----------------------------------------

    def report(self):

        return {
            "connected": self.guardian is not None,
            "ready": self.is_ready(),
            "statistics": self.statistics(),
            "last_automation": self.last_automation(),
            "history": self.automation_history()
        }

    # ----------------------------------------
    # Ready Check
    # ----------------------------------------

    def is_ready(self):
        return self.guardian is not None
