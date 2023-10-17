#0x0D. SQL - Introduction#
##Learning Objectives##
1.What is a database
2.What is a relational database
3.What does SQL stand for
4.What is MySQL
5.How to create a database in MySQL
6.What does DDL and DML stand for
7.How to CREATE or ALTER a table
8.How to SELECT data from a table
9.How to INSERT, UPDATE or DELETE data
10.What are subqueries?
11.How to use MySQL functions

##Tasks##
###0. List databases###

Write a script that lists all databases of  your MySQL server.

###1. Create a database###
Write a script that creates the database hbtn_0c_0 in your MySQL server.
Requirements
If the database hbtn_0c_0 already exists, your script should not fail
You are not allowed to use the SELECT or SHOW statements

###2. Delete a database###
Write a script that deletes the database htbn_0c_0 in your MySQL server.
Requirements
If the database hbtn_0c_0 doesn’t exist, your script should not fail
You are not allowed to use the SELECT or SHOW statements

###3. List tables###
Write a script that lists all the tables of a database in your MySQL server.
Requirement
The database name will be passed as argument of mysql command (in the following example: mysql is the name of the database)

###4. First table###
Write a script that creates a table called first_table in the current database in your MySQL server. The first_table should have id INT and name VARCHAR(256).
Requirement
The database name will be passed as an argument of the mysql command.
If the table first_table already exists, your script should not fail.
You are not allowed to use the SELECT or SHOW statements

###5. Full description###
Write a script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server.
Requirement
The database name will be passed as an argument of the mysql command
You are not allowed to use the DESCRIBE or EXPLAIN statements

###6. List all in table###
Write a script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server.
Requirement
All fields should be printed
The database name will be passed as an argument of the mysql command

###7. First add###
Write a script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server. The new row should have id = 89 with name = Best School.
Requirements
The database name will be passed as an argument of the mysql command

###8. Count 89###
Write a script that displays the number of records with id = 89 in the table “first_table” of the database “hbtn_0c_0” in your MySQL server.
Requirement
The database name will be passed as an argument of the mysql command

###9. Full creation###
Write a script that creates a table “second_table” in the database “hbtn_0c_0” in your MySQL server and add multiple rows. The second_table description should be id INT, name VARCHAR(256), score INT.
Requirement
The database name will be passed as an argument to the mysql command
If the table “second_table” already exists, your script should not fail
You are not allowed to use the SELECT and SHOW statements
Your script should create these records: id 1 name John score 10, id 2 name Alex score 3, id 3 name Bob score 14, id 4 name George score 8.

###10. List by best###
Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.
Requirement
Results should display both the score and the name (in this order)
Records should be ordered by score (top first)
The database name will be passed as an argument of the mysql command

###11. Select the best###
Write a script that lists all records with a “score >= 10” in the table “second_table” of the database “hbtn_0c_0” in your MySQL server.
Requirement
Results should display both the score and the name (in this order)
Records should be ordered by score (top first)
The database name will be passed as an argument of the mysql command

###12. Cheating is bad###
Write a script that updates the score of Bob to 10 in the table “second_table”
Requirement
You are not allowed to use Bob’s id value, only the name field
The database name will be passed as an argument of the mysql command

###13. Score too low###
Write a script that removes all records with a “score <= 5” in the table “second_table” of the database “hbtn_0c_0” in your MySQL server.
Requirement
The database name will be passed as an argument of the mysql command

###14. Average###
Write a script that computes the score average of all records in the table “second_table” of the database “hbtn_0c_0” in your MySQL server.
Requirements
The results column name should be “average”
The database name will be passed as an argument of the mysql command

###15. Number by score###
Write a script that lists the number of records with the same score in the table “second_table” of the database “hbtn_0c_0” in your MySQL server. The result should display the score and the number of records for this score with the label number. 
Requirement
The list should be sorted by the number of records (descending)
The database name will be passed as an argument to the mysql command

###16. Say my name###
Write a script that lists all records of the table “second_table” of the database “hbtn_0c_0” in your MySQL server. 
Requirement
Don’t list rows without a name value
Results should display the score and the name (in this order)
Records should be listed by descending score
The database name will be passed as an argument to the mysql command

