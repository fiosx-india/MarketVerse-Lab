"""
MarketVerse Guardian Constitution

Purpose:
Global development rules for the Guardian.
"""


class GuardianConstitution:

    # Development Rules
    AUTO_CREATE_FILES = False
    AUTO_BACKUP = False
    AUTO_DUPLICATE = False
    AUTO_TEMP_FILES = False

    STOP_ON_ERROR = True
    ONE_TASK_AT_A_TIME = True
    PROJECT_LOCK_ON_ERROR = True
    ALLOW_ONLY_REGISTERED_FILES = True

    VERSION = "1.0"


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
        }

    def is_ready(self):
        return True
