"""
MarketVerse Guardian
placement_analyzer.py

Purpose:
Suggest the correct location for a Python file
inside the MarketVerse project.
"""

from pathlib import Path


class PlacementAnalyzer:

    def __init__(self):

        self.rules = {
            "guardian": "Guardian/",
            "monitor": "Guardian/integrations/",
            "integration": "Guardian/integrations/",
            "core": "core/",
            "module": "modules/",
            "strategy": "modules/",
            "indicator": "modules/",
        }

    def analyze(self, file_path):

        file_path = Path(file_path)

        result = {
            "file": file_path.name,
            "current_location": str(file_path.parent),
            "recommended_location": None,
            "status": "OK",
            "reason": ""
        }

        name = file_path.name.lower()

        for keyword, folder in self.rules.items():

            if keyword in name:

                result["recommended_location"] = folder

                current = str(file_path.parent).replace("\\", "/")

                expected = folder.rstrip("/")

                if not current.endswith(expected):

                    result["status"] = "MOVE"

                    result["reason"] = (
                        f"Move '{file_path.name}' "
                        f"to '{folder}'"
                    )

                return result

        result["recommended_location"] = "Unknown"

        result["status"] = "REVIEW"

        result["reason"] = (
            "No placement rule found. "
            "Manual review required."
        )

        return result
