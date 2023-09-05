0x08. Python - More Classes and Objects
Learning Objectives

1.What is OOP
2.What is “first-class everything”
3.What is a class
4.What is an object and an instance
5.What is the difference between a class and an object or instance
6.What is an attribute
7.What are public, protected and private attributes
8.What is self
9.What is a method
10.How to use public, protected and private attributes
11.What is the special __init__ method
12.How to use the __init__ method
13.What is Data abstraction, data encapsulation, and information hiding
14.What is a property
15.What is the difference between an attribute and a property in Python
16.What is the Pythonic way to write getters and setters in Python
17.What are the special __str__ and __repr__ methods
18.How to use the __str__ and __repr__ methods
19.What is the difference between the __str__ and __repr__
20.What is a class attribute
21.What is the difference between an object attribute and a class attribute
22.What is a class method
23.What is a static method
24.How to dynamically create arbitrary new attributes for existing instances of a class
25.How to bind attributes to objects and classes
26.What is and what does contain __dict__ of a class and of an instance of a class
27.How does Python find the attributes of an object or class
28.How to use the getattr function

Tasks
0. Simple rectangle
Write an empty class “Rectangle” that defines a rectangle
Requirements
You are not allowed to import any module

Algorithm
Define class with keyword class and name Rectangle
Initialize class method __init__
End


1. Real definition of a rectangle
Write a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
Requirements
Private instance attribute: width:
Property def width(self): to retrieve it
Property setter def width(self, value): to set it
Width must be an integer, otherwise raise a TypeError exception with the message “width must be an integer”
If width is less than 0, raise a ValueError exception with the message “width must be >= 0”
Private instance attribute: height:
Property def height(self): to retrieve it
Property setter def height(self, value): to set it
Height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
If height is less than 0, raise a ValueError exception with the message “height must be >= 0”
Instantiation with optional width and height: def __init__(self, width=0, height=0):
You are not allowed to import any module

Algorithm
Initialize the class Rectangle
Class method is initialized __init__
Declare the @property function to define the properties

2. Area and Perimeter
Write a class Rectangle that defines a rectangle by: (based on 1-rectangle.py)
Requirements:
Private instance attribute: width:
Property def width(self): to retrieve it
Property setter def(self, value) to set it
Width must be an integer, otherwise a TypeError exception with the message with must be an integer
If width is less than 0, raise a ValueError exception with the message width must be >= 0
Private instance attribute: height:
Property def height(self): to retrieve it
Property setter def height(self, value) to set it
Height must be an integer, otherwise raise a TypeError exception with the message “height must be an integer”
If height is less than 0, raise a ValueError exception with the message “height must be >= 0”
Instantiation with optional width and height:def __init__(self, width=0, height=0):
Public instance method: def area(self): that returns the rectangle area
Public instance method: def perimeter(self): that returns the rectangle perimeter:
If width or height is equal to 0, perimeter is equal to 0
You are not allowed to import any module

Algorithm
Define class Rectangle
Define class method __init__ with attributes both public and private
Initialize the attributes
Define the properties for the private attributes
Define the public instance methods

 3. String representation
Write a class Rectangle that defines a rectangle by: (based on 2-rectangle.py)
Requirements
Private instance attribute: width:
Property def width(self): to retrieve it
Property setter def width(self, value): to set it
Width must be an integer, otherwise raise a TypeError exception with the message “width must be an integer”
If “width” is less than 0, raise a ValueError exception with the message “width must be >= 0”
Private instance attribute: height:
Property def height(self): to retrieve it
Property setter def height(self, value): to set it:
Height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
If height is less than 0, raise a ValueError exception with the message “height must be >= 0”
Instantiation with optional width and height:def __init__(self, width=0, height=0):
Public instance method: def area(self): that returns the rectangle area
Public instance method: def perimeter(self): that returns the rectangle perimeter
If width or height is equal to 0, perimeter has to be equal to 0
print() and str() should print the rectangle with the character #
You are not allowed to import any module

Algorithm
Define class Rectangle
Define class method __init__ with attributes both public and private
Initialize the attributes
Define the properties for the private attributes
Define the public instance methods
Define the __str__


4. Eval is magic
Write a class Rectangle that defines a rectangle by: (based on 2-rectangle.py)
Requirements
Private instance attribute: width:
Property def width(self): to retrieve it
Property setter def width(self, value): to set it
Width must be an integer, otherwise raise a TypeError exception with the message “width must be an integer”
If “width” is less than 0, raise a ValueError exception with the message “width must be >= 0”
Private instance attribute: height:
Property def height(self): to retrieve it
Property setter def height(self, value): to set it:
Height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
If height is less than 0, raise a ValueError exception with the message “height must be >= 0”
Instantiation with optional width and height:def __init__(self, width=0, height=0):
Public instance method: def area(self): that returns the rectangle area
Public instance method: def perimeter(self): that returns the rectangle perimeter
If width or height is equal to 0, perimeter has to be equal to 0
print() and str() should print the rectangle with the character #
repr() should return a string representation of the rectangle to be able to recreate a new instance by using eval() (see example below)
You are not allowed to import any module

