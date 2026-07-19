"""
MarketVerse Lab
plugin_manager.py

Purpose:
Plugin Manager for GuardianCore.
"""

class PluginManager:

    def __init__(self):
        self.guardian = None

    def connect_guardian(self, guardian):
        self.guardian = guardian

    def report(self):
        return {
            "connected": self.guardian is not None
        }

    def is_ready(self):
        return self.guardian is not None
