"""
MarketVerse Lab
cache_manager.py

Purpose:
Cache Manager for GuardianCore.

Responsibilities:
- Store cache values.
- Retrieve cache values.
- Remove cache entries.
- Track cache history.
- Generate cache reports.
"""

from datetime import datetime


class CacheManager:

    def __init__(self):
        self.guardian = None
        self.cache = {}
        self.history = []

    # ----------------------------------------
    # Connect Guardian
    # ----------------------------------------

    def connect_guardian(self, guardian):
        self.guardian = guardian

    # ----------------------------------------
    # Set Cache
    # ----------------------------------------

    def set(self, key, value):

        self.cache[key] = value

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
    # Get Cache
    # ----------------------------------------

    def get(self, key):
        return self.cache.get(key)

    # ----------------------------------------
    # Cache Exists
    # ----------------------------------------

    def exists(self, key):
        return key in self.cache

    # ----------------------------------------
    # Remove Cache
    # ----------------------------------------

    def remove(self, key):

        if key not in self.cache:
            return {
                "status": "NOT_FOUND",
                "key": key
            }

        value = self.cache.pop(key)

        self.history.append({
            "action": "REMOVE",
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
    # Total Cache Items
    # ----------------------------------------

    def total_items(self):
        return len(self.cache)

    # ----------------------------------------
    # Last Action
    # ----------------------------------------

    def last_action(self):

        if not self.history:
            return None

        return self.history[-1]

    # ----------------------------------------
    # Cache History
    # ----------------------------------------

    def cache_history(self):
        return list(self.history)

    # ----------------------------------------
    # Clear Cache
    # ----------------------------------------

    def clear(self):

        cleared_items = len(self.cache)

        self.cache.clear()
        self.history.clear()

        return {
            "status": "SUCCESS",
            "cleared_items": cleared_items,
            "message": "Cache cleared successfully."
        }

    # ----------------------------------------
    # Report
    # ----------------------------------------

    def report(self):

        return {
            "connected": self.guardian is not None,
            "ready": self.is_ready(),
            "total_items": self.total_items(),
            "cache": dict(self.cache),
            "last_action": self.last_action(),
            "history": self.cache_history()
        }

    # ----------------------------------------
    # Ready Check
    # ----------------------------------------

    def is_ready(self):
        return self.guardian is not None
