"""
MarketVerse Lab
config_manager.py

Purpose:
Configuration Manager for GuardianCore.

Responsibilities:
- Store configuration values.
- Update configurations.
- Remove configurations.
- Maintain configuration history.
- Generate configuration reports.
"""

from datetime import datetime


class ConfigManager:

    def __init__(self):
        self.guardian = None
        self.configs = {}
        self.history = []

    # ----------------------------------------
    # Connect Guardian
    # ----------------------------------------

    def connect_guardian(self, guardian):
        self.guardian = guardian

    # ----------------------------------------
    # Set Configuration
    # ----------------------------------------

    def set(self, key, value):

        self.configs[key] = value

        self.history.append({
            "action": "SET",
            "key": key,
            "value": value,
            "timestamp": datetime.now().isoformat()
        })

        return {
            "status": "SUCCESS",
            "key": key,
            "value": value
        }

    # ----------------------------------------
    # Get Configuration
    # ----------------------------------------

    def get(self, key):
        return self.configs.get(key)

    # ----------------------------------------
    # Remove Configuration
    # ----------------------------------------

    def remove(self, key):

        if key not in self.configs:
            return {
                "status": "FAILED",
                "message": "Configuration not found."
            }

        value = self.configs.pop(key)

        self.history.append({
            "action": "REMOVE",
            "key": key,
            "value": value,
            "timestamp": datetime.now().isoformat()
        })

        return {
            "status": "SUCCESS",
            "key": key
        }

    # ----------------------------------------
    # Configuration Exists
    # ----------------------------------------

    def exists(self, key):
        return key in self.configs

    # ----------------------------------------
    # Total Configurations
    # ----------------------------------------

    def total_configs(self):
        return len(self.configs)

    # ----------------------------------------
    # Last Change
    # ----------------------------------------

    def last_change(self):

        if not self.history:
            return None

        return self.history[-1]

    # ----------------------------------------
    # Configuration History
    # ----------------------------------------

    def config_history(self):
        return list(self.history)

    # ----------------------------------------
    # Clear Configurations
    # ----------------------------------------

    def clear(self):

        self.configs.clear()
        self.history.clear()

        return {
            "status": "SUCCESS",
            "message": "All configurations cleared."
        }

    # ----------------------------------------
    # Report
    # ----------------------------------------

    def report(self):

        return {
            "connected": self.guardian is not None,
            "ready": self.is_ready(),
            "total_configs": self.total_configs(),
            "configs": dict(self.configs),
            "last_change": self.last_change(),
            "history": self.config_history()
        }

    # ----------------------------------------
    # Ready Check
    # ----------------------------------------

    def is_ready(self):
        return self.guardian is not None
