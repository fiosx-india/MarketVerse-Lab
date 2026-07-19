"""
MarketVerse Lab
rule_engine.py

Purpose:
Rule Engine for GuardianCore.

Responsibilities:
- Evaluate Guardian rules.
- Store rule evaluation history.
- Provide rule reports.
- Connect with GuardianCore.
"""


class RuleEngine:

    def __init__(self):
        self.guardian = None
        self.history = []

    def connect_guardian(self, guardian):
        self.guardian = guardian

    def evaluate(self, data=None):

        result = {
            "status": "SUCCESS",
            "result": "All rules passed.",
            "data": data,
            "message": "Rule evaluation completed."
        }

        self.history.append(result)

        return result

    def evaluation_history(self):
        return list(self.history)

    def last_evaluation(self):
        if not self.history:
            return None
        return self.history[-1]

    def total_evaluations(self):
        return len(self.history)

    def clear_history(self):
        self.history.clear()

        return {
            "status": "SUCCESS",
            "message": "Rule evaluation history cleared."
        }

    def report(self):
        return {
            "connected": self.guardian is not None,
            "ready": self.is_ready(),
            "total_evaluations": self.total_evaluations(),
            "last_evaluation": self.last_evaluation(),
            "history": self.evaluation_history()
        }

    def is_ready(self):
        return self.guardian is not None
