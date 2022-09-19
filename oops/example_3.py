from logger_util import MyLogger as logger
from logger_util import LogLevel


class Employee:
    def __init__(self, name) -> None:
        self.name = name

    def print_details(self):
        msg = f'Name: {self.name}'
        logger.log_info(msg)


class Department:
    def __init__(self, name) -> None:
        self.name = name

    def print_details(self):
        msg = f'Department name: {self.name}'
        logger.log(LogLevel.Warning, msg)


# e = Employee("ADC")
# e.print_details()

d = Department("CSE")
d.print_details()
