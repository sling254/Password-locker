import unittest
from user import  User

class UserTestCreate(unittest.TestCase):
    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        This method is responsible for setting up an intialy state before each test begin
        '''
        self.user = User("emanuel", "12345", "e@mail.com")

    def tearDown(self):
        '''
        This method is responsible for resetting the test env back to intial state
        '''
        self.user_list = []
        self.user_list.append(self.user)



    def test_init(self):
        '''
        A test to check if the class is beign intialized correctly
        '''
        self.assertEqual(self.user.username,"emanuel")
        self.assertEqual(self.user.password,"12345")
        self.assertEqual(self.user.email,"e@mail.com")

    def test_user(self):
        '''
        A test to check if the the save function saves the values
        '''
        self.assertEqual(len(self.user_list), 1)

