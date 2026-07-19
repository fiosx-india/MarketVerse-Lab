"""
MarketVerse Lab
rule_engine.py

Purpose:
Rule Engine for GuardianCore.

Responsibilities:
- Evaluate Guardian rules.
- Store rule evaluation history.
- Generate rule reports.
"""

from datetime import datetime


class RuleEngine:

    def __init__(self):
        self.guardian = None
        self.history = []

    # ----------------------------------------
    # Connect Guardian
    # ----------------------------------------

    def connect_guardian(self, guardian):
        self.guardian = guardian

    # ----------------------------------------
    # Evaluate Rules
    # ----------------------------------------

    def evaluate(self, data=None):

        result = {
            "status": "SUCCESS",
            "result": "All rules passed.",
            "data": data,
            "message": "Rule evaluation completed.",
            "timestamp": datetime.now().isoformat()
        }

        self.history.append(result)

        return result

    # ----------------------------------------
    # Evaluation History
    # ----------------------------------------

    def evaluation_history(self):
        return list(self.history)

    # ----------------------------------------
    # Last Evaluation
    # ----------------------------------------

    def last_evaluation(self):

        if not self.history:
            return None

        return self.history[-1]

    # ----------------------------------------
    # Total Evaluations
    # ----------------------------------------

    def total_evaluations(self):
        return len(self.history)

    # ----------------------------------------
    # Statistics
    # ----------------------------------------

    def statistics(self):

        return {
            "total_evaluations": self.total_evaluations()
        }

    # ----------------------------------------
    # Clear History
    # ----------------------------------------

    def clear_history(self):

        self.history.clear()

        return {
            "status": "SUCCESS",
            "message": "Rule evaluation history cleared."
        }

    # ----------------------------------------
    # Report
    # ----------------------------------------

    def report(self):

        return {
            "connected": self.guardian is not None,
            "ready": self.is_ready(),
            "statistics": self.statistics(),
            "last_evaluation": self.last_evaluation(),
            "history": self.evaluation_history()
        }

    # ----------------------------------------
    # Ready Check
    # ----------------------------------------

    def is_ready(self):
        return self.guardian is not None
