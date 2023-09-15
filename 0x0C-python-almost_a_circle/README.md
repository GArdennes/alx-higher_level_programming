0x0C. Python - Almost a circle
Background Context
In this project, you will review everything about Python:
Import
Exceptions
Class
Private attribute
Getter/Setter
Class method
Static method
Inheritance
Unittest
Read/Write file
args and kwargs
Serialization/Deserialization
JSON

Learning Objectives
1.What is unit testing and how to implement it in a large project
2.How to serialize and deserialize a Class
3.How to write and read a JSON file
4.What is *args
5.How to use *args
6.What is **kwargs
7.How to use **kwargs
8.How to handle named arguments in a function 

Tasks
0. If it's not tested it doesn't work
All your files, classes and methods must be unit tested and be PEP 8 validated.

1. Base class
Write the first class “Base” First create a folder named models with an empty file __init__.py inside - with this file, the folder will become a Python package. Secondly create a file named models/base.py. Create the class Base with the private class attribute “__nb_objects = 0” and the class constructor “def __init__(self, id=None)”. In the class constructor “def __init__” if id is not None, assign the public instance attribute id with this argument value - you can assume id is an integer and you don’t need to test the type of it. Otherwise, increment __nb_objects and assign the new value to the public instance attribute id.


2. First Rectangle
Write the class Rectangle that inherits from Base. In the file models/rectangle.py create the class Rectangle that inherits from Base. The class should have private instance attributes, each with its own public getter and setter, __width for width, __height for height, __x for x and __y for y. Create the class constructor def __init__(self, width, height, x=0, y=0, id=None), call the super class with id - this super call will use the logic of the __init__ of the Base class. Assign each argument width, height, x and y to the right attribute.


3. Validate attributes
Update the class Rectangle by adding validation of all setter methods and instantiation (id excluded)
Requirements
1. If the input is not an integer, raise the TypeError exception with the message: <name of the attribute> must be an integer. Example: width must be an integer
2. If width or height is under or equals 0, raise the ValueError exception with the message: <name of the attribute> must be > 0. Example width must be > 0
3. If x or y is under 0, raise the ValueError exception with the message: <name of the attribute> must be >= 0. Example: x must be >= 0


4. Area first
Update the class Rectangle by adding the public method def area(self) that returns the area value of the Rectangle instance.


5. Display #0
Update the class Rectangle by adding the public method “def display(self)” that prints in stdout the Rectangle instance with the character # - you don’t need to handle x and y here.


6. __str__
Update the class Rectangle by overriding the __str__ method so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>


7. Display #1
Update the class Rectangle by improving the public method “def display(self)” to print in stdout the Rectangle instance with the character # by taking care of x and y


8. Update #0
Update the class Rectangle by adding the public method def update(self, *args) that assigns an argument to each attribute, 1st attribute should be the id attribute, 2nd argument should be the width attribute, 3rd argument should be the height attribute, 4th argument should be the x attribute, 5th argument should be the y attribute


9. Update #1
Update the class Rectangle by updating the public method def update(self, *args) by changing the prototype to update(self, *args, **kwargs) that assigns a key/value argument to attributes, **kwargs can be thought of as a double pointer to a dictionary: key/value. As python doesn’t have pointers, **kwargs is not literally a double pointer - describing it as such is just a way of explaiining its behaviour in terms you’re already familiar with. **kwargs must be skipped if *args exists and is not empty. Each key in this dictionary represents an attribute to the instance.


10. And now, the Square!
Write the class “Square” that inherits from “Rectangle”. In the file models/square.py create the class Square that inherits from Rectangle. Create the class constructor “def __init__(self, size, x=0, y=0, id=None), in the constructor call the super class with id, x, y, width and height - this super call will use the logic of __init__ of the Rectangle class. The width and height must be assigned to the value of size. You must not create new attributes for this class, use all attributes of Rectangle - As reminder: a Square is a Rectangle with the same width and height. All width, height, x and y validation must inherit from Rectangle - same behavior in case of wrong data. The overloading __str__ method should return [Square] (<id>) <x>/<y> - <size> in our case, width or height.


11. Square size
Update the class Square by adding the public getter and setter size. The setter should assign (in this order) the width and the height - with the same value. The setter should have the same value validation as the Rectangle for width and height - No need to change the exception error message (it should be the one from width)


12. Square update
Update the class Square by adding the public method def update(self, *args, **kwargs) that assigns attributes. *args is the list of arguments - no keyworded arguments. 1st argument should be the id attribute. 2nd argument should be the size attribute. 3rd argument should be the x attribute. 4th argument should be the y attribute. **kwargs can be thought of as a double pointer to a dictionary: key/value (keyworded arguments). **kwargs must be skipped if *args exists and in not empty. Each key in this dictionary represents an attribute to the instance.


13. Rectangle instance to dictionary representation
Update the class Rectangle by adding the public method “def to_dictionary(self)” that returns the dictionary representation of a Rectangle. This dictionary must contain: id, width, height, x, y


14. Square instance to dictionary representation
Update the class Square by adding the public method def to_dictionary(self) that returns the dictionary representation of a Square. This dictionary must contain: id, size, x, y


15. Dictionary to JSON string
JSON is one of the standard formats for sharing data representation. Update the class Base by adding the static method def to_json_string(list_dictionaries) that returns the JSON string representation of list_dictionaries. “List_dictionaries” is a list of dictionaries. If “list_dictionaries” is None or empty, return the string: “[]”, otherwise, return the JSON string representation of “list_dictionaries”


16. JSON string to file
Update the class Base by adding the class method “def save_to_file(cls, list_objs)” that writes the JSON string representation of list_objs to a file. “List_objs” is a list of instances who inherits of “Base” - example: list of “Rectangle” or list of “Square” instances. If “list_objs” is “None”, save an empty list. The filename must be: <Class name>.json - example: “Rectangle.json”. You must use the static method “to_json_string” (created before). You must overwrite the file if it already exists.


17. JSON string to dictionary
Update the class “Base” by adding the static method “def from_json_string(json_string) that returns the list of the JSON string representation json_string. Json_string is a string representing a list of dictionaries. If json_string is None or empty, return an empty list. Otherwise, return the list represented by json_string.


18. Dictionary to Instance
Update the class Base by adding the class method def create(cls, **dictionary) that returns an instance with all attributes already set. **dictionary can be thought of as a double pointer to a dictionary. To use the update method to assign all attributes, you must create a ‘dummy’ instance before. Create a Rectangle or Square instance with ‘dummy’ mandatory attributes (width, height, size, etc). Call update instance method to this ‘dummy’ instance to apply your real values. You must use the method def update(self, *args, **kwargs). **dictionary must be used as **kwargs of the method update. You are not allowed to use eval


19. File to instances
Update the class Base by adding the class method “def load_from_file(cls)” that returns a list of instances. The filename must be <Class name>.json. Example Rectangle.json. If the file doesn’t exist, return an empty list, otherwise, return a list of instances - the type of these instances depends on cls (current class using this method). You must use the from_json_string and create methods (implemented previously)**

