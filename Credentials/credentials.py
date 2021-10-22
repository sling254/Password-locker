class Credential:
    """
    a class that creates new credentials 
    """
    credential_list = []

    def __init__(self, credential_name, password,number):
        '''
        __init__ method that helps us define properties for our objects.

        Args:
            credential_name: New credential credential_name.
            password : New credential password.
            number: New contact phone number.
        '''
        self.credential_name = credential_name
        self.password = password
        self.number = number