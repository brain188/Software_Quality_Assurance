import unittest  
from App import app  

class TestApp(unittest.TestCase):  
    def setUp(self):  
        self.app = app.test_client()  

    def test_home_route(self):  
        response = self.app.get('/')  
        
        print(f"Status Code: {response.status_code}")  
        print(f"Response Data: {response.data}")  
        print(f"Content-Type: {response.content_type}")  
        
        self.assertEqual(response.status_code, 200)  
        # Expecting a JSON response  
        self.assertEqual(response.get_json(), {"message": "Hello, I am a level 400 student, this is software quality tools"})  

if __name__ == '__main__':  
    unittest.main()