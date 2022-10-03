from decimal import DivisionByZero

"""
try -> critical operation which can raise an exception is placed inside try
expect -> The code that handles the exception is written in the expect block
finally -> this the block which always be executed during the normal flow and the error flow.

Try statement must have at least one except or finally clause

Exception is the base class, from which all the other sub exceptions were implemented.

So the base class Exception statement should be end in other words all the 
sub class exceptions like ZeroDivisionError should be handled before.


lets say we have functions C calling B and function B calling A
- If the exception occurred in A -> it it handled in A, expect block in A will be called. else it looks for the handing other functions, if not code will in function C
"""


def division(number, divider):
    try:
        return number/divider
    except ZeroDivisionError as ex:
        print("DivisionByZero occurred, Divider can not be Zero")
        print(ex)
    except Exception as ex:
        print("Some exception occurred while performing division")
        print(ex)
    finally:
        print("Finally executed")


# r = division(10, 2)
# print(r)


def abc(randomList):
    for entry in randomList:
        try:
            print(f"Current entry is: {entry}")
            result = 1/(entry)
            print(f"result value: {result}")
        except (TypeError) as ex:
            print(f"TypeError unsupported operand type: {ex}")
        except ZeroDivisionError as ex:
            print(f"DivisionByZero occurred, Divider can not be Zero: {ex}")
        except Exception as ex:
            print(f"Exception occurred: {ex}")
        finally:
            print("Finally block executed")
    print("For loop end")


# abc(["A", 2, 3, 0, 1])

# Custom exception
class SalaryNotInRange(Exception):
    def __init__(self, salary: int, msg="Salary should be in range of 1000 to 5000") -> None:
        self.salary = salary
        self.message = msg
        super().__init__(self.message)


def evaluate_salary(salary):
    if salary > 5000:
        raise SalaryNotInRange(salary)
    else:
        print(f"Given salary: {salary}")


def new_func(salary):
    try:
        evaluate_salary(salary=salary)
    except SalaryNotInRange as ex:
        print(f"SalaryNotInRange exception occurred: {ex}")


salary = int(input("Enter salary"))
new_func(salary)
