"""
MarketVerse Lab
event_bus.py

Purpose:
Central Event Bus for GuardianCore.
"""

class EventBus:

    def __init__(self):
        self.guardian = None
        self.events = []

    def connect_guardian(self, guardian):
        self.guardian = guardian

    def publish(self, name, data=None):
        event = {
            "name": name,
            "data": data
        }

        self.events.append(event)

        return {
            "status": "SUCCESS",
            "event": event
        }

    def history(self):
        return list(self.events)

    def report(self):
        return {
            "connected": self.guardian is not None,
            "total_events": len(self.events),
            "events": self.events
        }

    def is_ready(self):
        return self.guardian is not None
