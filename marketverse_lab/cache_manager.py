"""
MarketVerse Lab
cache_manager.py

Purpose:
Cache Manager for GuardianCore.
"""


class CacheManager:

    def __init__(self):
        self.guardian = None
        self.cache = {}

    def connect_guardian(self, guardian):
        self.guardian = guardian

    def set(self, key, value):
        self.cache[key] = value

        return {
            "status": "SUCCESS",
            "key": key,
            "value": value
        }

    def get(self, key):
        return self.cache.get(key)

    def remove(self, key):
        if key in self.cache:
            value = self.cache.pop(key)

            return {
                "status": "SUCCESS",
                "key": key,
                "value": value
            }

        return {
            "status": "NOT_FOUND",
            "key": key
        }

    def clear(self):
        cleared_items = len(self.cache)
        self.cache.clear()

        return {
            "status": "SUCCESS",
            "cleared_items": cleared_items
        }

    def report(self):
        return {
            "connected": self.guardian is not None,
            "ready": self.is_ready(),
            "total_items": len(self.cache),
            "cache": dict(self.cache)
        }

    def is_ready(self):
        return self.guardian is not None
