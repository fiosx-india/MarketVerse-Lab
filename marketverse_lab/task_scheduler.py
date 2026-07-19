"""
MarketVerse Lab
task_scheduler.py

Purpose:
Schedules and manages Guardian tasks.
"""

from collections import deque


class TaskScheduler:

    def __init__(self):
        self.guardian = None
        self.tasks = deque()

    def connect_guardian(self, guardian):
        self.guardian = guardian

    def add_task(self, name, data=None):
        self.tasks.append({
            "name": name,
            "data": data
        })

        return {
            "status": "SUCCESS",
            "task": name
        }

    def next_task(self):
        if not self.tasks:
            return None

        return self.tasks[0]

    def run_next(self):
        if not self.tasks:
            return {
                "status": "EMPTY"
            }

        task = self.tasks.popleft()

        return {
            "status": "SUCCESS",
            "task": task
        }

    def pending_tasks(self):
        return list(self.tasks)

    def clear_tasks(self):
        self.tasks.clear()

        return {
            "status": "CLEARED"
        }

    def report(self):
        return {
            "ready": self.is_ready(),
            "pending": len(self.tasks),
            "tasks": self.pending_tasks()
        }

    def is_ready(self):
        return self.guardian is not None
