# 0x15. JavaScript - Web jQuery
## Learning Objectives
Why did JQuery make front-end programming so easy?
How to select HTML elements in JavaScript
How to select HTML elements with JQuery
What are the differences between ID, class and tag name selectors
How to modify an HTML element style
How to get and update an HTML element content
How to modify the DOM
How to make a GET request with JQuery Ajax
How to make a POST request with JQuery Ajax
How to listen/bind to DOM events

## Requirements
Allowed editors: vi, vim, emacs
All your files will be interpreted on Chrome
All your files should end with a new line
A README.md file, at the root of the folder of the project, is mandatory
Your code should be “semistandard” compliant with the flag –global $
You must use JQuery version 3.x
You are not allowed to use var
HTML should not reload for each action: DOM manipulation, update values, fetch data …

## Tasks
0. No JQuery
Write a JavaScript 0-script.js that updates the text color of the <header> element to red (#FF0000). 
Requirements
You must use document.querySelector to select the HTML tag
You can’t use the JQuery API

1. With JQuery
Write a JavaScript 1-script.js script that updates the text color of the <header> element to red (#FF0000)
Requirements
You can’t use document.querySelector to select the HTML tag
You must use the JQuery API

2. Click and turn red
Write a JavaScript 2-script.js script that updates the text color of the <header> element to red (#FF0000) when the user clicks on the tag DIV#red_header.
Requirement
You can’t use document.querySelector to select the HTML tag
You must use the JQuery API

3. Add `.red` class
Write a JavaScript 3-script.js script that adds the class red to the <header> element when the user clicks on the tag ‘DIV#red_header’.
Requirement
You can’t use document.querySelector to select the HTML tag
You must use the JQuery API

4. Toggle classes
Write a JavaScript 4-script.js script that toggles the class of the <header> element when the user clicks on the tag DIV#toggle_header.
Requirements
The <header> element must always have one class: red or green, never both at the same time and never empty.
If the current class is red, when the user clicks on DIV#toggle_header, the class must be updated to green; and the reverse.
You can’t use document.querySelector to select the HTML tag.
You must use the JQuery API

5. List of elements
Write a JavaScript 5-script.js script that adds a <li> element to a list when the user clicks on the tag DIV#add_item.
Requirement
The new element must be: <li>Item</li>
The new element must be added to UL.my_list
You can’t use document.querySelector to select the HTML tag
You must use the JQuery API

6. Change the text
Write a JavaScript script 6-script.js that updates the text of the <header> element to New Header!!! When the user clicks on DIV#update_header
Requirements
You can’t use document.querySelector to select the HTML tag
You must use the JQuery API

7. Star wars character
Write a JavaScript 7-script.js script that fetches the character ‘name’ from this URL: https://swapi-api.alx-tools.com/api/people/5/?format=json
Requirement
The name must be displayed in the HTML tag DIV#character
You can’t use document.querySelector to select the HTML tag
You must use the JQuery API

8. Star Wars movies
Write a JavaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json
Requirements
All movie titles must be listed in the HTML tag ‘UL#list_movies’
You can’t use document.querySelector to select the HTML tag
You must use the JQuery API

9. Say Hello!
Write a JavaScript script that fetches from URL:https://hellosalut.stefanbohacek.dev/?lang=fr  and displays the value of ‘hello’ from that fetch in the HTML tag ‘DIV#hello’.
Requirements
The translation of ‘hello’ must be displayed in the html tag ‘DIV#hello’.
You can’t use document.querySelector to select the HTML tag
You must use the JQuery API
Your script must work when it is imported from the <head> tag

