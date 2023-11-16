## 0x0F. Python - Object-relational mapping
### Learning Objectives
How to connect to a MySQL database from a Python script
How to SELECT rows in a MySQL table from a Python script
How to INSERT rows in a MySQL table from a Python script
What ORM means
How to map a Python Class to a MySQL table
How to create a Python Virtual Environment

### Tasks
0. Get all states
Write a script 0-select_states.py that lists all states from the database hbtn_0e_0_usa. Results must be sorted in ascending order by states.id.
Requirements
Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed).
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Your code should not be executed when imported.

1. Filter states
Write a script 1-filter_states.py that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa. Results must be sorted in ascending order by states.id. Results must be displayed as they are in the example below. 
Requirements
Your script should take 3 arguments: mysql_username, mysql_password and database_name (no argument validation needed).
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Your code should not be executed when imported.

2. Filter states by user input
Write a script 2-my_filter_states.py that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. Results must be sorted in ascending order by states.id. Results must be displayed as they are in the example below.
Requirements
Your script should take 4 arguments: mysql_username, mysql_password, database_name and states_name_searched (no argument validation needed)
Your must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
You must use format to create the SQL query with the user input
Your code should not be executed when imported

3. SQL Injection...
Wait, do you remember the previous task? Did you test "Arizona"; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = "" as an input?
Once again, write a script 3-my_safe_filter_states.py that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where the name matches the argument. But this time, write one that is safe from MySQL injections! Results must be sorted in ascending order by states.id. Results must be displayed as they are in the example below.
Requirements
Your script should take 4 arguments: mysql username, mysql password, database name and state name searched (safe from MySQL injection)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306

4. Cities by states
Write a script 4-cities_by_state.py that lists all cities from the database hbtn_0e_4_usa. Results must be sorted in ascending order by cities.id. Results must be displayed as they are in the example below.
Requirement
Your script should take 3 arguments: mysql username, mysql password and database name
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
You can use only execute() one.
Your code should not be executed when imported

5. All cities by state
Write a script 5-filter_cities.py that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa. Results must be sorted in ascending order by cities.id. The results must be displayed as they are in the example below.
Requirements.
Your script should take 4 arguments: mysql username, mysql password, database name and state name (SQL injection free!)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
You can use only execute() once
Your code should not be executed when imported

6. First state model
Python file that contains the class definition of a State and an instance "Base = declarative_base()". State class inherits from Base. Links to the MySQL table states. Class attribute id that represents a column of an auto-generated, unique integer, can not be null and is a primary key. Class attribute name that represents a column of a string with maximum 128 characters and can not be null.
Requirement
You must use the module SQLAlchemy
Your script should connect to a MySQL server running on localhost at port 3306.
WARNING: all classes who inherit from Base must be imported before calling Base.metadata.create_all(engine)

7. All states via SQLAlchemy
Write a script 7-model_state_fetch_all.py that lists all State objects from the database hbtn_0e_6_usa. Results must be sorted in ascending order by states.id. The results must be displayed as they are in the example below.
Requirements
Your script should take 3 arguments: mysql username, mysql password and database name
You must use the module SQLAlchemy
You must import State and Base from model_state - from model_state import Base, State
Your script should connect to a MySQL server running on localhost at port 3306
Your code should not be executed when imported

8. First state

9. Contains `a`
Write a script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa. Results must be sorted in ascending order by states.id. The results must be displayed as they are in the example below.
Requirements
Your script should take 3 arguments: mysql username, mysql password and database name
You must use the module SQLAlchemy
You must import State and Base from model_state - from model_state import Base, State
Your script should connect to a MySQL server running on localhost at port 3306.
Your code should not be executed when imported

10. Get a state
Write a script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa. Results must display the states.id. If no state has the name you searched for, display "Not found".
Requirement
Your script should take 4 arguments: mysql username, mysql password, database name and state name to search (SQL injection free)
You must use the module SQLAlchemy
You must import State and Base from model_state - from model_state import Base, State
Your script should connect to a MySQL server running on localhost at port 3306
You can assume you have one record with the state name to search
Your code should not be executed when imported

11. Add a new state
Write a script that adds the State object "Louisiana" to the database hbtn_0e_6_usa. Print the new states.id after creation.
Requirement
Your script should take 3 arguments: mysql username, mysql password and database name
You must use the module SQLAlchemy
You must import State and Base from model_state - from model_state import Base, State
Your script should connect to a MySQL server running on localhost at port 3306
Your code should not be executed when imported

12. Update a state
Write a script that changes the name of a State object from the database hbtn_0e_6_usa. Change the name of the State where id=2 to New Mexico. 
Requirement
Your script should take 3 arguments: mysql username, mysql password and database name
Your must use the module SQLAchemy
You must import State and Base from model_state - from model_state import Base, State
Your script should connect to a MySQL server running on localhost at port 3306
Your code should not be executed when imported

13. Delete states
Write a script that deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa.
Requirement
Your script should take 3 arguments: mysql username, mysql password and database name
You must use the module SQLAlchemy
You must import State and Base from model_state - from model_state import Base, State
Your script should connect to a MySQL server running on localhost at port 3306
Your code should not be executed when imported

14. Cities in state
Write a Python file similar to model_state.py named model_city.py that contains the class definitions of a City. City class inherits from Base (imported from model_state). Links to the MySQL table cities. Class attribute id that represents a column of an auto-generated, unique integer, can not be null and is a primary key. Class attribute name that represents a column of a string of 128 characters and can not be null. Class attribute state_id that represents a column of an integer, can not be null and is a foreign key  to states.id. 

Write a script 14-model_city_fetch_by_state.py that prints all City objects from the database hbtn_0e_14_usa. Results must be sorted in ascending order by cities.id. Results must be displayed as they are in the example below(<state name>: (<city id>)<city name>).
