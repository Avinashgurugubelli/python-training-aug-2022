print("Hello world")
print("Welocome")


"""
Python Data types
---------------
String -> v = "ABC"
int    -> n = 12
float  -> f = 12.0
list   -> l = ["A", "B", "C"]
tuple  -> t = ("A", "B", "C")
set    -> s = {"Jack", "max"}
dict   -> d = {"Name": "Jack", "Age": 30 }

"""

"""
names = ["Jack", "Jhon", "Martin",  "Jack"]

List:
- Allows duplicated, since the list are indexed.
- Accessing an element: -> name_of_list[index] e.g. names[0], names[1]
- Size of list: len(names) -> 4
- When you are trying to access the element beyond the range: e.g. names is 4 -> now you are accessing names[4]
 - > error will be thrown -> Index out of range.
- Updating the value: names[0] = "Sony"
- Add a new value to list (append): when the new value is added it will append at the end. e.g. names.append("Ravi")
  Now the new list will be: ["Sony", "Jhon", "Martin",  "Jack", "Ravi"]
- list is Ordered.
- print(type(names)) -> list
"""


"""
e.g. tp = ("A", "B", "C", "A")
Tuple:
- Allows duplicated, since the tuple are indexed.
- Accessing an element: -> name_of_tuple[index] e.g. tp[0], tp[1]
- when you are trying to assign/update it will thrown an error: TypeError: 'tuple' object does not support item assignment
- Tuple is orderd.
"""

tp = ["A", "B", "C", "A"]
tp[0] = "Z"
print(tp)

"""
DICT:

dc = {
  "Key-1": "Value",
  "Key-2": "Value-2,
  "Key-3" [
    {
        key: [
            {

            }
        ]
    }
  ]
}
- it will not allow duplicate key.
- Access the dic -> dc["key-1"]
"""


"""
s = {"x", "y", "z"}

- Set is unordered
- Duplicates Not Allowed
"""


x = "1"

print(type(x))
print(int(x))
