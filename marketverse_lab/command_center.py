"""
MarketVerse Lab
command_center.py

Purpose:
Command Center for GuardianCore.
"""


class CommandCenter:

    def __init__(self):
        self.guardian = None
        self.history = []

    def connect_guardian(self, guardian):
        self.guardian = guardian

    def execute(self, command):

        result = {
            "status": "SUCCESS",
            "command": command,
            "message": f"Command '{command}' executed."
        }

        self.history.append(result)

        return result

    def command_history(self):
        return list(self.history)

    def last_command(self):
        if not self.history:
            return None
        return self.history[-1]

    def total_commands(self):
        return len(self.history)

    def clear_history(self):
        self.history.clear()

        return {
            "status": "SUCCESS",
            "message": "Command history cleared."
        }

    def report(self):
        return {
            "connected": self.guardian is not None,
            "ready": self.is_ready(),
            "total_commands": self.total_commands(),
            "last_command": self.last_command(),
            "history": self.command_history()
        }

    def is_ready(self):
        return self.guardian is not None
