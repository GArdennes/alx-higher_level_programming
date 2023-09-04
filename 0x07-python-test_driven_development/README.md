0. Integers addition
Write a function “def add_integer(a, b=98)” that adds 2 integers.
Requirements
a and b must be integers or floats, otherwise, raise a TypeError exception with the message “a must be an integer” or “b must be an integer”
a and b must be first cast to integers if they are float
Returns an integer: the addition of a and b
You are not allowed to import any module

Algorithm
Define function
Check the input arguments with conditions
If a is not an integer or float raise TypeError with exception message
If b is not an integer or float raise TypeError with exception message
Return the addition of the two arguments

1. Divide a matrix
Write a function “def matrix_divided(matrix, div)” that divides all elements of a matrix.
Requirements
matrix must all be a list of lists of integers or floats, otherwise raise a TypeError exception with the message “matrix must be a matrix (list of lists) of integers / floats”
each row of the matrix must be of the same size, otherwise raise a TypeError exception with the message “each row of the matrix must have the same size”
div must be a number(integer or float), otherwise raise a TypeError exception with the message “div must be a number”
div can’t be equal to 0, otherwise raise a ZeroDivisionError exception with the message “division by zero”
All elements of the matrix should be divided by div, rounded to 2 decimal places
Returns a new matrix
You are not allowed to import any module

Algorithm
Define function
Check input arguments with conditionals
If the matrix is not a list of lists of integers or floats raise a TypeError
If matrix lists in the list is not the same length raise a TypeError
If div is not a float or integer raise a TypeError
If div is 0 raise a ZeroDivisionError
Perform division of elements of the matrix
Return new matrix


2. Say my name
Write a function “def say_my_name(first_name, last_name=””)” that prints “My name is <first name> <last name>
Requirements
First name and last name must be strings otherwise, raise a TypeError exception with the message “first_name must be a string” or “last_name must be a string”
You are not allowed to import any module

Algorithm
Define function
Check if arguments are strings with conditionals
If first_name is not a string raise a TypeError
If last_name is not a string raise a TypeError
Return print statement


3. Print square
Write a function “def print_square(size)” that prints a square with the character #
Requirements
size is the size length of the square
size must be an integer, otherwise raise a TypeError exception with the message “size must be an integer”
If size is less than 0, raise a ValueError exception with the message “size must be >= 0”
If size is a float and is less than 0, raise a TypeError exception with the message “size must be an integer”
You are not allowed to import any module

Algorithm
Define function
Check if the argument is integer, 0 or float with conditionals
If not an integer raise TypeError 
If less than 0 raise ValueError
If size is float and less than 0 raise TypeError
Print # symbol


4. Text indentation
Write a function “def text_indentation(text)” that prints a text with 2 new lines after each of these characters: ., ? and :
Requirements
text must be a string, otherwise, raise a TypeError exception with the message “text must be a string”
There should be no space at the beginning or at the end of each printed line
You are not allowed to import any module

Algorithm
Define function
Check if arguments are correct with conditionals
Iterate through the string to check for the presence of special characters
Print 2 new lines if yes else continue


5. Max integer - Unittest
In this task, you will write unittests for the function “def max_integer(list=[]).
Requirements
Your test file should be inside a folder “tests”
You have to use the unittest module
Your test file should be python files
Your test file should be executed by using this command: python3 -m unittest tests.6-max_integer_test
All tests you make must be passable by the given function below

