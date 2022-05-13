# lyft-interview-test: A String Cutting Python Web Application
__________________________________________________________________________________________________________________________________________________________
This repository houses a Flask API written in Python. The API's purpose is to receive POST requests with a string (any string) and return a JSON object with the key "return_string" and a string containing every third letter from the original string supplied with the POST request. 


# Set-up
__________________________________________________________________________________________________________________________________________________________

* Note: you need to have Python version 3.8.2 or higher installed on you computer prior to running any of the following commands.

1. Clone the repository to your local directory
2. Navigate to the cloned repository via your terminal/command line 
3. Run `pip install -r requirements.txt` to make sure that you have the required Python libraries/packages installed.
4. Activate the web application by typing `python app.py`
5. In a new window on your terminal/command line, type the following command: `curl -X POST http://127.0.0.1:5000/test --data '{"string_to_cut": "iamyourlyftdriver"}' -H 'Content-Type: application/json'` to provide a POST request. This command will return a JSON object with "return_string" as the key and a string containing every third letter as the corresponding value. Example output:
{
  "return_string": "muydv"
}

NOTE: the default string provided to the web application is 'iamyourlyftdriver'. You can supply your desired string by chainging just this string (i.e. "iamyourlyftdriver") in the curl command. 

