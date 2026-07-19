"""
MarketVerse Lab
diagnostics_manager.py

Purpose:
Run diagnostics on Guardian modules.
"""


class DiagnosticsManager:

    def __init__(self):
        self.guardian = None

    def connect_guardian(self, guardian):
        self.guardian = guardian

    def run(self):

        if self.guardian is None:
            return {
                "status": "Guardian Not Connected"
            }

        report = {}

        modules = [
            ("Audit Manager", self.guardian.audit_manager),
            ("State Manager", self.guardian.state_manager),
            ("Session Manager", self.guardian.session_manager),
            ("Snapshot Manager", self.guardian.snapshot_manager),
            ("Recovery Manager", self.guardian.recovery_manager),
            ("Version Manager", self.guardian.version_manager),
            ("Backup Manager", self.guardian.backup_manager),
            ("Rollback Manager", self.guardian.rollback_manager)
        ]

        for name, module in modules:

            try:

                if hasattr(module, "is_ready"):
                    status = module.is_ready()
                else:
                    status = False

                report[name] = {
                    "status": "PASS" if status else "FAIL"
                }

            except Exception as e:

                report[name] = {
                    "status": "ERROR",
                    "message": str(e)
                }

        return report

    def report(self):

        diagnostics = self.run()

        passed = sum(
            1 for item in diagnostics.values()
            if item["status"] == "PASS"
        )

        failed = len(diagnostics) - passed

        return {
            "connected": self.guardian is not None,
            "modules": len(diagnostics),
            "passed": passed,
            "failed": failed,
            "diagnostics": diagnostics
        }

    def is_ready(self):
        return self.guardian is not None
