"""
MarketVerse Lab
guardian_health.py

Purpose:
Central Guardian Health Engine.
Evaluates overall project health.
"""


class GuardianHealth:
    def __init__(self):
        self.guardian = None

    # ----------------------------------------
    # Guardian Connection
    # ----------------------------------------

    def connect_guardian(self, guardian):
        self.guardian = guardian

    # ----------------------------------------
    # Module Status
    # ----------------------------------------

    def module_status(self):

        if self.guardian is None:
            return {}

        return {
            "ProjectMapper": self.guardian.mapper_ready(),
            "DependencyGraph": self.guardian.dependency_ready(),
            "IntegrationChecker": self.guardian.integration_ready(),
            "ErrorIntelligence": self.guardian.error_ready(),
            "KnowledgeBase": self.guardian.knowledge_ready(),
            "ChangePlanner": self.guardian.change_ready(),
            "AutoPatchEngine": self.guardian.patch_ready(),
            "ProjectMemory": self.guardian.memory_ready(),
            "LiveMonitor": self.guardian.monitor_ready(),
            "WorkflowEngine": self.guardian.workflow_ready(),
            "AIAssistant": self.guardian.assistant_ready(),
            "ImportAnalyzer": self.guardian.import_ready(),
            "GuardianHealth": self.is_ready(),
        }

    # ----------------------------------------
    # Health Score
    # ----------------------------------------

    def health_score(self):

        status = self.module_status()

        if not status:
            return 0

        total = len(status)
        healthy = sum(status.values())

        return round((healthy / total) * 100)

    # ----------------------------------------
    # Health Status
    # ----------------------------------------

    def health_status(self):

        score = self.health_score()

        if score >= 90:
            return "PASS"

        if score >= 70:
            return "WARNING"

        return "FAIL"

    # ----------------------------------------
    # Statistics
    # ----------------------------------------

    def statistics(self):

        status = self.module_status()

        total = len(status)
        healthy = sum(status.values())
        unhealthy = total - healthy

        return {
            "total_modules": total,
            "healthy_modules": healthy,
            "unhealthy_modules": unhealthy,
        }

    # ----------------------------------------
    # Report
    # ----------------------------------------

    def report(self):

        return {
            "status": self.health_status(),
            "score": self.health_score(),
            "statistics": self.statistics(),
            "modules": self.module_status(),
        }

    # ----------------------------------------
    # Ready Check
    # ----------------------------------------

    def is_ready(self):

        return self.guardian is not None

    # ----------------------------------------
    # String Representation
    # ----------------------------------------

    def __str__(self):

        return "GuardianHealth()"

    __repr__ = __str__
