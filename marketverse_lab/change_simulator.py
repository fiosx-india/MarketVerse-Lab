"""
MarketVerse Lab
change_simulator.py

Purpose:
Simulate a file change before applying it.
"""

class ChangeSimulator:

    def __init__(self):
        self.guardian = None

    def connect_guardian(self, guardian):
        self.guardian = guardian

    def simulate(self, file_name, action="modify"):

        if self.guardian is None:
            return {}

        try:
            risk = self.guardian.risk_analyzer.analyze(file_name)
        except Exception:
            risk = {}

        try:
            impact = self.guardian.impact_analyzer.analyze(file_name)
        except Exception:
            impact = {}

        try:
            plan = self.guardian.change_planner.generate_plan(
                file_name,
                action
            )
        except Exception:
            plan = {}

        return {
            "file": file_name,
            "action": action,
            "risk": risk,
            "impact": impact,
            "plan": plan,
            "simulation": "READY"
        }

    def report(self):

        return {
            "connected": self.guardian is not None
        }

    def is_ready(self):

        return self.guardian is not None
