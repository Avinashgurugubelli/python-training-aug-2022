
from enum import Enum


class LogLevel(Enum):
    INFO = 0
    DEBUG = 1
    Warning = 2


class MyLogger:

    @staticmethod
    def log_info(message):
        print(f'Info: {message}')

    @staticmethod
    def log_debug(message):
        print(f'Debug: {message}')

    @staticmethod
    def log_warning(message):
        print(f'Warning: {message}')

    @staticmethod
    def log(severity, message):
        if severity == LogLevel.INFO:
            MyLogger.log_info(message)

        if severity == LogLevel.Warning:
            MyLogger.log_warning(message)

        if severity == LogLevel.DEBUG:
            MyLogger.log_debug(message)
