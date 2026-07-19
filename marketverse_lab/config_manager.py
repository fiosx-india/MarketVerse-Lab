"""
MarketVerse Lab
config_manager.py

Purpose:
Configuration Manager for GuardianCore.
"""

class ConfigManager:

    def __init__(self):
        self.guardian = None
        self.configs = {}

    def connect_guardian(self, guardian):
        self.guardian = guardian

    def set(self, key, value):
        self.configs[key] = value

        return {
            "status": "SUCCESS",
            "key": key,
            "value": value
        }

    def get(self, key):
        return self.configs.get(key)

    def report(self):
        return {
            "connected": self.guardian is not None,
            "total_configs": len(self.configs),
            "configs": self.configs
        }

    def is_ready(self):
        return self.guardian is not None
