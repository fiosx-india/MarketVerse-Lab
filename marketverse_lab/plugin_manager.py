"""
MarketVerse Lab
plugin_manager.py

Purpose:
Plugin Manager for GuardianCore.

Responsibilities:
- Load plugins.
- Unload plugins.
- Maintain plugin history.
- Generate plugin reports.
"""

from datetime import datetime


class PluginManager:

    def __init__(self):
        self.guardian = None
        self.loaded_plugins = []
        self.history = []

    # ----------------------------------------
    # Connect Guardian
    # ----------------------------------------

    def connect_guardian(self, guardian):
        self.guardian = guardian

    # ----------------------------------------
    # Load Plugin
    # ----------------------------------------

    def load(self, name):

        if not name:
            return {
                "status": "FAILED",
                "message": "Plugin name required."
            }

        if name not in self.loaded_plugins:
            self.loaded_plugins.append(name)

            self.history.append({
                "action": "LOAD",
                "plugin": name,
                "timestamp": datetime.now().isoformat()
            })

        return {
            "status": "SUCCESS",
            "plugin": name
        }

    # ----------------------------------------
    # Unload Plugin
    # ----------------------------------------

    def unload(self, name):

        if name in self.loaded_plugins:

            self.loaded_plugins.remove(name)

            self.history.append({
                "action": "UNLOAD",
                "plugin": name,
                "timestamp": datetime.now().isoformat()
            })

            return {
                "status": "SUCCESS",
                "plugin": name
            }

        return {
            "status": "FAILED",
            "message": "Plugin not loaded."
        }

    # ----------------------------------------
    # Plugin List
    # ----------------------------------------

    def plugins(self):
        return list(self.loaded_plugins)

    # ----------------------------------------
    # Last Action
    # ----------------------------------------

    def last_action(self):

        if not self.history:
            return None

        return self.history[-1]

    # ----------------------------------------
    # Total Plugins
    # ----------------------------------------

    def total_plugins(self):
        return len(self.loaded_plugins)

    # ----------------------------------------
    # History
    # ----------------------------------------

    def plugin_history(self):
        return list(self.history)

    # ----------------------------------------
    # Clear Plugins
    # ----------------------------------------

    def clear(self):

        self.loaded_plugins.clear()
        self.history.clear()

        return {
            "status": "SUCCESS",
            "message": "All plugins cleared."
        }

    # ----------------------------------------
    # Report
    # ----------------------------------------

    def report(self):

        return {
            "connected": self.guardian is not None,
            "ready": self.is_ready(),
            "total_plugins": self.total_plugins(),
            "plugins": self.plugins(),
            "last_action": self.last_action(),
            "history": self.plugin_history()
        }

    # ----------------------------------------
    # Ready Check
    # ----------------------------------------

    def is_ready(self):
        return self.guardian is not None
