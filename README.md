### What this project is for?
This project uses the following API endpoint https://jsonplaceholder.typicode.com/

The scripts therein does the following:
- Does a GET request to the /users endpoint.
- Validates the response code to be 200.
- Validates the response time to be less than 200ms.
- Iterates over all elements of the json response body and print out all company names ending in “ Group”.

### Pre-requisites
1. Clone the repository
```bash
$ git clone https://github.com/jaymutuku/python-api-tests
```
```bash
$ cd to python-api-tests/
```

#### Create and Activate a Virtual Environment
```bash
$ pip3 install virtualenv
$ virtual -p python3 venv 
$ source venv/bin/activate
```
Incase you get an error in the second step above:
command 'virtualenv' not found ...
Then
```bash
$ sudo apt install virtualenv
```
#### Install the required packages
```bash
$ pip install requests ijson
```
You don't need to install the unittest library is a built-in library.

#### Save the dependencies to _requirements.txt_
```bash
$ pip freeze > requirements.txt
```
### How do I run the project?

2. Discover and run the tests!
```bash
$ python -m unittest discover
```
3. Expected Output
```bash
Company Name: Johns Group
Company Name: Abernathy Group
.Response Status: 200
.Response Time: 0.478977
F
======================================================================
FAIL: test_response_time (users_test.test_users.APITests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/<username>/Desktop/humanitec/answers/python-api-tests/users_test/test_users.py", line 20, in test_response_time
    self.assertLess(responseTime,0.2)
AssertionError: 0.478977 not less than 0.2

----------------------------------------------------------------------
Ran 3 tests in 1.587s

FAILED (failures=1)

```