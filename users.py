"""
__author_ = "Josphat Mutuku"
__email__ = "mutuku.josphat@gmail.com"
__date__ ="2019-07-03"

"""

import requests
import unittest
import ijson

USERS_URL = 'http://jsonplaceholder.typicode.com/users'

def get_users():
    # Do a GET request to the /users endpoint
    response = requests.get(USERS_URL)
    if response.ok:        
        return response
    else:
        return None

def parse_json(json_filename):
    with open(json_filename, 'rb') as input_file:
        # load json iteratively
        parser = ijson.parse(input_file)
        for prefix, event, value in parser:
            print('prefix={}, event={}, value={}'.format(prefix, event, value))
 
 
def extract_company_names(json_filename):
    
    with open(json_filename, 'rb') as input_file:       
        company_names = ijson.items(input_file, 'item.company.name')         
        for name in company_names:
            if name.endswith('Group'):
                print('Company Name: {}'.format(name))
                    