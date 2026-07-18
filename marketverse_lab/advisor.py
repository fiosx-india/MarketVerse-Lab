"""
MarketVerse Lab
advisor.py

Purpose:
Provide AI recommendations and
overall project health summary.
"""


class ProjectAdvisor:
    def __init__(self):

        self.guardian = None

    # ----------------------------------------

    def connect_guardian(self, guardian):

        self.guardian = guardian

    # ----------------------------------------

    def project_score(self):

        if self.guardian is None:
            return 0

        score = 100

        dependency = self.guardian.dependency_report()

        score -= dependency["statistics"]["missing_dependencies"] * 10
        score -= dependency["statistics"]["circular_dependencies"] * 20

        return max(score, 0)

    # ----------------------------------------

    def project_status(self):

        score = self.project_score()

        if score >= 90:
            return "EXCELLENT"

        if score >= 75:
            return "GOOD"

        if score >= 50:
            return "WARNING"

        return "CRITICAL"

    # ----------------------------------------

    def recommendations(self):

        dependency = self.guardian.dependency_report()

        advice = []

        if dependency["statistics"]["missing_dependencies"] > 0:
            advice.append("Resolve missing dependencies.")

        if dependency["statistics"]["circular_dependencies"] > 0:
            advice.append("Remove circular dependencies.")

        if not advice:
            advice.append("Project is healthy. Continue development.")

        return advice

    # ----------------------------------------

    def report(self):

        return {
            "score": self.project_score(),
            "status": self.project_status(),
            "recommendations": self.recommendations(),
        }

    # ----------------------------------------

    def is_ready(self):

        return self.guardian is not None

    # ----------------------------------------

    def __str__(self):

        return (
            f"ProjectAdvisor("
            f"score={self.project_score()}, "
            f"status={self.project_status()})"
        )

    __repr__ = __str__
