"""
MarketVerse Lab
command_center.py

Purpose:
Command Center for GuardianCore.

Responsibilities:
- Execute commands.
- Maintain command history.
- Generate execution reports.
"""

from datetime import datetime


class CommandCenter:

    def __init__(self):
        self.guardian = None
        self.history = []

    # ----------------------------------------
    # Connect Guardian
    # ----------------------------------------

    def connect_guardian(self, guardian):
        self.guardian = guardian

    # ----------------------------------------
    # Execute Command
    # ----------------------------------------

    def execute(self, command):

        result = {
            "status": "SUCCESS",
            "command": command,
            "message": f"Command '{command}' executed.",
            "timestamp": datetime.now().isoformat()
        }

        self.history.append(result)

        return result

    # ----------------------------------------
    # Command History
    # ----------------------------------------

    def command_history(self):
        return list(self.history)

    # ----------------------------------------
    # Last Command
    # ----------------------------------------

    def last_command(self):

        if not self.history:
            return None

        return self.history[-1]

    # ----------------------------------------
    # Total Commands
    # ----------------------------------------

    def total_commands(self):
        return len(self.history)

    # ----------------------------------------
    # Statistics
    # ----------------------------------------

    def statistics(self):

        return {
            "total_commands": self.total_commands()
        }

    # ----------------------------------------
    # Clear History
    # ----------------------------------------

    def clear_history(self):

        self.history.clear()

        return {
            "status": "SUCCESS",
            "message": "Command history cleared."
        }

    # ----------------------------------------
    # Report
    # ----------------------------------------

    def report(self):

        return {
            "connected": self.guardian is not None,
            "ready": self.is_ready(),
            "statistics": self.statistics(),
            "last_command": self.last_command(),
            "history": self.command_history()
        }

    # ----------------------------------------
    # Ready Check
    # ----------------------------------------

    def is_ready(self):
        return self.guardian is not None
