0x0A. Python - Inheritance
Learning Objectives
1.What is a superclass?
2.What is a base class?
3.What is a parent class?
4.What is a subclass?
5.How to list all attributes and methods of a class or instance?
6.When can an instance have new attributes?
7.How to inherit a class from another?
8.How to define a class with multiple base classes?
9.What is the default class every class inherits from?
10.How to override a method or attribute inherited from the base class?
11.Which attributes or methods are available by heritage to subclasses?
12.What is the purpose of inheritance?
13.What are isinstance, issubclass, type and super?
14.When to use isinstance, issubclass, type and super?
15.How to use isinstance, issubclass, type and super?


Tasks
0. Lookup
Write a function ‘def lookup(obj):’ that returns the list of available attributes and methods of an object
Requirements
1. You are not allowed to import any module

Algorithm
1. Create a list attributes to store the attributes of the object
2. Iterate over the attributes of the object, and add each attribute to the list attributes
3. Create a list methods to store the methods of the object
4. Iterate over the methods of the object, and add each method to the list methods.
5. Return the list attributes and methods


1. My list
Write a class “MyList” that inherits from “list”. Create a public instance method “def print_sorted(self)” that prints the list, but sorted(ascending sort). You can assume that all the elements of the list will be of type “int”.
Requirements
1.You are not allowed to import any module

Algorithm
1. Create a class MyList that inherits from list
2. Add a public instance method “def print_sorted(self)” to the class MyList
3. The print_sorted() method should sort the list and then print the list


2. Exact same object
Write a function “def is_same_class(obj, a_class)” that returns “True” if the object is exactly an instance of the specified class; otherwise “False”.
Requirements
1. You are not allowed to import any module

Algorithm
1. Check if the object is an instance of the specified class
2. If the object is an instance of the specified class, return “True”
3. Otherwise, return “False”


3. Same class or inherit from
Write a function “def is_kind_of_class(obj, a_class)” that returns “True” if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class; otherwise “False”.
Requirements
1. You are not allowed to import any module

Algorithm
1. Check if obj is an instance of a_class. If yes, return true;
2. If obj is a type, check if it is a base class of a_class. If yes, return True
3. Otherwise, return False


4. Only subclass of
Write a function “def inherits_from(obj, a_class)” that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.
Requirement
1. You are not allowed to import any module

Algorithm
1. Check if obj is an instance of a_class. If yes, return True.
2. Otherwise, for each base class of a_class, recursively call the function inherits_from(obj, base_class). If any of the recursive calls return True, return True.
3. Otherwise, return False


5. Geometry module
Write an empty class “BaseGeometry”
Requirement
1. You are not allowed to import any module

Algorithm
1. Use the pass statement to create an empty class


6. Improve Geometry
Write a class “BaseGeometry”( based on 5-base_geometry.py). Create the public instance method: “def area(self)” that raises an “Exception” with the message “area() is not implemented”.
Requirements
1. You are not allowed to import any module

Algorithm
1. Create a class called “BaseGeometry”
2. Add a public instance method called “area()” that raises an “Exception” with the message “area() is not implemented”


7. Integer validator
Write a class “BaseGeometry” (based on 6-base_geometry.py). Create the public instance method: “def area(self)” that raises an “Exception” with the message “area() is not implemented”. Create the public instance method “def integer_validator(self, name, value)” that validates “value”. You can assume “name” is always a string.
Requirements
1. If value is not an integer: raise a TypeError exception, with the message “<name> must be an integer”
2. If value is less or equal to 0: raise a ValueError exception with the message “<name> must be greater than 0”
3. You are not allowed to import any module

Algorithm
1. Add a public instance method “integer_validator” 


8. Rectangle
Write a class “Rectangle” that inherits from “BaseGeometry” (7-base_geometry.py). Create an instantiation with “width” and “height” : “def __init__(self, width, height)”. 
Requirements
1. Width and height must be private. No getter or setter
2. Width and height must be positive integers, validated by “integer_validator”

Algorithm
1. Add the class method __init__


9. Full rectangle
Write a class “Rectangle” that inherits from “BaseGeometry” (7-base_geometry.py). (task based on 8-rectangle.py). Create an instance with width and height “def __init__(self, width, height)”. 
Requirements.
1. The area() method must be implemented. 
2. print() should print, and str() should return, the following rectangle description: “[Rectangle] <width>/<height>”


10. Square #1
Write a class “Square” that inherits from “Rectangle” (9-rectangle.py). Create the instance with “size” : ‘def __init__(self, size)”.
Requirements
1.size must be private. No getter or setter
2.size must be a positive integer, validated by “integer_validator”
3.the area() method must be implemented


11. Square #2
Write a class “Square” that inherits from “Rectangle” (9-rectangle.py). (task based on 10-square.py). Create the instance def __init__(self, size). The area() method must be implemented. 
Requirements
1. print() should print, and str() should return, the square description “[Square] <width>/<height>”

