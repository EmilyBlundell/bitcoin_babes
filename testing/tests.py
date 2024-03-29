import unittest

"""
The unittest is done to test the API endpoints if its up and running. 
If its running, the test passes, if not, it fails.
"""
URL = 'http://127.0.0.1:5000'
BEST_WORSE = 'http://127.0.0.1:5000/leader/selection'
NEW_TRADER = 'http://127.0.0.1:5000/new'
USER_ID = 'http://127.0.0.1:5000/user/investor_id'
ALL_INVESTORS = 'http://127.0.0.1:5000/allinvestors'

class BasicTests(unittest.TestCase):

    def test_landing_page(self):
        """Get landing page"""
        response = requests.get(URL)
        if response.ok:
            return response
        else:
            return None

    def test_best_worse(self):
        """Getting best and worse trader"""
        response = requests.get(BEST_WORSE)
        if response.ok:
            return response
        else:
            return None

    def test_add_trader(self):
        response = requests.put(NEW_TRADER)
        if response.ok:
            return response
        else:
            return None
    
    def test_investor_id(self):
        response = requests.put(USER_ID)
        if response.ok:
            return response
        else:
            return None

    def test_all_investors(self):
        response = requests.put(ALL_INVESTORS)
        if response.ok:
            return response
        else:
            return None

if __name__ == "__main__":
    unittest.main()
