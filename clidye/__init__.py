# -*- coding: utf-8 -*-
"""
clidye

"""
import datetime
import logging
from logging.handlers import RotatingFileHandler
# Our formatters
from . import formatters

__version__ = '0.0.1'

__all__ = ['formatters', 'handlers', 'utils']
__title__ = 'clidye'
__author__ = 'Gilbert Montague'
__description__ = 'Another Python Logging Module. Command line Dye. Pretty Print (and logging) for Python'
__email__ = 'gilbert.i.montague@gmail.com'
__license__ = 'MIT'
__copyright__ = 'Copyright 2018 Gilbert Montague'

# Available log formats
LOG_FMT ={
    'CSV': formatters.LOG_FMT_CSV,
    'DEFAULT': formatters.LOG_FMT_DEFAULT,
    'JSON': formatters.LOG_FMT_JSON
}

class Clidye(object):
    """Command line Dye. Pretty print for Python

    """
    def __init__(self, name, verbose=False, enable_logging=False, logging_file='/tmp/log.log', **kwargs):
        """A logger class that logs events

        Attributes:
            name (string): The logger instance name.

        Args:
            name (string): the logger instance name
            verbose (bool): should we print and log the debug information
            enable_logging (bool): should we enable logging?
            logging_file (string): where to dump this log
        """

        self.name = name
        self.verbose = verbose
        self.logging_file = logging_file
        self.enable_logging = enable_logging
        
        self.log_fmt = kwargs.get('log_fmt')

        if self.log_fmt is None:
            self.log_fmt = formatters.LOG_FMT_DEFAULT
        elif self.log_fmt in LOG_FMT:
            self.log_fmt = LOG_FMT[self.log_fmt]

        self.log_level = kwargs.get('log_level')
        if self.log_level is None:
            self.log_level = logging.INFO
        
        self.max_log_file_size = kwargs.get('max_file_size')
        if self.max_log_file_size is None:
            self.max_log_file_size = formatters.MAX_LOG_FILE_SIZE_BYTES
        
        self.backup_count = kwargs.get('backup_count')
        if self.backup_count is None:
            self.backup_count = formatters.DEFAULT_BACKUP_COUNT
        
        if self.enable_logging:
            self.init_logging()
        
        
            
        
    def init_logging(self):
        self.logger = logging.getLogger(self.name)
        self.logging_handler = RotatingFileHandler(self.logging_file, maxBytes=self.max_log_file_size, backupCount=self.backup_count)
        self.logging_formatter = logging.Formatter(self.log_fmt)
        self.logging_handler.setFormatter(self.logging_formatter)
        self.logger.addHandler(self.logging_handler)
        self.logger.setLevel(self.log_level)

        self.info("Logging to file enabled. Logging to {}".format(self.logging_file))

    def get_current_fmt_time(self):
        """
            Returns the current system time
            @rtype: string
            @return: The current time, formatted
        """
        return str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]) + formatters.CC_ENDC

    def fmt_name(self):
        """
            Returns the name of this logger, formatted for maximum pretty print
        """
        return formatters.CC_BOLD + self.name + formatters.CC_ENDC
    def enable_verbose(self):
        self.info("Enabling console debug messages")
        self.verbose = True

    def disable_verbose(self):
        self.info("Disabling console debug messages")
        self.verbose = False

    def info(self,message=""):
        """
            Prints an info message to console

            Args:
                message (str): The message to be printed
        """
        print("[%s][%-20s][%-20s] %s" % (self.get_current_fmt_time(), self.fmt_name(), formatters.INFO_MSG, str(message)))
        if self.enable_logging:
            self.logger.info(message)

    def debug(self,message=""):
        """
            Prints a debug message to console

            Args:
                message (str): The message to be printed
        """
        if self.verbose:
            print("[%s][%-20s][%-20s] %s" % (self.get_current_fmt_time(), self.fmt_name(), formatters.DEBUG, str(message)))

    def warning(self,message=""):
        """
            Prints a Warning message to console

            Args:
                message (str): The message to be printed
        """
        print("[%s][%-20s][%-20s] %s" % (self.get_current_fmt_time(), self.fmt_name(), formatters.WARNING, str(message)))
        if self.enable_logging:
            self.logger.warning(message)

    def fatal(self,message=""):
        """
            Prints a fatal message to console

            Args:
                message (str): The message to be printed
        """
        print("[%s][%-20s][%-20s] %s" % (self.get_current_fmt_time(), self.fmt_name(), formatters.FATAL_ERROR, str(message)))
        if self.enable_logging:
            self.logger.error(message)