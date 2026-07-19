"""
MarketVerse Lab
notification_manager.py

Purpose:
Manage Guardian notifications.
"""

from datetime import datetime


class NotificationManager:

    def __init__(self):
        self.guardian = None
        self.notifications = []

    def connect_guardian(self, guardian):
        self.guardian = guardian

    def notify(self, title, message, level="INFO"):

        item = {
            "time": datetime.now().isoformat(),
            "title": title,
            "message": message,
            "level": level
        }

        self.notifications.append(item)

        return item

    def history(self):
        return self.notifications

    def clear(self):
        self.notifications.clear()

        return {
            "status": "SUCCESS"
        }

    def report(self):

        return {
            "connected": self.guardian is not None,
            "total_notifications": len(self.notifications),
            "last_notification":
                self.notifications[-1]
                if self.notifications else None
        }

    def is_ready(self):
        return self.guardian is not None
