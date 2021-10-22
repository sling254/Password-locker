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
        This method is responsible for resetting the test env back to intial state by destroying the listed properties
        '''
        User.user_list = [] 
    def test_init(self):
        '''
        A test to check if the class is beign intialized correctly
        '''
        self.assertEqual(self.user.username,"emanuel")
        self.assertEqual(self.user.password,"12345")
        self.assertEqual(self.user.email,"e@mail.com")

    def test_save_user(self):
        '''
        A test to check if the the save method saves the values
        '''
        self.user.save_user()
        self.assertEqual(len(User.user_list),1)

    def test_delete_user(self):
        '''
        A test to check if the delete method works 
        '''
        self.user.save_user()
        self.new_user = User("sling","7895", "sling@mail.com")
        self.new_user_2 = User("sling254","77895", "webd@mail.com")
        self.new_user_2.save_user()
        self.new_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),2)


    





    
if __name__ == '__main__':
    unittest.main()