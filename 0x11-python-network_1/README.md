# 0x11. Python - Network #1
## Learning Objectives
How to fetch internet resources with the Python package urllib
How to decode urllib body response
How to use the Python package requests 
How to make HTTP GET request
How to make HTTP POST / PUT / etc. request
How to fetch JSON resources
How to manipulate data from an external service


## Tasks
0. What's my status? #0
Write a Python script that fetches  https://alx-intranet.hbtn.io/status
Requirements
You must use the package urllib
You are not allowed to import any packages other than urllib

1. Response header value #0
Write a Python script 1-hbtn_header.py that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response. The value of this variable is different for each request. 
Requirements
You must use the packages urllib and sys
You are not allowed to import packages other than urllib and sys
You must use a with statement

2. POST an email #0
Write a Python script 2-post_email.py that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8). Your email must be sent in the email variable. 
Requirements
You must use the packages urllib and sys
You are not allowed to import packages other than urllib and sys

3. Error code #0
Write a Python script 3-error_code.py that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8). You have to manage urllib.error.HTTPError exceptions and print Error code: followed by the HTTP status code.
Requirements
You must use the packages urllib and sys
You don’t need to check arguments passed to the script

4. What's my status? #1
Write a Python script 4-hbtn_status.py that fetches https://alx-intranet.hbtn.io/status. You must use the package requests.
Requirement
You must use the package requests
You are not allowed to import packages other than requests
The body of the response must be displayed like the following example
guillaume@ubuntu:~/0x11$ ./4-hbtn_status.py | cat -e
Body response:$
    - type: <class 'str'>$
    - content: OK$
guillaume@ubuntu:~/0x11$

5. Response header value #1
Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header. 
Requirements
You must use the packages requests and sys
You don’t need to check script arguments (number and type)

6. POST an email #1
Write a python script 6-post_email.py that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response. The email must be sent in the variable email. 
Requirements
You must use the packages requests and sys
You don’t need to check arguments passed to the script

7. Error code #1
Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response. If the HTTP status code is greater than or equal to 400, print: Error code: followed by the value of the HTTP status code.
Requirements
You must use the packages requests and sys
You don’t need to check arguments passed to the script

8. Search API
Write a Python script 8-json_api.py that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter. The letter must be sent in the variable q. If no argument is given, set q=””. If the response body is properly JSON formatted and not empty, display the id and name like this: [<id>]<name>. Otherwise display Not a valid JSON if the JSON is invalid or display No result if the JSON is empty.
Requirements
You must use the package requests and sys
You are not allowed to import packages other than requests and sys

9. My GitHub!

Write a Python script 10-my_github.py that takes your GitHub credentials (username and password) and uses the GitHub API to display your id. You must use Basic Authentication with a personal access token as password to access your information (only read:user permission is needed). The first argument will be your username. The second argument will be your password. 
Requirements
You must use the package requests and sys
You don’t need to check arguments passed to the script (number or type)
