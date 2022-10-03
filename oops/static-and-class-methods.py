
class Employee:
    NO_OF_EMPLOYEES = 0

    def __init__(self, first_name, last_name, salary) -> None:
        self.emp_id = Employee.NO_OF_EMPLOYEES + 1
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    @classmethod
    def init_via_full_name(cls, full_name: str, salary):
        full_name_split = full_name.split(",")
        return cls(full_name_split[0], full_name_split[1], salary)

    @staticmethod
    def increment_emp_id():
        Employee.NO_OF_EMPLOYEES + 1

    def print_details(self):
        print(
            f"First name: {self.first_name}, last_name: {self.last_name}, salary: {self.salary}")


e = Employee("ABC", "XYZ", 500)
e.print_details()


e2 = Employee.init_via_full_name("Jhon,Biden", 6000)
e2.print_details()
