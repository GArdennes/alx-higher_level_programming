# 0x14. JavaScript - Web scraping
## Learning Objectives
How to manipulate JSON data
How to use request and fetch API
How to read and write a file using fs module
Callback functions are to Javascript as lambda functions are to python? 

## Requirements
Allowed editors: vi, vim, emacs
All your files will be interpreted on Ubuntu 20.04 LTS using node (version 14.x)
All your files should end with a new line
The first line of all your files should be exactly “#!/usr/bin/node”
A README.md file, at the root of the folder of the project, is mandatory
Your code should be semistandard compliant.
All your files must be executable
The length of your files will be tested using “wc”
You are not allowed to use “var”

## Tasks
0. Readme
Write a script 0-readme.js that reads and prints the content of a file. The first argument is the file path. The content of the file must be in “utf-8”. If an error occurred during the reading, print the error object.

1. Write me
Write a script 1-writeme.js that writes a string to a file. The first argument is the file path. The second argument is the string to write. The content of the file must be written in ‘utf-8’. If an error occurred during writing, print the error object.

2. Status code
Write a script 2-statuscode.js that displays the status code of a GET request. The first argument is the URL to request (GET). The status code must be printed like this: “code: <status code>”. You must use the module “request”.

3. Star wars movie title
Write a script 3-starwars_title.js that prints the title of a Star Wars movie where the episode number matches the given integer. The first argument is the movie ID. 
Requirements
You must use the <link: Star wars API> with the endpoint https://swapi-api.alx-tools.com/api/films/:id
You must use the module request

4. Star wars Wedge Antilles
Write a script 4-starwars_count.js that prints the number of movies where the character “Wedge Antilles” is present. The first argument is the API URL of the <link: Star wars API>: https://swapi-api.alx-tools.com/api/films/. Wedge Antilles is character ID 18, your script must use this ID for filtering the result of the API. You must use the module request.

5. Loripsum
Write a script 5-request_store.js that gets the contents of a webpage and stores it in a file. The first argument is the URL to request. The second argument is the file path to store the body response. 
Requirements
The file must be UTF-8 encoded
You must use the module request

6. How many completed?
Write a script 6-completed_tasks.js that computes the number of tasks completed by user id. The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
Requirements
You must only print users with completed task
You must use the module request

7. Who was playing in this movie?
Write a script 100-starwars_characters.js that prints all characters of a Star Wars movie. The first argument is the Movie ID - example: 3 = “Return of the Jedi”. Display one character name by line. 
Requirements
You must use the <link: Star wars API>
You must use the module request

8. Right order
Write a script 101-starwars_characters.js that prints all characters of a Star Wars movie. The first argument is the Movie ID - example: 3 = “Return of the Jedi”. Display one character name by line in the same order of the list “characters” in the /films/ response.
Requirements
You must use the Star wars API
You must use the module request
