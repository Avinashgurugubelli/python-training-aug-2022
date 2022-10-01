import json

"""
File operation is a I/O operation

1. Open a file
2. Read / Write (Perform operation)
3. close the file
"""

# Opening a file


f = open("sample.txt")  # Open file in the current directory.
# if it is other location specify a path
# f = open("D:/Trainings/python/python-training-aug-2022/file-operations/sample.txt")

"""
File modes:

Open text modes:

- r - (read) -> default value -> open file for reading -> it will throws an error if the file not exists in the path.
- a  - (append) -> open file for appending the content, it will create a new if file not exists
- w - (write) -> open file for a write operation, it will create a new file if the file not exists
- (x) - (create) -> create a file in the path specified -> it will throw an error if the file already exists
- (b) - opens a file in binary format
- (+) - opens a file for updating (reading and writing)


f = open("sample.txt", 'w') -> write in a text mode
f = open("img.bmp", "r+b") -> read and write in binary format

Encoding - highly recommended, to work seamlessly in diff platforms

f = open("sample.txt", 'r', 'utf-8')


Closing a file:
--------------
when we done with the performing the task(operation) on a file, we need to properly close the file to avoid deadlock issues.

f = open("sample.txt", 'r', 'utf-8')
f.close()

- Best practice: This way are guaranteeing that the file is properly closed even when some exception occurs.
try:
    f = open("sample.txt", 'r', 'utf-8')
finally:
    f.close()

In python, We don't need to explicitly call the close() method. it is done internally with below way
Recommended approach:

with open("sample.txt", 'r', 'utf-8') as f:
    # perform your operations

"""

# reading a file

# f = open("sample.txt", "r", encoding="utf-8")
# print(f.read())
# f.close()

"""
f.read() -> will read all the content
f.readline() -> will read only one line
f.readlines() -> returns a list of lines of the entire file.
"""
# with open("sample.txt", "r", encoding="utf-8") as f:
#     data = f.readlines()
# loop the loop - as DATA is array/list now

# with open("sample.txt", "w", encoding="utf-8") as f:
#     f.write("Hey,")
#     f.write("Written from program")


def read_json(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        # holds the data in a string
        data = file.read()
        # print(data)
        try:
            # holds the data in a json obj (convening string to json)
            obj = json.loads(data)
            print(obj["name"])
            print(obj)
        except json.decoder.JSONDecodeError as ex:
            print('Invalid JSON file')
        except Exception as ex:
            print("Exception occurred while reading a JSON file")
            print(ex)


read_json("sample.json")
# read_json("sample.txt")
