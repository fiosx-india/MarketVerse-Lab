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


class ReportGenerator:

    def __init__(self):
        self.guardian = None
        self.history = []

    def connect_guardian(self, guardian):
        self.guardian = guardian

    def generate(self, report_name="Guardian Report", data=None):

        report = {
            "status": "SUCCESS",
            "report": report_name,
            "data": data,
            "message": f"'{report_name}' generated successfully."
        }

        self.history.append(report)

        return report

    def report_history(self):
        return list(self.history)

    def last_report(self):
        if not self.history:
            return None
        return self.history[-1]

    def total_reports(self):
        return len(self.history)

    def clear_history(self):
        self.history.clear()

        return {
            "status": "SUCCESS",
            "message": "Report history cleared."
        }

    def report(self):
        return {
            "connected": self.guardian is not None,
            "ready": self.is_ready(),
            "total_reports": self.total_reports(),
            "last_report": self.last_report(),
            "history": self.report_history()
        }

    def is_ready(self):
        return self.guardian is not None
