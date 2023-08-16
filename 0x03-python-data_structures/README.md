0x03. Python - Data Structures: Lists, Tuples

Learning Objectives
1.What are lists 
1a.How to use lists
2.What are the differences and similarities between strings and lists
2a.What are the most common methods of lists and how to use them
3.How to use lists as stacks and queues
4.What are list comprehensions and how to use them
5.What are tuples and how to use them
6.When to use tuples versus lists
7.What is a sequence
8.What is tuple packing
9.What is sequence unpacking
10.What is the del statement and how to use it

Lists are mutable compound data structures that take elements of different data types. Lists can be manipulated in various ways, through concatenation, indexing and slicing. Lists and strings compare in terms of the following items; mutability, data types, indexing, slicing and methods. The most common methods of lists in Python are:
append(): adds an element to the end of the list. e.g. my_list.append("hello")
extend(): adds the element of another list to the end of the list e.g. my_list.extend(other_list)
insert(): inserts an element into the list at a specified index e.g. my_list.insert(1, "world")
remove(): removes an element from the list by its value e.g. my_list.remove("hello")
pop(): removes an element from the list at a specified index e.g. my_list.pop(1)
index(): returns the index of the first occurrence of an element in the list e.g. my_list.index("world")
count(): returns the number of occurrences of an element in the list e.g. my_list.count("hello")
sort(): sorts the list in ascending order e.g. my_list.sort()
reverse(): reverses the order of the list e.g. my_list.reverse()
clear(): removes all elements from the list e.g. my_list.clear()
A stack is a data structure in Data science which declares that items in the structure operate by a LIFO (Last In First Out). This can be implemented with the methods append() and pop(). A queue is a data structure in Data science which declares that items in the structure operate by a FIFO (First In First Out) principle. This can be implemented in lists with the methods insert() and popleft(). 

List Comprehensions on the other hand are syntactic constructs that are used to create a list from an iterable object in the following tasks: filtering, mapping and iterating over data. Iterating simply creating a new list by iterating over items in another list e.g. new_list = [letter for letter in "hello"] Mapping involves creating a list by applying a function over the elements in the list e.g. new_list = [x**2 for x in range(1, 11)]. Filtering involves creating a list over iterable elements in a list that meet a certain condition e.g. new_list = [x for x in range(1, 11) if x % 2 == 0].	 

 Tuples are immutable compound data structures that store various data types e.g. my_tuple = ("hello", 123, True).Tuples are used when the data items would not be changed. In python sequences are particular data types that contain an ordered list of items. Some types of sequences are lists, tuples, strings, ranges, bytes and bytearrays. Tuple packing is a way to assign multiple values to a tuple, sometimes the values could be the results of expressions e.g. my_tuple = (1 + 2, 3 * 4). Sequence unpacking on the other hand happens to be a way to store the elements of a sequence in multiple variables. It presents a simple way of assigning the results of expressions to multiple variables e.g.x, y = 1 + 2, 3 * 4 or x, y, z = my_tuple . The del statement is a way to remove elements from a list even to remove slices or clear entire lists.

Quiz Questions
Question #0 What do these lines print?
>>> a = [1, 2, 3, 4]
>>> a[-3]
Answer: 2

Question #1 What do these lines print?
>>> a = [1, 2, 3, 4]
>>> b = a
>>> b
Answer: [1, 2, 3, 4]

Question #2 What do these lines print?
>>> a = [1, 2, 3, 4]
>>> a[2] = 10
>>> a
Answer: [1, 2, 10, 4]

Question #3 What do these lines print?
>>> a = [1, 2, 3, 4]
>>> a.append(5)
>>> len(a)
Answer: 5

Question #4 What do these lines print?
>>> a = [1, 2, 3, 4]
>>> a[0]
Answer: 1

Question #5 What do these lines print?
>>> a = [1, 2, 3, 4]
>>> a[-1]
Answer: 4

Question #6 What do these lines print?
>>> a = [1, 2, 3, 4]
>>> b = a
>>> a[2] = 10
>>> b
Answer: [1, 2, 10, 4]

Question #7 What do these lines print?
>>> a = [1, 2, 3, 4]
>>> a[1:3]
Answer: [2, 3]

Question #8 What do these lines print?
>>> a = [1, 2, 3, 4]
>>> len(a)
Answer: 4

Question #9 What do these lines print?
>>> a = [1, 2, 3, 4]
>>> b = a
>>> a[2] = 10
>>> a
Answer: [1, 2, 10, 4]


Tasks
0. Print a list of integers
Write a function ‘def print_list_integer(my_list=[])’ that prints all integers of a list.
Requirements:
Print one integer per line
You are not allowed to import any module
You can assume that the list only contains integers
You are not allowed to cast integers into strings
You have to use string format to print integers

ALGORITHM
Create the file 0-print_list_integer.py
Declare the function 
Create a loop that iterates through the list
Print each item with the string format


1. Secure access to an element in a list
Write a function ‘def element_at(my_list, idx)’ that retrieves an element from a list like in C
Requirements:
If idx is negative, the function should return None
If idx is out of range(> of number of element in my_list), the function should return None
You are not allowed to import any module
You are not allowed to use try/except

