"""
MarketVerse Lab
resource_manager.py

Purpose:
Resource Manager for GuardianCore.

Responsibilities:
- Allocate resources.
- Release resources.
- Track resource history.
- Generate resource reports.
"""

from datetime import datetime


class ResourceManager:

    def __init__(self):
        self.guardian = None
        self.resources = {}
        self.history = []

    # ----------------------------------------
    # Connect Guardian
    # ----------------------------------------

    def connect_guardian(self, guardian):
        self.guardian = guardian

    # ----------------------------------------
    # Allocate Resource
    # ----------------------------------------

    def allocate(self, name, value):

        self.resources[name] = value

        self.history.append({
            "action": "ALLOCATE",
            "resource": name,
            "value": value,
            "timestamp": datetime.now().isoformat()
        })

        return {
            "status": "SUCCESS",
            "resource": name,
            "value": value
        }

    # ----------------------------------------
    # Get Resource
    # ----------------------------------------

    def get(self, name):
        return self.resources.get(name)

    # ----------------------------------------
    # Resource Exists
    # ----------------------------------------

    def exists(self, name):
        return name in self.resources

    # ----------------------------------------
    # Release Resource
    # ----------------------------------------

    def release(self, name):

        if name not in self.resources:
            return {
                "status": "NOT_FOUND",
                "resource": name
            }

        value = self.resources.pop(name)

        self.history.append({
            "action": "RELEASE",
            "resource": name,
            "value": value,
            "timestamp": datetime.now().isoformat()
        })

        return {
            "status": "SUCCESS",
            "resource": name,
            "value": value
        }

    # ----------------------------------------
    # Total Resources
    # ----------------------------------------

    def total_resources(self):
        return len(self.resources)

    # ----------------------------------------
    # Last Action
    # ----------------------------------------

    def last_action(self):

        if not self.history:
            return None

        return self.history[-1]

    # ----------------------------------------
    # Resource History
    # ----------------------------------------

    def resource_history(self):
        return list(self.history)

    # ----------------------------------------
    # Clear Resources
    # ----------------------------------------

    def clear(self):

        self.resources.clear()
        self.history.clear()

        return {
            "status": "SUCCESS",
            "message": "All resources cleared."
        }

    # ----------------------------------------
    # Status
    # ----------------------------------------

    def status(self):

        return {
            "total_resources": self.total_resources(),
            "resources": dict(self.resources)
        }

    # ----------------------------------------
    # Report
    # ----------------------------------------

    def report(self):

        return {
            "connected": self.guardian is not None,
            "ready": self.is_ready(),
            "total_resources": self.total_resources(),
            "resources": dict(self.resources),
            "last_action": self.last_action(),
            "history": self.resource_history()
        }

    # ----------------------------------------
    # Ready Check
    # ----------------------------------------

    def is_ready(self):
        return self.guardian is not None
