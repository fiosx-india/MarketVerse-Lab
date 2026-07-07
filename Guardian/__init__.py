"""
MarketVerse Guardian

Guardian package initializer.
"""

from .scanner import ProjectScanner
from .validator import ProjectValidator
from .dependency import DependencyAnalyzer
from .health import HealthMonitor
from .advisor import GuardianAdvisor
from .import_checker import ImportChecker
from .notifier import Notifier
from .registry import ProjectRegistry, ModuleInfo
from .registry_sync import RegistrySync
from .file_analyzer import FileAnalyzer
from .placement_analyzer import PlacementAnalyzer
from .auto_fixer import AutoFixer
from .self_healing import SelfHealing
from .controller import GuardianController


def run_guardian(root="."):
    guardian = GuardianController()
    return guardian.run(root)


__all__ = [
    "GuardianController",
    "run_guardian",
    "ProjectScanner",
    "ProjectValidator",
    "DependencyAnalyzer",
    "HealthMonitor",
    "GuardianAdvisor",
    "ImportChecker",
    "Notifier",
    "ProjectRegistry",
    "ModuleInfo",
    "RegistrySync",
    "FileAnalyzer",
    "PlacementAnalyzer",
    "AutoFixer",
    "SelfHealing",
]

__version__ = "2.2.0"
