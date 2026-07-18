"""
MarketVerse Lab
impact_analyzer.py

Purpose:
Analyze the impact of changing a file.
"""

class ImpactAnalyzer:

    def __init__(self):
        self.guardian = None

    def connect_guardian(self, guardian):
        self.guardian = guardian

    def impact(self, file_name):

        if self.guardian is None:
            return []

        try:
            return self.guardian.dependency_graph.impact(file_name)
        except Exception:
            return []

    def impact_level(self, file_name):

        count = len(self.impact(file_name))

        if count == 0:
            return "LOW"

        if count <= 3:
            return "MEDIUM"

        return "HIGH"

    def analyze(self, file_name):

        affected = self.impact(file_name)

        return {
            "file": file_name,
            "affected_files": affected,
            "affected_count": len(affected),
            "impact_level": self.impact_level(file_name),
        }

    def report(self):

        if self.guardian is None:
            return {"connected": False}

        return {
            "connected": True
        }

    def is_ready(self):
        return self.guardian is not None
