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

from .controller import GuardianController

self.import_checker = ImportChecker()
self.file_analyzer = FileAnalyzer()
self.placement_analyzer = PlacementAnalyzer()

def run_guardian():
    guardian = GuardianController()
    return guardian.run()
    
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
]

__version__ = "2.0.0"
