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

        # -----------------------------
    # Storage Rules
    # -----------------------------
    MAX_REPORT_HISTORY = 20
    MAX_SCAN_RESULTS = 500
    MAX_LOG_SIZE_MB = 10
    MAX_CACHE_SIZE_MB = 50

    AUTO_DELETE_OLD_REPORTS = True
    AUTO_DELETE_TEMP = True
    AUTO_DELETE_CACHE = True

    # -----------------------------
    # Cache Rules
    # -----------------------------
    AUTO_CLEAR_CACHE = True
    AUTO_CLEAR_TEMP = True
    AUTO_CLEAR_PYCACHE = True
    AUTO_CLEAR_LOGS = True

    # -----------------------------
    # Report Rules
    # -----------------------------
    SHOW_INTERNAL_ERRORS = False
    SHOW_FILE_LIST = False
    SHOW_SCAN_DETAILS = False

    # -----------------------------
    # Network Rules
    # -----------------------------
    ALLOW_EXTERNAL_UPLOAD = False
    ALLOW_DEBUG_EXPORT = False
    ALLOW_FULL_REPORT_EXPORT = False
    ALLOW_INTERNAL_REPORTS = False

    # -----------------------------
    # File Protection Rules
    # -----------------------------
    ALLOW_DELETE_SOURCE = False
    ALLOW_MOVE_SOURCE = False
    ALLOW_RENAME_SOURCE = False
    ALLOW_PATCH_SOURCE = True

    # -----------------------------
    # Scan Limits
    # -----------------------------
    SCAN_ONLY_REGISTERED = True
    SCAN_MAX_FILES = 1000
    SCAN_TIMEOUT_SECONDS = 30
    SKIP_BINARY_FILES = True

    # -----------------------------
    # Cleanup Rules
    # -----------------------------
    AUTO_REMOVE_BAK = True
    AUTO_REMOVE_TMP = True
    AUTO_REMOVE_PYC = True
    AUTO_REMOVE_EMPTY_DIRS = True

    def is_allowed_file(self, path):
        return Path(path).suffix.lower() in self.ALLOWED_EXTENSIONS

    def is_ignored_folder(self, folder):
        return folder in self.IGNORE_FOLDERS

    def is_ignored_file(self, filename):
        return filename in self.IGNORE_FILES

    def report(self):
        return {
            "max_report_history": self.MAX_REPORT_HISTORY,
            "max_scan_results": self.MAX_SCAN_RESULTS,
            "max_cache_size_mb": self.MAX_CACHE_SIZE_MB,
            "auto_delete_cache": self.AUTO_DELETE_CACHE,
            "auto_clear_cache": self.AUTO_CLEAR_CACHE,
            "scan_only_registered": self.SCAN_ONLY_REGISTERED,
            "scan_max_files": self.SCAN_MAX_FILES,
            "allow_external_upload": self.ALLOW_EXTERNAL_UPLOAD,
            
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
