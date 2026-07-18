"""
MarketVerse Lab
risk_analyzer.py

Purpose:
Analyze project risk before making changes.
"""

class RiskAnalyzer:

    def __init__(self):

        self.guardian = None

    # ----------------------------------------

    def connect_guardian(self, guardian):

        self.guardian = guardian

    # ----------------------------------------

    def risk_score(self, file_name):

        if self.guardian is None:
            return 0

        affected = self.guardian.dependency_graph.impact(file_name)

        return len(affected)

    # ----------------------------------------

    def risk_level(self, file_name):

        score = self.risk_score(file_name)

        if score == 0:
            return "LOW"

        if score <= 3:
            return "MEDIUM"

        return "HIGH"

    # ----------------------------------------

    def analyze(self, file_name):

        affected = self.guardian.dependency_graph.impact(file_name)

        return {
            "file": file_name,
            "risk_score": len(affected),
            "risk_level": self.risk_level(file_name),
            "affected_files": affected,
        }

    # ----------------------------------------

    def report(self):

        if self.guardian is None:

            return {
                "connected": False
            }

        report = {}

        for file_name in self.guardian.dependency_graph.nodes.keys():

            report[file_name] = self.analyze(file_name)

        return report

    # ----------------------------------------

    def is_ready(self):

        return self.guardian is not None
