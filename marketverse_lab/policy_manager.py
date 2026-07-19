"""
MarketVerse Lab
policy_manager.py

Purpose:
Manage Guardian policies.
"""


class PolicyManager:

    def __init__(self):
        self.guardian = None
        self.policies = {}

    def connect_guardian(self, guardian):
        self.guardian = guardian

    def add_policy(self, name, value):

        self.policies[name] = value

        return {
            "status": "SUCCESS",
            "policy": name,
            "value": value
        }

    def get_policy(self, name):
        return self.policies.get(name)

    def remove_policy(self, name):

        if name in self.policies:
            del self.policies[name]

        return {
            "status": "SUCCESS"
        }

    def history(self):
        return self.policies

    def report(self):

        return {
            "connected": self.guardian is not None,
            "total_policies": len(self.policies),
            "policies": self.policies
        }

    def is_ready(self):
        return self.guardian is not None
