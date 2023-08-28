0. Safe list printing
Write a function ‘def safe_print_list(my_list=[], x=0)’ that prints x elements of a list
Requirements
my_list can contain any type(integer, string, etc.)
All elements must be printed on the same line followed by a new line
x represents the number of elements to print
returns the real number of elements printed
you have to use try: / except:
you are not allowed to import any module
you are not allowed to use len()


1. Safe printing of an integers list
Write a function ‘def safe_print_integer(value)’ that prints an integer with “{:d}”.format()
Requirements
value can be any type (integer, string, etc)
The integer should be printed followed by a new line
Returns true if value has been correctly printed (it means the value is an integer). Otherwise return false
You have to use try: / except:
You have to use “{:d}”.format() to print as integer
You are not allowed to import any module
You are not allowed to use type()


2. Print and count integers
Write a function def safe_print_list_integers(my_list=[], x=0) that prints the first x elements of a list and only integers. my_list can contain any type (integer, string, etc). All integers have to be printed on the same line followed by a new line - other type of value in the list must be skipped (in silence).
Requirements
x represents the number of elements to access in my_list
x can be bigger than the length of my_list - if it’s the case, an exception is expected to occur
Returns the real number of integers printed
You have to use try: / except:
You have to use “{:d}”.format()
You are not allowed to import any module
You are not allowed to use len()


3. Integers division with debug
Write a function def safe_print_division(a, b) that divides 2 integers and prints the result. You can assume that a and b are integers.
Requirements
The result of the division should print on the “finally:” section preceded by “Inside result:”
Returns the value of the division, otherwise: “None”
You have to use “try: / except: / finally:
You have to use “{}”.format() to print the result
You are not allowed to import any module


4. Divide a list
Write a function “def list_division(my_list_1, my_list_2, list_length):” that divides element 2 lists
my_list_1 and my_list_2 can contain any type (integer, string, etc.)
Requirements
Returns a new list(length = list_length) with all divisions
If 2 elements can’t be divided, the division result should be equal to 0
If an element is not an integer or float, print: wrong type
If the division can’t be done (/0), print: division by 0
If my_list_1 or my_list_2 is too short, print: out of range
You have to use “try: / except: / finally:
You are not allowed to import any module


5. Raise exception
Write a function ‘def raise_exception()’ that raises a type exception. You are not allowed to import any module.


6. Raise a message
Write a function ‘def raise_exception_msg(message=””)’ that raises a name exception with a message. You are not allowed to import any module.

