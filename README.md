# lyft-interview-test: A String Cutting Python Web Application
__________________________________________________________________________________________________________________________________________________________
This repository houses a Flask API written in Python. The API's purpose is to recive POST requests with a string (any string) and return a JSON object with the key "return_string" and a string containing every third letter from the original string supplied with the POST request. 


# Set-up
__________________________________________________________________________________________________________________________________________________________

1. Clone the repository to your local directory
2. Navigate to the cloned repository via your terminal/command line 
3. Type the following command in the command line: `curl -X POST http://127.0.0.1:5000/test --data '{"string_to_cut": "iamyourlyftdriver"}' -H 'Content-Type: application/json'`

NOTE: the default string provided to the web application is 'iamyourlyftdriver'. You can supply your desired string by chainging this string in the curl command printed in part 3. 

