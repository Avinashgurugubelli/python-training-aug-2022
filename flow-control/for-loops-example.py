"""
What is for loop?:
- In python for loop is used to iterate over a sequence(List, tuple, string)
- Syntax
for val in sequence:
    loop statements/body
"""

ages = [10, 0, 17, 160, 18, 35]

# for age in ages:
#     if age >= 18:
#         if age > 150:
#             message = f'Passed age: {age}  - Your age is greater than 150 , you are not eligible to vote'
#             print(message)
#         else:
#             print("eligible to vote")
#     else:
#         print("you are a minor , you are not eligible to vote")


"""
# range() function
range(10) -> 0 to 9
range(start, end, step_size)
"""

# for x in range(10):
#     print(x)


# for y in range(1, 10, 2):
#     print(y)

# Iterate through a list using indexing
employees = [
    {
        "name": "Jack",
        "gender": "M",
        "skills": [
            {
                "skill": "C#",
                "experience": 5
            },
            {
                "skill": "Python",
                "experience": 7
            },
            {
                "skill": "Java",
                "experience": 10
            }

        ]
    },
    {
        "name": "Andriea",
        "gender": "F",
        "skills": [
            {
                "skill": "C#",
                "experience": 5
            },
            {
                "skill": "Python",
                "experience": 7
            },
            {
                "skill": "Java",
                "experience": 10
            }

        ]
    },
    {
        "name": "Jhon",
        "gender": "M",
        "skills": [
            {
                "skill": "C#",
                "experience": 5
            },
            {
                "skill": "Python",
                "experience": 7
            },
            {
                "skill": "Java",
                "experience": 10
            }

        ]
    }
]

# for i in range(len(employees)):
#     name = employees[i]["name"]
#     gender = employees[i]["gender"]
#     if(gender == 'M'):
#         print("Mr." + name)
#     else:
#         print("Ms."+name)


# for employee in employees:
#     print("Employee name: " + employee['name'])
#     current_employee_skills = employee['skills']
#     # print(current_employee_skills)
#     for s in current_employee_skills:
#         print("Skill : " + s["skill"])


"""
For loop with else

this for..else statement can be used with break keyword.
to run the else block only when the break keyword was not executed.

Break keyword: 
- break statement terminates the loop containing it. 
- control of the program flows to the statement immediately after the body of the loop.
"""
# num_to_search = 80
# nums = [10, 20, 30, 40, 50, 60]

# for num in nums:
#     if num == num_to_search:
#         print("searched number found")
#         break
#     print("current number: " + str(num))
# else:
#     print("No number found")


"""
Continue key word:
- The continue statement/keyword is used to skip the code inside a loop of the current iteration only. 
- i.e. Loop dose not terminate but continues on with the next iteration.
"""
name = "jack is handsome"

# for letter in name:
#     if letter == "s":
#         continue
#     print("Current letter: " + letter)
# print("End of for loop")


"""
pass statement:

In python the pass statement is null statement.
the difference b/w a comment and pass statement in python is that while the interpreter ignores a comment completely.
pass is not ignored, However nothing happens when the pass is executed, it results no operation

"""

word = "ABCD"

for val in word:
    pass


"""
While loop:
- like for loop it is also used to iterate over a block of code as long as the test condition met (true).
- we generally use this loop when we don't know the number of times to iterate beforehand.

while test_expression:
    block of code.
"""

n = 10
counter = 5
sum = 0

while counter <= n:
    sum = sum+1  # incrementing the sum
    counter = counter+1  # updating the counter

print("Sum value: " + str(sum))


"""
while loop with else - Home work
"""