Algorithm
Define class Rectangle
Define class method __init__ with attributes both public and private
Initialize the attributes
Define the properties for the private attributes
Define the public instance methods
Define the __str__ and __repr__


5. Detect instance deletion
Write a class Rectangle that defines a rectangle by: (based on 2-rectangle.py)
Requirements
Private instance attribute: width:
Property def width(self): to retrieve it
Property setter def width(self, value): to set it
Width must be an integer, otherwise raise a TypeError exception with the message “width must be an integer”
If “width” is less than 0, raise a ValueError exception with the message “width must be >= 0”
Private instance attribute: height:
Property def height(self): to retrieve it
Property setter def height(self, value): to set it:
Height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
If height is less than 0, raise a ValueError exception with the message “height must be >= 0”
Instantiation with optional width and height:def __init__(self, width=0, height=0):
Public instance method: def area(self): that returns the rectangle area
Public instance method: def perimeter(self): that returns the rectangle perimeter
If width or height is equal to 0, perimeter has to be equal to 0
print() and str() should print the rectangle with the character #
repr() should return a string representation of the rectangle to be able to recreate a new instance by using eval() 
Print the message “Bye rectangle … (... being 3 dots not ellipsis) when an instance of Rectangle is deleted
You are not allowed to import any module

Algorithm
Define class Rectangle
Define class method __init__ with attributes both public and private
Initialize the attributes
Define the properties for the private attributes
Define the public instance methods
Define the __str__ and __repr__ methods
Define the __del__ method


6. How many instances
Write a class Rectangle that defines a rectangle by: (based on 2-rectangle.py)
Requirements
Private instance attribute: width:
Property def width(self): to retrieve it
Property setter def width(self, value): to set it
Width must be an integer, otherwise raise a TypeError exception with the message “width must be an integer”
If “width” is less than 0, raise a ValueError exception with the message “width must be >= 0”
Private instance attribute: height:
Property def height(self): to retrieve it
Property setter def height(self, value): to set it:
Height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
If height is less than 0, raise a ValueError exception with the message “height must be >= 0”
Instantiation with optional width and height:def __init__(self, width=0, height=0):
Public instance method: def area(self): that returns the rectangle area
Public instance method: def perimeter(self): that returns the rectangle perimeter
If width or height is equal to 0, perimeter has to be equal to 0
print() and str() should print the rectangle with the character #
repr() should return a string representation of the rectangle to be able to recreate a new instance by using eval() 
Print the message “Bye rectangle … (... being 3 dots not ellipsis) when an instance of Rectangle is deleted
You are not allowed to import any module

Algorithm
Define class Rectangle
Define class method __init__ with attributes both public and private
Initialize the attributes
Define the properties for the private attributes
Define the public class attribute “number_of_instances”
Initialized to 0
Incremented during each new instance instantiation
Decremented during each instance deletion
Define the public instance methods
Define the __str__ and __repr__ methods
Define the __del__ method

7. Change representation
Write a class Rectangle that defines a rectangle by: (based on 2-rectangle.py)
Requirements
Private instance attribute: width:
Property def width(self): to retrieve it
Property setter def width(self, value): to set it
Width must be an integer, otherwise raise a TypeError exception with the message “width must be an integer”
If “width” is less than 0, raise a ValueError exception with the message “width must be >= 0”
Private instance attribute: height:
Property def height(self): to retrieve it
Property setter def height(self, value): to set it:
Height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
If height is less than 0, raise a ValueError exception with the message “height must be >= 0”
Public class attribute “number_of_instances”
Initialized to 0
Incremented during each new instance instantiation
Decremented during each instance deletion
Public class attribute “print_symbol”
Initialized to #
Used as symbol for string representation
Can be any type
Instantiation with optional width and height:def __init__(self, width=0, height=0):
Public instance method: def area(self): that returns the rectangle area
Public instance method: def perimeter(self): that returns the rectangle perimeter
If width or height is equal to 0, perimeter has to be equal to 0
print() and str() should print the rectangle with the character #
repr() should return a string representation of the rectangle to be able to recreate a new instance by using eval() 
Print the message “Bye rectangle … (... being 3 dots not ellipsis) when an instance of Rectangle is deleted
You are not allowed to import any module

Algorithm
Define class Rectangle
Define class method __init__ with attributes both public and private
Initialize the attributes
Define the properties for the private attributes
Define the public class attribute “number_of_instances”
Define the public class attribute “print_symbol”
Define the public instance methods
Define the __str__ and __repr__ methods
Define the __del__ method


