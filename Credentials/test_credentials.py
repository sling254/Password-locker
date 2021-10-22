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

    def test_delete_credential(self):
        '''
        test_delete_credential to test if we can remove a credential from our credential list
        '''
        self.new_credential.save_credential()
        test_credential = Credential("Instagram","userTest","pope2020") #new credential
        test_credential.save_credential()

        self.new_credential.delete_credential() #Deleting a credential object
        self.assertEqual(len(Credential.credential_list),1)

        
    def test_find_credential_by_account_name(self):
        '''
        test to check if we can find a credential by account_name and display information
        '''

        self.new_credential.save_credential()
        test_credential = Credential("Instagram","UserTest","jnr345") #new credential
        test_credential.save_credential()

        found_credential = Credential.find_credential_by_account_name("Instagram")

        self.assertEqual(found_credential.account_name,test_credential.account_name)





    
if __name__ == '__main__':
    unittest.main()

        