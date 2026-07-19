"""
MarketVerse Lab
event_bus.py

Purpose:
Central Event Bus for GuardianCore.
"""

from datetime import datetime


class EventBus:

    def __init__(self):
        self.guardian = None
        self.events = []

    # ----------------------------------------
    # Connect Guardian
    # ----------------------------------------

    def connect_guardian(self, guardian):
        self.guardian = guardian

    # ----------------------------------------
    # Publish Event
    # ----------------------------------------

    def publish(self, name, data=None):

        event = {
            "name": name,
            "data": data,
            "timestamp": datetime.now().isoformat()
        }

        self.events.append(event)

        return {
            "status": "SUCCESS",
            "event": event
        }

    # ----------------------------------------
    # Event History
    # ----------------------------------------

    def history(self):
        return list(self.events)

    # ----------------------------------------
    # Last Event
    # ----------------------------------------

    def last_event(self):

        if not self.events:
            return None

        return self.events[-1]

    # ----------------------------------------
    # Total Events
    # ----------------------------------------

    def total_events(self):
        return len(self.events)

    # ----------------------------------------
    # Find Events
    # ----------------------------------------

    def find(self, name):

        return [
            event
            for event in self.events
            if event["name"] == name
        ]

    # ----------------------------------------
    # Clear History
    # ----------------------------------------

    def clear(self):

        self.events.clear()

        return {
            "status": "SUCCESS",
            "message": "Event history cleared."
        }

    # ----------------------------------------
    # Report
    # ----------------------------------------

    def report(self):

        return {
            "connected": self.guardian is not None,
            "ready": self.is_ready(),
            "total_events": self.total_events(),
            "last_event": self.last_event(),
            "events": self.history()
        }

    # ----------------------------------------
    # Ready Check
    # ----------------------------------------

    def is_ready(self):
        return self.guardian is not None
