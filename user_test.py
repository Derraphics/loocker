import unittest #Importing the unittest module
from user import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the User class behaviors
    
    Arg:
        unittest.Testcase: A TestCase class that helps in creating test case classes
    '''

    def setUp(self):
        '''
        Set up method to run before each test case
        '''
        self.new_User = User("Derrick", "Derroh",  "derrick@gmail.com", "Derrick123")

    def test_init(self):
        '''
        test case to test if the object has been properly initialized
        '''

        self.assertEqual(self.new_User.first_name,"Derrick")
        self.assertEqual(self.new_User.last_name,"Derroh")
        self.assertEqual(self.new_User.user_email,"derrick@gmail.com")
        self.assertEqual(self.new_User.user_password,"Derrick123")

if __name__ == '__main__':
    unittest.main()