8. Compare rectangles
Write a class Rectangle that defines a rectangle by: (based on 2-rectangle.py)
Requirements
Private instance attribute: width:
Property def width(self): to retrieve it
Property setter def width(self, value): to set it
Width must be an integer, otherwise raise a TypeError exception with the message “width must be an integer”
If “width” is less than 0, raise a ValueError exception with the message “width must be >= 0”
Private instance attribute: height:
Property def height(self): to retrieve it
Property setter def height(self, value): to set it:
Height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
If height is less than 0, raise a ValueError exception with the message “height must be >= 0”
Public class attribute “number_of_instances”
Initialized to 0
Incremented during each new instance instantiation
Decremented during each instance deletion
Public class attribute “print_symbol”
Initialized to #
Used as symbol for string representation
Can be any type
Instantiation with optional width and height:def __init__(self, width=0, height=0):
Public instance method: def area(self): that returns the rectangle area
Public instance method: def perimeter(self): that returns the rectangle perimeter
If width or height is equal to 0, perimeter has to be equal to 0
print() and str() should print the rectangle with the character #
repr() should return a string representation of the rectangle to be able to recreate a new instance by using eval() 
Print the message “Bye rectangle … (... being 3 dots not ellipsis) when an instance of Rectangle is deleted
Static method “def bigger_or_equal(rect_1, rect_2):” that returns the biggest rectangle based on the area
rect_1 must be an instance of “Rectangle”, otherwise raise a “TypeError” exception with the message “rect_1 must be an instance of Rectangle”
rect_2 must be an instance of “Rectangle”, otherwise raise a “TypeError” exception with the message “rect_2 must be an instance of Rectangle”
Returns rect_1 if both have the same area value
You are not allowed to import any module

Algorithm
Define class Rectangle
Define class method __init__ with attributes both public and private
Initialize the attributes
Define the properties for the private attributes
Define the public class attribute “number_of_instances”
Define the public class attribute “print_symbol”
Define the public instance methods
Define the __str__ and __repr__ methods
Define the __del__ method
Create the static method “def bigger_or_equal(rect_1, rect_2)


9. A square is a rectangle
Write a class Rectangle that defines a rectangle by: (based on 2-rectangle.py)
Requirements
Private instance attribute: width:
Property def width(self): to retrieve it
Property setter def width(self, value): to set it
Width must be an integer, otherwise raise a TypeError exception with the message “width must be an integer”
If “width” is less than 0, raise a ValueError exception with the message “width must be >= 0”
Private instance attribute: height:
Property def height(self): to retrieve it
Property setter def height(self, value): to set it:
Height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
If height is less than 0, raise a ValueError exception with the message “height must be >= 0”
Public class attribute “number_of_instances”
Initialized to 0
Incremented during each new instance instantiation
Decremented during each instance deletion
Public class attribute “print_symbol”
Initialized to #
Used as symbol for string representation
Can be any type
Instantiation with optional width and height:def __init__(self, width=0, height=0):
Public instance method: def area(self): that returns the rectangle area
Public instance method: def perimeter(self): that returns the rectangle perimeter
If width or height is equal to 0, perimeter has to be equal to 0
print() and str() should print the rectangle with the character #
repr() should return a string representation of the rectangle to be able to recreate a new instance by using eval() 
Print the message “Bye rectangle … (... being 3 dots not ellipsis) when an instance of Rectangle is deleted
Static method “def bigger_or_equal(rect_1, rect_2):” that returns the biggest rectangle based on the area
rect_1 must be an instance of “Rectangle”, otherwise raise a “TypeError” exception with the message “rect_1 must be an instance of Rectangle”
rect_2 must be an instance of “Rectangle”, otherwise raise a “TypeError” exception with the message “rect_2 must be an instance of Rectangle”
Returns rect_1 if both have the same area value
Class method “def square(cls, size=0)” that returns a new Rectangle instance with “width == height == size”
You are not allowed to import any module

Algorithm
Define class Rectangle
Define class method __init__ with attributes both public and private
Initialize the attributes
Define the properties for the private attributes
Define the public class attribute “number_of_instances”
Define the public class attribute “print_symbol”
Define the public instance methods
Define the __str__ and __repr__ methods
Define the __del__ method
Create the static method “def bigger_or_equal(rect_1, rect_2)


10. N queens
The N queens puzzle is the challenge of placing N non-attacking queens on an NxN chessboard. Write a program “nqueens” that solves the N queens problem. N must be an integer greater or equal to 4. 
Requirements
If the user called the program with the wrong number of arguments, print “Usage: nqueens N” followed by a new line, and exit with the status of 1
If N is not an integer, print “N must be a number” followed by a new line, and exit with the status 1
If N is smaller than 4, print “N must be at least 4”, followed by a new line, and exit with the status 1
The program should print every possible solution to the problem. One solution per line. You don’t have to print the solutions in a specific order
You are only allowed to import the sys module

