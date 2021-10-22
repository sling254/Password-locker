class Credential:
    """
    a class that creates new credentials 
    """
    credential_list = []

    def __init__(self, account_name,username, password):
        '''
        __init__ method that helps us define properties for our objects.

        Args:
            credential_name: New credential credential_name.
            password : New credential password.
            number: New contact phone number.
        '''
        self.account_name = account_name        
        self.username =username
        self.password = password



    def save_credential(self):
        '''
        save_credential method saves credential object into the credential_list
        '''
        Credential.credential_list.append(self)

    
    def delete_credential(self):
        '''
        delete_credential method deletes a saved credential from the credential_list
        '''
        Credential.credential_list.remove(self)

    @classmethod
    def find_credential_by_account_name(cls,account_name):
        '''
        Method that takes in a account_name and returns a credential that matches that account_name.
        Args:
        account_name:account_name to search for
        Returns:
        credential  that matches the account_name.
        '''
        for credential in cls.credential_list:
            if credential.account_name == account_name:
                return credential


    @classmethod
    def credential_exist(cls,account_name):
        '''
        Method that checks if a credential exists from the credential list.
        Args:
            account_name: account_name to search if it exists
        Returns :
            Boolean: True or false depending if the credential exists
        '''
        for credential in cls.credential_list:
            if credential.account_name == account_name:
                return True

        return False