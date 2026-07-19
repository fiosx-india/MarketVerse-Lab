"""
MarketVerse Lab
report_generator.py

Purpose:
Report Generator for GuardianCore.

Responsibilities:
- Generate Guardian reports.
- Store generated report history.
- Provide report statistics.
- Connect with GuardianCore.
"""

from datetime import datetime


class ReportGenerator:

    def __init__(self):

        self.guardian = None
        self.history = []

    # ----------------------------------------
    # Connect Guardian
    # ----------------------------------------

    def connect_guardian(self, guardian):

        self.guardian = guardian

    # ----------------------------------------
    # Generate Report
    # ----------------------------------------

    def generate(
        self,
        report_name="Guardian Report",
        data=None
    ):

        report = {
            "status": "SUCCESS",
            "report": report_name,
            "data": data,
            "created_at": datetime.now().isoformat(),
            "message": f"'{report_name}' generated successfully."
        }

        self.history.append(report)

        return report

    # ----------------------------------------
    # Report History
    # ----------------------------------------

    def report_history(self):

        return list(self.history)

    # ----------------------------------------
    # Last Report
    # ----------------------------------------

    def last_report(self):

        if not self.history:
            return None

        return self.history[-1]

    # ----------------------------------------
    # Total Reports
    # ----------------------------------------

    def total_reports(self):

        return len(self.history)

    # ----------------------------------------
    # Statistics
    # ----------------------------------------

    def statistics(self):

        return {
            "total_reports": self.total_reports(),
            "connected": self.guardian is not None
        }

    # ----------------------------------------
    # Clear History
    # ----------------------------------------

    def clear_history(self):

        self.history.clear()

        return {
            "status": "SUCCESS",
            "message": "Report history cleared."
        }

    # ----------------------------------------
    # Reset
    # ----------------------------------------

    def reset(self):

        return self.clear_history()

    # ----------------------------------------
    # Report
    # ----------------------------------------

    def report(self):

        return {
            "connected": self.guardian is not None,
            "ready": self.is_ready(),
            "statistics": self.statistics(),
            "last_report": self.last_report(),
            "history": self.report_history()
        }

    # ----------------------------------------
    # Ready Check
    # ----------------------------------------

    def is_ready(self):

        return self.guardian is not None

    # ----------------------------------------
    # String Representation
    # ----------------------------------------

    def __str__(self):

        return (
            f"ReportGenerator("
            f"reports={self.total_reports()})"
        )

    __repr__ = __str__
