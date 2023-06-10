import unittest

from users import get_users,parse_json,extract_company_names

class APITests(unittest.TestCase):     
    
    # Validate the response to be 200 OK
    def test_response_status(self):
        response = get_users()
        print('Response Status: {}'.format(response.status_code))        
        self.assertEqual(response.status_code, 200)
        
        
    #  Validate the response to be less than 200ms
    def test_response_time(self):       
        responseTime = get_users().elapsed.total_seconds()        
        
        print('Response Time: {}'.format(responseTime))        
            # 200milliseconds = 0.2 seconds        
        self.assertLess(responseTime,0.2)
        
    """ Iterate over all elements of the json response body 
        & print out company names ending in "Group"
    """   
    def test_print_company_names_ending_with_group(self):     
       
        # write response to a binary file
        with open('./users.json', mode='wb') as json_filename:
            json_filename.write(get_users().content)

            json_filename.close()

            extract_company_names('./users.json') 

            # results = extract_company_names('./users.json')       

            # self.assertIsNotNone(results) 

if __name__ == "__main__":
    unittest.main()



