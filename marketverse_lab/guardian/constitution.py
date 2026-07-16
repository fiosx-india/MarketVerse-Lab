"""
MarketVerse Guardian Constitution

Purpose:
Global development rules for the Guardian.
"""

from pathlib import Path


class GuardianConstitution:

    VERSION = "2.0"

    # -----------------------------
    # Development Rules
    # -----------------------------
    AUTO_CREATE_FILES = False
    AUTO_BACKUP = False
    AUTO_DUPLICATE = False
    AUTO_TEMP_FILES = False

    STOP_ON_ERROR = True
    ONE_TASK_AT_A_TIME = True
    PROJECT_LOCK_ON_ERROR = True
    ALLOW_ONLY_REGISTERED_FILES = True

    # -----------------------------
    # Scan Rules
    # -----------------------------
    MAX_SCAN_DEPTH = 25

    ALLOWED_EXTENSIONS = {
        ".py",
        ".json",
        ".yaml",
        ".yml",
        ".md",
        ".txt",
    }

    IGNORE_FOLDERS = {
        "__pycache__",
        ".git",
        ".venv",
        "venv",
        "node_modules",
        ".idea",
        ".vscode",
        ".pytest_cache",
        ".mypy_cache",
        "build",
        "dist",
    }

    IGNORE_FILES = {
        ".DS_Store",
        "Thumbs.db",
    }

    # -----------------------------
    # Security Rules
    # -----------------------------
    HIDE_INTERNAL_REPORTS = True
    SHOW_ONLY_SUMMARY = True
    KEEP_FULL_HISTORY = False

    # -----------------------------
    # Performance Rules
    # -----------------------------
    ENABLE_FAST_SCAN = True
    ENABLE_INCREMENTAL_SCAN = True

    def is_allowed_file(self, path):
        return Path(path).suffix.lower() in self.ALLOWED_EXTENSIONS

    def is_ignored_folder(self, folder):
        return folder in self.IGNORE_FOLDERS

    def is_ignored_file(self, filename):
        return filename in self.IGNORE_FILES

    def report(self):
        return {
            "version": self.VERSION,
            "auto_create_files": self.AUTO_CREATE_FILES,
            "auto_backup": self.AUTO_BACKUP,
            "auto_duplicate": self.AUTO_DUPLICATE,
            "auto_temp_files": self.AUTO_TEMP_FILES,
            "stop_on_error": self.STOP_ON_ERROR,
            "one_task_at_a_time": self.ONE_TASK_AT_A_TIME,
            "project_lock_on_error": self.PROJECT_LOCK_ON_ERROR,
            "allow_only_registered_files": self.ALLOW_ONLY_REGISTERED_FILES,
            "fast_scan": self.ENABLE_FAST_SCAN,
            "incremental_scan": self.ENABLE_INCREMENTAL_SCAN,
            "show_only_summary": self.SHOW_ONLY_SUMMARY,
            "hide_internal_reports": self.HIDE_INTERNAL_REPORTS,
        }

    def is_ready(self):
        return True
