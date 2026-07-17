"""
MarketVerse Lab
bootstrap.py

Purpose:
Initialize the complete
MarketVerse AI System.
"""

from .guardian_core import GuardianCore


class Bootstrap:

    def __init__(self):

        # Core Engine
        self.guardian = GuardianCore()

        # Service Modules
        self.monitor = self.guardian.live_monitor
        self.assistant = self.guardian.ai_assistant
        self.workflow = self.guardian.workflow_engine

    # ----------------------------------------
    # Start System
    # ----------------------------------------

    def start(self):

        return {
            "status": "READY",
            "guardian": self.guardian.is_ready(),
            "assistant": self.assistant.is_ready(),
            "workflow": self.workflow.is_ready(),
            "monitor": self.monitor.is_ready(),
        }

    # ----------------------------------------
    # Shutdown
    # ----------------------------------------

    def shutdown(self):

        self.monitor.reset()
        self.workflow.reset()

        return {
            "status": "STOPPED",
        }


# ----------------------------------------
# Bootstrap Function
# ----------------------------------------

def bootstrap_system():

    system = Bootstrap()
    system.start()

    return system
