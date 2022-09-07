"""
Functions:

Why do we need functions?
- A function is a group of related statements to perform a specific task.
- Functions helps to break our program into smaller and modular chunks.

"""
# Importing a module
import util

# Giving alias name to a imported module
import util as my_util

# importing using from
from util import is_even_number

# importing all the functions in the util
from util import *

# Giving alias name to a imported function
from util import is_even_number as is_even

# Function syntax


def function_name(parameters):
    """ doc string """
    # statements


# No return statement


def print_even_odd_count(numbers):
    """
    This function calculates the even numbers and odd numbers from a given collection
    """
    # numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    even_count = 0
    odd_count = 0
    for i in numbers:
        if is_even(i):
            even_count += 1
        else:
            odd_count = odd_count + 1
    return {
        "even_count": even_count,
        "odd_count": odd_count
    }
    # return [even_count, odd_count] # return a list/ array
    # print("Number of even numbers " + str(even_count))
    # print("Number of odd numbers " + str(odd_count))


# Function calling

result = print_even_odd_count((1, 2, 3, 4, 5, 6, 7, 8, 9))
print(result)
# if the result is of array/list
# print("Number of even numbers " + str(result[0]))
# print("Number of odd numbers " + str(result[1]))


# if the result is of dict
print("Number of even numbers " + str(result["even_count"]))
print("Number of odd numbers " + str(result["odd_count"]))

# print_even_odd_count((11, 12, 33, 45, 55, 65, 74, 84, 49))

# x = is_even_number(20)
# print(x)


"""
# Lambda function -> in python we called this as anonymous function
what is anonymous functions? -> A function is defined with out a name.

Normal function:
def function_name()

Lambda functions syntax:
-----------------------
lambda arguments: expression (one line)

# Function
is_odd = lambda num: num % 2 == 0
"""
# is_odd = lambda num: num % 2 == 0
# is_odd(5)

numbers = [1, 5, 4, 6, 15, 23, 86, 10, 12]
# new_list = list(filter(lambda x: (x % 2 == 0), numbers))

# new_list = list(filter(is_odd, numbers))


# print(new_list)


def multiply_by_two(nums):
    new_nums = []
    for i in nums:
        new_nums.append(i*2)
    return new_nums


r = multiply_by_two(numbers)
print(r)

r2 = list(map(lambda x: x*2, numbers))
print(r2)
