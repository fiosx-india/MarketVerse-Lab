"""
MarketVerse Lab
scanner.py

Purpose:
Scan the project and collect health information.
"""

from pathlib import Path
import ast
from datetime import datetime


class ProjectScanner:

    def __init__(self, project_root="."):
        self.project_root = Path(project_root)

    def scan(self):
        report = {
            "total_files": 0,
            "python_files": 0,
            "empty_files": [],
            "syntax_errors": [],
            "scan_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        for file in self.project_root.rglob("*"):
            if not file.is_file():
                continue

            report["total_files"] += 1

            if file.suffix == ".py":
                report["python_files"] += 1

                try:
                    text = file.read_text(encoding="utf-8")

                    if not text.strip():
                        report["empty_files"].append(str(file))
                        continue

                    ast.parse(text)

                except SyntaxError as e:
                    report["syntax_errors"].append({
                        "file": str(file),
                        "line": e.lineno,
                        "message": e.msg
                    })

                except Exception:
                    pass

        return report