ALGORITHM
Create the file 1-element_at.py
Define the function
Create a conditional to check if the element is less than 0
If yes then return None, else continue
Create a conditional to check if the element is out of range
If yes then return None, else continue
Return the value of the list at the index of idx


2. Replace element
Write a function ‘def replace_in_list(my_list, idx, element)’ that replaces an element of a list at a specific position (like in C)
Requirements:
If idx is negative, the function should not modify anything, and returns the original list
If idx is out of range, the function should not modify anything and returns the original list
You are not allowed to import any module
You are not allowed to use “try/except”

ALGORITHM
Create file 2-replace_in_list.py
Create the function declaration def replace_in_list(my_list, idx, element)
Create a condition to check if the index is out of range
Replace the value at index with element
Return the list


3. Print a list of integers... in reverse!
Write a function ‘def print_reversed_list_integer(my_list=[])’ that prints all integers of a list, in reverse order.
Requirements:
Print one integer per line
You are not allowed to import any module
You can assume that the list only contains integers
You are not allowed to cast integers into strings
You have to use string format to print integers

ALGORITHM
Create file 3-print_reversed_list_integer.py
Create function ‘def print_reversed_list_integer(my_list=[])’
Loop through the list to print all the elements in reverse order


4. Replace in a copy
Write a function ‘def new_in_list(my_list, idx, element)’ that replaces an element in a list at a specific position without modifying the original list
Requirements:
If idx is negative, the function should return a copy of the original list
If idx is out of range, the function should return a copy of the original list
You are not allowed to import any module
You are not allowed to use try/except

ALGORITHM
Create file 4-new_in_list.py
Create function def new_in_list(my_list, idx, element)
Create condition to check for index out of range
If true return original list
Create duplicate list 
Change index value in new list
Return new list


5. Can you C me now?
Write a function ‘def no_c(my_string)’ that removes all characters c and C from a string
Requirements:
The function should return the new string
You are not allowed to import any module
You are not allowed to use string replace method

ALGORITHM
Create the file 5-no_c.py
Create the function def no_c(my_string)
Create a new string variable
Iterate through the list for all letters of the string that pass the condition
Store the letters in the new string
Return the new string

6. Lists of lists = Matrix
Write a function ‘def print_matrix_integer(matrix = [[]])’  that prints a matrix of integers
Requirements:
You are not allowed to import any module
You can assume that the list only contains integers
You are not allowed to cast integers into strings
You have to use the string format to print integers

ALGORITHM
Create file 6-print_matrix_integer.py
Create function def print_matrix_integer(matrix = [[]])
Initialize a variable to store the index of the current row
Iterate over the rows of the matrix list

7. Tuples addition
Write a function ‘def add_tuple(tuple_a=(), tuple_b=())’ that adds 2 tuples
Requirements:
Return a tuple with 2 integers, the first element should be the addition of the first element of each argument, the second element should be the addition of the second element of each argument
You are not allowed to import any module
You can assume that the two tuples will only contain integers
If a tuple is smaller than 2, use the value 0 for each missing integer
If a tuple is bigger than 2, use only the first 2 integers

ALGORITHM
Create file 7-add_tuple.py
Create function def add_tuple(tuple_a = (), tuple_b=())
Create new tuple variable
Declare variables as placeholders for the elements of the tuples
Return new tuple with sum


8. More returns!
Write a function ‘def multiple_returns(sentence)’ that returns a tuple with the length of a string and its first character
Requirements:
If the sentence is empty, the first character should be equal to None
You are not allowed to import any module
ALGORITHM
Create file 8-multiple_returns.py
Create function def multiple_returns(sentence)
Check if sentence is empty
If yes then initialize first element to be None
Create new tuple variable to contain length of string and first element of string using tuple packing
Return new tuple


9. Find the max
Write a function ‘def max_integer(my_list=[])’ that finds the biggest integer of a list
Requirements:
If the list is empty, return None
You can assume that the list only contains integers
You are not allowed to import any module
You are not allowed to use the builtin max()

ALGORITHM
Create the file 9-max_integer.py
Create the function def max_integer(my_list=[])
Use the list method sort on the list argument and save in new list
Return last element of new list


10. Only by 2
Write a function ‘def divisible_by_2(my_list=[])’ that finds all multiples of 2 in a list
Requirements:
Return a new list with True or False, depending on whether the integer at the same position in the original list is a multiple of 2
The new list should have the same size as the original list
You are not allowed to import any module

ALGORITHM
Create file 10-divisible_by_2.py
Create function def divisible_by_2(my_list=[])
Create new list using list comprehension that checks if element of my_list is even
If yes then insert true
Else insert false
Return new list


11. Delete at
Write a function ‘def delete_at(my_list=[], idx=0)’ that deletes the item at a specific position in a list 
Requirements:
If idx is negative or out of range, return original list
You are not allowed to use pop()
You are not allowed to import any module

ALGORITHM
Create file 11-delete_at.py
Create function def delete_at(my_list=[], idx = 0)
Create condition to check if idx is out of range
If yes return the original list else continue
Delete the specific value at that index
Return the list



