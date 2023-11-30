# 0x10. Python - Network #0
## Learning Objectives
What is a URL
What is HTTP
How to read a URL
What is the scheme for an HTTP URL
What is a domain name
What is a sub-domain
How to define a port number in a URL
What is a query string
What is an HTTP response
What is an HTTP request
What is an HTTP header
What is the HTTP message body
What is the HTTP request method
What is the HTTP response status code
What is the HTTP cookie
How do you request with cURL
What happens when you type google.com in your browser

## Tasks
0. cURL body size
Write a Bash script 0-body_size.sh that takes in a URL, sends a request to that URL, and displays the size of the body of the response. The size must be displayed in bytes. 
Requirement
You have to use curl

1. cURL to the end
Write a Bash script 1-body.sh that takes in a URL, sends a GET request to the URL, and displays the body of the response. 
Requirement
You should display only body of a 200 status code response
You have to use curl

2. cURL Method
Write a Bash script 2-delete.sh that sends a DELETE request to the URL passed as the first argument and displays the body of the response.
Requirement
You have to use curl

3. cURL only methods
Write a Bash script 3-methods.sh that takes in a URL and displays all HTTP methods the server will accept.
Requirements
You have to use curl

4. cURL headers
Write a Bash script 4-header.sh that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response. A header variable “X-School-User-Id” must be sent with the value 98.
Requirement
You have to use curl

5. cURL POST parameters
Write a Bash script 5-post_params.sh that takes in a URL, sends a POST request to the passed URL, and displays the body of the response. A variable email must be sent with the value test@gmail.com. A variable subject must be sent with the value I will always be here for PLD.
Requirement
You have to use curl

