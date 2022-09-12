"""
Inheritance:

Inheritance is the mechanism of creating new classes from existing ones.

"""


class Parent:
    def __init__(self) -> None:
        print("parent class constructor called")


class Child(Parent):
    def __init__(self) -> None:
        print("Child class constructor called")
        # Parent.__init__(self)  # one way of calling parent class constructor
        super().__init__()  # recommended way of calling the parent class constructor


"""
c = Child()

output:
Child class constructor called
parent class constructor called

"""
c = Child()


class Person:
    def __init__(self, first_name, last_name) -> None:
        print("Person constructor called")
        self._first_name = first_name
        self._last_name = last_name

    def print_details(self):
        print(f'first_name: {self._first_name}, last_name: {self._last_name}')


class Student(Person):

    def __init__(self, first_name, last_name) -> None:
        super().__init__(first_name, last_name)

    def greet(self):
        print("Hello !")


# s1 = Student("Avi", "G")
# s1.greet()
# s1.print_details()

# s2 = Student("Sahit", "L")
# s2.print_details()

# s1._first_name = "asda"
# s1._last_name = "sdsd"
