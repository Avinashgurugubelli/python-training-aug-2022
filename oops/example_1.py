from abc import ABC, abstractmethod


class Employee:
    # Constructor is a special type of function which is called automatically when we create an object
    # self: Self in python is used to represent the current instance of a class.
    # self should be the first parameter always for the functions inside a class
    # Here aadhar_number field is an optional parameter
    # Optional parameter rules: it should be always a last parameter for a given function, also it can have multiple

    def __init__(self, name, email_id=None, aadhar_number=None):
        # if no underscore is given -> by default it will consider as public
        self.phone_number = None
        self._name = name
        # Private attribute
        self.__salary = None
        self._email_id = email_id
        # Private attribute
        self.__aadhar_number = aadhar_number

    # methods names should be snake case, i.e each word should be separated by _
    def set_salary(self, salary):
        self.__salary = salary

    def print_details(self):
        print(
            f'Name: {self._name}, email: {self._email_id}, salary: {self.__salary}, aadhar_number: {self.__aadhar_number}')


# Creating an object
emp = Employee("Jack", "jack@gamil.com", 112233)
print("Employee name, accessing out side the class: "+emp._name)
print(emp.phone_number)
# This will throw an error -> because salary is a private attribute/filed of an employee
# print("Employee salary, accessing out side the class: "+emp.__salary)

# emp.print_details()
emp.set_salary(5000)
emp.print_details()

emp_2 = Employee("Martin", "Martin@gmail.com")
# emp_2.set_salary()
emp_2.print_details()
print(emp_2.phone_number)

'''
# passing name and aadhar_number only
# this is wrong: here 2nd parameter will map to emailID
emp_3 = Employee("Rose", 1265689)

1st way to achieve is passing empty value in the 2nd argument
i.e. emp_3 = Employee("Rose", "", 1265689) or emp_3 = Employee("Rose", None, 1265689)

Proper way is calling function using the named attributes, u can also change the order of arguments when u passing via named syntax
emp_3 = Employee(name="Rose", aadhar_number=1265689)

'''
emp_3 = Employee(name="Rose", aadhar_number=1265689)
emp_3.print_details()

# Encapsulation

'''
1. Encapsulation: this principal states that all important information is contained inside an object and only expose the necessary information.

Access modifier:
---------------
- private, public, protected

- Public: (in python it is denoted by single underscore '_' )
 - Value can be accessed inside a class and out the class using class object.
 - This can be specified to both attributes/fields, methods

- private (in python it is denoted by double underscore '__' )
    - Value can be accessed inside a class but not outside the class
    - This can be specified to both attributes/fields, methods
- protected: 
  - Value can be accessed inside a class and its children classes, but not outside the class
  - This can be specified to both attributes/fields, methods
'''

"""
2. Abstraction:

Abstraction is the process of hiding the internal details of an application from the outer world.

"""

# Abstract class
"""
Abstract class:
 An abstract class can be considered as a blue print of other classes. It allows you to create a set of methods that
 must be created with in the child classes built from the abstract class.

"""

"""
Normal class

class Car:
    def turn_on(self):
        pass


Abstract class:

class Car(ABC):
    @abstractmethod
    def turnOnCar(self):
        pass

- ABC is a in build python class -> it is inherited to  make an normal class a abstract class.
- You can not create a object to the abstract class.

What is the need of abstact class?
- it will act blue print of other classes
"""


class Car(ABC):
    @abstractmethod
    def turn_on_Car(self):
        pass

    @abstractmethod
    def turn_off_Car(self):
        pass

# car = Car()  # error: Can't instantiate abstract class

# Inheritance


class ManualCar(Car):
    def turn_on_Car(self):
        print("Manual car turn on")

    def turn_off_Car(self):
        print("Manual car turn off")


c = ManualCar()
c.turn_on_Car()
