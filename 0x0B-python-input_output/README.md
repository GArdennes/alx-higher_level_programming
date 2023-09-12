0x0B. Python - Input/Output
Learning Objectives
1.How to open a file
2.How to write text in a file
3.How to read the full content of a file
4.How to read a file line by line 
5.How to move the cursor in a file
6.How to make sure a file is closed after using it
7.What is the with statement
8.How to use the with statement
9.What is JSON
10.What is serialization
11.What is deserialization
12.How to convert a Python data structure to a JSON string
13.How to convert a JSON string to a Python data structure

Tasks
0. Read file
Write a function “def read_file(filename=””)” that reads a text file(UTF8) and prints it to stdout.
Requirements
You must use the with statement
You don’t need to manage file permission or file doesn’t exist exceptions
You are not allowed to import any module

Algorithm
1. Open the file in read mode, with the encoding mode utf-8
2. Read the contents of the file
3. Print the contents of the file to stdout
4. Close the file

1. Write to a file
Write a function “def write_file(filename=””, text=””)” that writes a string to a text file(UTF8) and returns the number of characters written
Requirements
You must use the with statement
You don’t need to manage file permission exceptions
Your function should create the file if doesn’t exist
Your function should overwrite the content of the file if it already exists
You are not allowed to import any module

Algorithm
1. Open the file in write mode
2. Write the text to the file
3. Get the number of characters written
4. Close the file


2. Append to a file
Write a function “def append_write(filename=””, text=””)” that appends a string at the end of a text file(UTF8) and returns the number of characters added
Requirements
If the file doesn’t exist, it should be created
You must use the with statement
You don’t need to manage file permission or file doesn’t exist exceptions
You are not allowed to import any module
Algorithm
1. Open the file in append mode
2. Write the text to the file
3. Get the number of characters written
4. Close the file


3. To JSON string
Write a function “def to_json_string(my_obj)” that returns the JSON representation of an object (string)
Requirements
You don’t need to manage exceptions if the object can’t be serialized

Algorithm
1. Import the json module
2. Use the json.dumps() function to serialize the object to a JSON string.


4. From JSON string to Object
Write a function “def from_json_string(my_str)” that returns an object(Python data structure) represented by a JSON string
Requirements
You don’t need to manage exceptions if the JSON string doesn’t represent an object

Algorithm
1. Import the json module
2. Use the json.loads() function to deserialize the JSON string to an object


5. Save Object to a file
Write a function “def save_to_json_file(my_obj, filename)” that writes an Object to a text file, using a JSON representation.
Requirements
You must use the with statement
You don’t need to manage exceptions if the object can’t be serialized
You don’t need to manage file permission exceptions

Algorithm
1. Import the json module
2. Use the json.dumps() function to serialize the object to a JSON string
3. Open the file in write mode
4. Write the JSON string to the file
5. Close the file


6. Create object from a JSON file
Write a function “def load_from_json_file(filename)” that creates an Object from a “JSON file”:
Requirements
You must use the with statement
You don’t need to manage exceptions if the JSON string doesn’t represent an object
You don’t need to manage file permissions / exceptions

Algorithm
1. Import the json module
2. Open the file in read mode
3. Use the json.loads() function to deserialize the JSON string to an object
4. Close the file


7. Load, add, save
Write a script that adds all arguments to a Python list, and then save them to a file.
Requirements
You must use your function save_to_json_file from 5-save_to_json_file.py
You must use your function load_from_json_file from 6-load_from_json_file.py
The list must be saved as a JSON representation in a file named add_item.json
If the file doesn’t exist, it should be created
You don’t need to manage file permissions/exceptions

Algorithm
1. Import the sys module
2. Import the necessary functions from other files
3. Create a list to store the arguments
4. Iterate over the arguments and add them to the list
5. Save the list to a file


8. Class to JSON
Write a function “def class_to_json(obj)” that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object
Requirements
obj is an instance of a Class
All attributes of the obj class are serializable: list, dictionary, string, integer and boolean
You are not allowed to import any module

Algorithm
1. Check if the object is a list or a dictionary
2. If the object is a list, recursively call the class_to_json() function on each element of the list
3. If the object is a dictionary, recursively call the class_to_json() function on each key-value pair in the dictionary
4. If the object is a string, integer, or boolean, return the object itself


9. Student to JSON
Write a class Student that defines a student by using public instance attributes like first_name, last_name and age. Instantiate with “def __init__(self, first_name, last_name, age)”. Implement the public method def to_json(self) that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py)
Requirements
You are not allowed to import any module

Algorithm
1. Define a class “Student” with public instance attributes first_name, last_name, and age
2. Define the __init__(self, first_name, last_name, age) constructor that initializes the instance attributes
3. Define the to_json(self) method that returns a dictionary representation of the Student instance.


10. Student to JSON with filter
Write a class Student that defines a student by: (based on 9-student.py) with public instance attributes first_name, last_name and age and public method def to_json(self, attrs=None).
Requirements
If attrs is a list of strings, only attribute names contained in this list must be retrieved.
Otherwise, all attributes must be retrieved
You are not allowed to import any module


11. Student to disk and reload
Write a class Student that defines a student by: (based on 10-student.py). Public instance attributes: first_name, last_name, age. Public method def to_json(self, attrs=None). Public method def reload_from_json(self, json) that replaces all attributes of the Student instance. You can assume json will always be a dictionary. A dictionary key will be the public attribute name. A dictionary value will be the value of the public attribute.
Requirements
You are not allowed to import any module


12. Pascal's Triangle
Create a function def pascal_triangle(n) that returns a list of lists of integers representing the Pascal’s triangle of n:
Requirements
Returns an empy list if “n <= 0”
You can assume n will be always an integer
You are not allowed to import any module

Algorithm
1. Create a list of lists to store the Pascal’s triangle
2. Initialize the first row of the triangle to [1]
3. Iterate over the rows of the triangle, starting from the second row
4. For each row, initialize the first and last elements of the row to 1
5. For each element of the row, except for the first and last elements, set the element to the sum of the two elements above it
6. Return the Pascal’s triangle

