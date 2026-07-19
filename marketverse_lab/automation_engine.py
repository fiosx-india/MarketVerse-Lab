"""
MarketVerse Lab
automation_engine.py

Purpose:
Automation Engine for GuardianCore.

Responsibilities:
- Run automation tasks.
- Store automation execution history.
- Provide automation reports.
- Connect with GuardianCore.
"""


class AutomationEngine:

    def __init__(self):
        self.guardian = None
        self.history = []

    def connect_guardian(self, guardian):
        self.guardian = guardian

    def run(self, name, data=None):

        result = {
            "status": "SUCCESS",
            "automation": name,
            "data": data,
            "message": f"Automation '{name}' completed."
        }

        self.history.append(result)

        return result

    def automation_history(self):
        return list(self.history)

    def last_automation(self):
        if not self.history:
            return None
        return self.history[-1]

    def total_automations(self):
        return len(self.history)

    def clear_history(self):
        self.history.clear()

        return {
            "status": "SUCCESS",
            "message": "Automation history cleared."
        }

    def report(self):
        return {
            "connected": self.guardian is not None,
            "ready": self.is_ready(),
            "total_automations": self.total_automations(),
            "last_automation": self.last_automation(),
            "history": self.automation_history()
        }

    def is_ready(self):
        return self.guardian is not None
