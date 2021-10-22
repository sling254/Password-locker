from credentials import Credential
import  unittest

class TestCredential(unittest.TestCase):
    '''
    Test class that defines test cases for the credentials class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        self.new_credential = Credential("facebook","k11","qwerty")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credential.credential_list = []
    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credential.account_name,"facebook")
        self.assertEqual(self.new_credential.username,"k11")
        self.assertEqual(self.new_credential.password,"qwerty")

    
    

        





    
if __name__ == '__main__':
    unittest.main()

        