"""
MarketVerse Lab
resource_manager.py

Purpose:
Resource Manager for GuardianCore.
"""


class ResourceManager:

    def __init__(self):
        self.guardian = None
        self.resources = {}

    def connect_guardian(self, guardian):
        self.guardian = guardian

    def allocate(self, name, value):
        self.resources[name] = value

        return {
            "status": "SUCCESS",
            "resource": name,
            "value": value
        }

    def get(self, name):
        return self.resources.get(name)

    def status(self):
        return {
            "total_resources": len(self.resources),
            "resources": dict(self.resources)
        }

    def report(self):
        return {
            "connected": self.guardian is not None,
            "total_resources": len(self.resources),
            "resources": dict(self.resources)
        }

    def is_ready(self):
        return self.guardian is not None
