"""
MarketVerse Lab
orchestrator.py

Purpose:
Coordinate Guardian modules.
"""


class Orchestrator:

    def __init__(self):
        self.guardian = None
        self.modules = {}

    def connect_guardian(self, guardian):
        self.guardian = guardian

    def register(self, name, module):
        self.modules[name] = module

        return {
            "status": "SUCCESS",
            "module": name
        }

    def get(self, name):
        return self.modules.get(name)

    def list_modules(self):
        return list(self.modules.keys())

    def report(self):
        return {
            "connected": self.guardian is not None,
            "total_modules": len(self.modules),
            "modules": self.list_modules()
        }

    def is_ready(self):
        return self.guardian is not None
