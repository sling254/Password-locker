#!/usr/bin/env python3.6
class User:
    '''
    Class that creates a new instance of a user
    '''
    user_list = [] #store the users
    def __init__(self, username, password, email):
        '''
        __init__ method that helps us define properties for our objects.

        Args:
            username: New user username.
            password : New user password.
            email : New user email.
        '''

        self.username = username
        self.password = password
        self.email = email

    def save_user(self):
        '''
        save the user
        '''
        User.user_list.append(self)

    def delete_user(self):
        '''
        delete user
        '''
        User.user_list.remove(self)

    @classmethod
    def find_by_username(cls, username):
        '''
        Method that takes in a username and returns a user that matches that username.
        Args:
        number:username to search for user
        Returns:
        User  that matches the username.
        '''
        for  user in cls.user_list:
            if user.username==username:
                return user

    @classmethod
    def user_exists(cls,username):
        '''
        Method that takes in a username and returns a true if the user with that username does exist.
        Args:
        username:username to search for user
        Returns:
        Boolean value of true if the username does exist.
        Boolean value of false if the username does not exist.
        '''
        for user in cls.user_list:
            if user.username==username:
                return True
            return False






if __name__ == '__main__':
    user = User("emanuel", "12345", "e@mail.com")
    User.save_user( user)
    


