"""
MarketVerse Lab
plugin_manager.py

Purpose:
Plugin Manager for GuardianCore.
"""


class PluginManager:

    def __init__(self):
        self.guardian = None
        self.loaded_plugins = []

    def connect_guardian(self, guardian):
        self.guardian = guardian

    def load(self, name):
        if name and name not in self.loaded_plugins:
            self.loaded_plugins.append(name)

        return {
            "status": "SUCCESS",
            "plugin": name
        }

    def plugins(self):
        return list(self.loaded_plugins)

    def report(self):
        return {
            "connected": self.guardian is not None,
            "total_plugins": len(self.loaded_plugins),
            "plugins": list(self.loaded_plugins)
        }

    def is_ready(self):
        return self.guardian is not None
