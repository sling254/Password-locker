#!/usr/bin/env python3.6
from user import User
from credentials import Credential
import string, random

#functions for user_account
def create_user(username,password,email):
  '''
  Function to create a new user
  '''
  new_user = User(username,password,email)
  return new_user

def save_user(user):
    '''
    save the user
    '''
    return user.save_user()

def del_user(user):
  '''
  Function to delete a user
  '''
  user.delete_user()

def find_user(username):
  '''
  Function that finds a user by username and returns the user
  '''
  return User.find_by_username(username)

def check_existing_user(username):
  '''
  Function that check if user exists with username and returns a Boolean
  '''
  return User.user_exists(username)

def display_users():
  '''
  Function that returns all the saved users
  '''
  return User.display_user()

#Functions for user credentials
def create_credential(account_name,username,password):
  '''
  Function to create a new credential
  '''
  new_credential = Credential(account_name,username,password)
  return new_credential

def save_credential(credential):
  '''
  Function to save credential
  '''
  credential.save_credential()

def del_credential(credential):
  '''
  Function to delete a credential
  '''
  credential.delete_credential()

def find_credential(account_name):
  '''
  Function that finds a credential by account_name and returns the credential
  '''
  return Credential.find_credential_by_account_name(account_name)

def check_existing_credential(account_name):
  '''
  Function that check if credential exists with account_name and returns a Boolean
  '''
  return Credential.credential_exist(account_name)

def display_credentials():
  '''
  Function that returns all the saved credentials
  '''
  return Credential.display_credentials()


# A function to generate password
def pass_gen():
  print("+++++++++++++++++++++++++++++++")
  print("Welcome to Password Generator")
  phrase = string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation
  while True:
    try:
        length = int(input("please Key in the lenght of the password you need: "))
        password = random.sample(phrase, length)
    except ValueError:
        print("You did not key in a valid number")
        continue
    else:
      password = ("".join(password))
      return password 
  


def main():
  print("Hello, Welcome to your password locker account \n")
  print("short_codes to help you around: to create an account use: cc \n")

  while True:
    short_code = input().lower()

    #user creating own password
    if short_code == 'cc':
      print("New user Account")
      print("-"*10)

      print ("Enter your a preferred username ....")
      username = input()
      print("-"*10)
      print ("Enter password  ....")
      password = input()
      print("-"*10)

      print ("Enter your email address ....")
      email = input()
      print("-"*10)
      print("-"*10)

    
      save_user(create_user(username, password,email)) #create and save user
      print(f"New user created with \n User name -- {username} \n User Email -- {email} ")
      print("-"*70)
      
      print("Enter command login -to login to your account \n")
    #Login code
    if short_code == 'login':
      print("Welcome to login Interface")
      print("Enter your username")
      input_user_name = input()

      print("Enter your password")
      input_user_password = input()
      print("-"*10)
      print("-"*60)
      if  input_user_name != username or input_user_password != password:
        print("ACCESS DENIED!!")
        print("Invalid username or password!!!!")
        print("Try again")
        print("\/"*20)
        print("Enter command login to re-try login to your account \n")
            
      else:
        print("ACCESS GRANTED!!")
        print(f"Welcome {username} {email} to your account")
        print("Option 1 >>> To save account credentials for account that exists  use code * ca *")
        print("Option 2 >>> To save account credentials for account you wish to create and have a password generated for you use code * ca-g *")
    if short_code == 'ca':             
        print ("Enter your a account name you wish to store credentials for ....")
        acc_name = input()
        print("-"*10)
        print ("Enter your username for the  account ....")
        acc_username = input()
        print("-"*10)
        print ("Enter Password for the  account ....")
        password = input()
        print("-"*10)
        save_credential(create_credential(acc_name, acc_username,password)) #
        print("Thank you for using our service")
        print("-"*70)
        print("To view your credentials account credentials use code * display-c * to display all saved accounts")

    if short_code == 'ca-g':
      print ("Enter your a account name you wish to store credentials for ....")
      acc_name = input()
      print("-"*10)
      print ("Enter your username for the  account ....")
      acc_username = input()
      print("-"*10)
      print ("Enter Password for the  account ....")
      password=pass_gen()
      print(f">>>> you password is {password}")
      print("-"*10)
      save_credential(create_credential(acc_name, acc_username,password)) #
      print("Thank you for using our service")
      print("-"*70)

    if short_code == "display-c":
      print("-"*70)
      display_credentials()
      print("Here is a list of all your credentials")
      print("-"*70)
      print("To delete credental account use code * delete-c * ")

    if short_code == "delete-c":
      print("Enter the account-name you want to delete  ")
      delete_acc = input()
      print("-"*10)
      print("-"*60)
      if check_existing_credential(delete_acc):
        dl_acc = find_credential(delete_acc)
        print(f"<<{dl_acc.account_name}>> with Username <<{dl_acc.username}>> will be deleted")
        dl_acc = del_credential(dl_acc)
        print("Credential deleted successfully")
      else:
        print("That account name does not exist")


      
      
          




      

   

if __name__ == '__main__':

  main()


   