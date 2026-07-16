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
