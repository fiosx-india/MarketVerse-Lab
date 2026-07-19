"""
MarketVerse Lab
metrics_manager.py

Purpose:
Metrics Manager for GuardianCore.
"""


class MetricsManager:

    def __init__(self):
        self.guardian = None
        self.data = {
            "cpu": 0,
            "memory": 0,
            "disk": 0,
            "modules": 0
        }

    def connect_guardian(self, guardian):
        self.guardian = guardian

    def metrics(self):

        if self.guardian:
            blueprint = getattr(self.guardian, "blueprint", None)

            if blueprint:
                self.data["modules"] = len(
                    getattr(blueprint, "modules", {})
                )
            else:
                self.data["modules"] = 0
        else:
            self.data["modules"] = 0

        return dict(self.data)

    def report(self):
        return {
            "connected": self.guardian is not None,
            "ready": self.is_ready(),
            "metrics": self.metrics()
        }

    def is_ready(self):
        return self.guardian is not None
