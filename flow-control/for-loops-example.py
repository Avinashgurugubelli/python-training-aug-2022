"""
What is for loop?:
- In python for loop is used to iterate over a sequence(List, tuple, string)
- Syntax
for val in sequence:
    loop statements/body
"""
from ast import AugAssign
from email import message


ages = [10, 0, 17, 160, 18, 35]

for age in ages:
    if age >= 18:
        if age > 150:
            message = f'Passed age: {age}  - Your age is greater than 150 , you are not eligible to vote'
            print(message)
        else:
            print("eligible to vote")
    else:
        print("you are a minor , you are not eligible to vote")


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
names = [
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
    }
]

for i in range(len(names)):
    name = names[i]["name"]
    gender = names[i]["gender"]
    if(gender == 'M'):
        print("Mr." + name)
    else:
        print("Ms."+name)
