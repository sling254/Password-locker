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

    
    def test_save_credentials(self):
        '''
        test_save_multiple_contact to check if we can save multiple contact
        objects to our contact_list
        '''

        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),1)

    def test_save_multiple_credentials(self):
        '''
        test_save_multiple_contact to check if we can save multiple Credentials
        objects to our credential_list
        '''
        self.new_credential.save_credential()
        test_credential = Credential("Twitter","user1","ytrewq") 
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),2)

        





    
if __name__ == '__main__':
    unittest.main()

        