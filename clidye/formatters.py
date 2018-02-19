# -*- coding: utf-8 -*-
"""
Useful formatters for clidye
"""

# Console Colors (CC) Constants
CC_HEADER = '\033[95m'
CC_OKBLUE = '\033[94m'
CC_OKGREEN = '\033[92m'
CC_WARNING = '\033[93m'
CC_FAIL = '\033[91m'
CC_ENDC = '\033[0m'
CC_BOLD = '\033[1m'
CC_UNDERLINE = '\033[4m'

# Full macros for colorful lines
INFO_MSG = CC_OKGREEN + CC_BOLD + "INFO" + CC_ENDC
DEBUG = CC_OKBLUE + CC_BOLD + "DEBUG" + CC_ENDC
WARNING = CC_WARNING + CC_BOLD + "WARNING" + CC_ENDC
FATAL_ERROR = CC_FAIL + CC_BOLD + "FATAL" + CC_ENDC

# MAX Rotating Log File Size
MAX_LOG_FILE_SIZE_BYTES = 2000
DEFAULT_BACKUP_COUNT = 5

# LOG FMTs
LOG_FMT_CSV = '%(asctime)s.%(msecs)d,%(name)s,%(levelname)s,"%(message)s"'
LOG_FMT_DEFAULT = '%(asctime)s.%(msecs)-3d %(name)-12s %(levelname)-8s %(message)s'
LOG_FMT_JSON = (
    '{"time": "%(asctime)s.%(msecs)d", "name": "%(name)s", "level":'
    ' "%(levelname)s", "message": "%(message)s"}')
