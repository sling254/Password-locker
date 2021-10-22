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