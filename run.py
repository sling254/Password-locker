#!/usr/bin/env python3.6
from user import User
from credentials import Credential
import string, random
from rich import print 
from rich.console import Console
from rich.table import Table
from rich.progress import track
from time import sleep


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

def copy_username(account_name):
  '''
  Function that copies saved users
  '''
  return Credential.copy_username(account_name)

def copy_password(account_name):
  '''
  Function that copies saved password
  '''
  return Credential.copy_password(account_name)




# A function to generate password
def pass_gen():
  print("+++++++++++++++++++++++++++++++")
  print("Welcome to Password Generator")
  phrase = string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation
  while True:
    try:
        length = int(input(">>> please Key in the lenght of the password you need: "))
        password = random.sample(phrase, length)
    except ValueError:
        print("You did not key in a valid number")
        continue
    else:
      password = ("".join(password))
      return f" '{password}' "

#Function to display command to the user  
def display_commands():
  console = Console()
  table = Table(show_header=True, header_style="bold magenta")
  table.add_column("Short Code")
  table.add_column("Use for")
  table.add_row(
      "display-c", 
      "To display all saved accounts"
  )
  table.add_row(
    "delete-c",
    "To delete saved credentials"
  )
  table.add_row(
    "copy-user",
    "To copy a user to the clipboard"
  )
  table.add_row(
    "copy-pass",
    "To copy a password to the clipboard"
  )
  table.add_row(
    "exit",
    "To exit the program"
  )
  console.print(table)
  print("-"*60)

def main():
  print("[bold blue] >>> Hello, Welcome to your password locker  <<< \n")
  for step in track(range(30), description="Setting up..."):
          sleep(0.1)
  print(">>> To use this service you have to setup an account")
  console = Console()
  table = Table(show_header=True, header_style="bold magenta")
  table.add_column("Short Code")
  table.add_column("Use for")
  table.add_row(
      "cc ", 
      "To create an account this will take a second"
  )  
  console.print(table)
  print("-"*60)

  while True:
    short_code = input().lower()
    #user creating own password
    if short_code == 'cc':
      print(">>> New user Account <<<")
      print("-"*10)
      print (">>> Enter a preferred username ....")
      username = input()
      print("-"*10)
      print (">>> Enter password  ....")
      password = input()
      print("-"*10)
      print (">>> Enter your email address ....")
      email = input()
      print("-"*10)
      print("-"*10)
    
      save_user(create_user(username, password,email)) #create and save user
      print(f">>> New user created with \n [bold green] User name -- {username} \n User Email -- [bold green]{email} ")
      print("-"*70)
      print(f">>> Please proceed to login in ")
      console = Console()
      table = Table(show_header=True, header_style="bold magenta")
      table.add_column("Short Code")
      table.add_column("Use for")
      table.add_row(
          "login", 
          "To login to an account"
      )  
      console.print(table)
      print("-"*60)
      
    #Login code
    if short_code == 'login':
      print(">>> [bold blue]Welcome to login Interface <<<")
      print(">>> Enter your username")
      input_user_name = input()
      print(">>> Enter your password")
      input_user_password = input()      
      for step in track(range(5), description="Checking your credentials..."):
          sleep(0.1)
      print("-"*60)
      if  input_user_name != username or input_user_password != password:
        print(">>> [bold red] ACCESS DENIED!! [/bold red] <<<")
        print(">>> Invalid username or password!!!!")
        print(" >>> Try again")
        print("[bold red]\_/"*20)
        console = Console()
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Short Code")
        table.add_column("Use for")
        table.add_row(
            "login", 
            "To re-try login"
        )
        console.print(table)
        print("-"*60) 
            
      else:
        print(">>> [bold green] ACCESS GRANTED!! <<<")
        print(f"Welcome [bold green] >>> {username} <<< {email} [/bold green] to your account")
        console = Console()
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Short Codes")
        table.add_column("Use for")
        table.add_row(
            "ca", 
            "To save account credentials for account that exists"
        )
        table.add_row(
          "ca-g",
          "To save account credentials for account you wish to create and have a password generated for you use code"
        )
        console.print(table)
        print("-"*60) 
    if short_code == 'ca':             
        print (">>> Enter your a account name you wish to store credentials for ....")
        acc_name = input()
        print("-"*10)
        print (">>> Enter your username for the  account ....")
        acc_username = input()
        print("-"*10)
        print (">>> Enter Password for the  account ....")
        password = input()
        print("-"*10)
        save_credential(create_credential(acc_name, acc_username,password)) #
        print(">>> [bold blue]Thank you for using our service")
        print("-"*70)
        #Function to display command to the user
        display_commands()
        

    if short_code == 'ca-g':
      print (">>> Enter your a account name you wish to store credentials for ....")
      acc_name = input()
      print("-"*10)
      print (">>> Enter your username for the  account ....")
      acc_username = input()
      print("-"*10)
      print (">>> Enter Password for the  account ....")
      password=pass_gen()
      print(f">>>> you password is {password}")
      print("-"*10)
      save_credential(create_credential(acc_name, acc_username,password)) #
      print(">>>[bold blue] Thank you for using our service")
      print("-"*70)
      #Function to display command to the user
      display_commands()

    if short_code == "display-c":
      print("-"*70)
      print(">>> Here is a list of all your credentials")
      display_credentials()      
      print("-"*70)
      #Function to display command to the user
      display_commands()

    if short_code == "delete-c":
      print(">>> Enter the account-name you want to delete  ")
      delete_acc = input()
      print("-"*10)
      print("-"*60)
      if check_existing_credential(delete_acc):
        dl_acc = find_credential(delete_acc)
        print(f"<< {dl_acc.account_name} >> with Username << {dl_acc.username} >> will be deleted")
        dl_acc = del_credential(dl_acc)
        print(">>> [bold green]Credential deleted successfully")
      else:
        print("[bold red]That account name does not exist")
      #Function to display command to the user
      display_commands()

      #copy password 
    if short_code == 'copy-user':

      print(">>> Enter the Account name to copy the Username ")

      search_credential = input()
      print("-"*10)
      print("-"*60)
      if check_existing_credential(search_credential):
        search_credential = copy_username(search_credential)
        print("[bold green]Username copied successfully")

      else:
        print("[bold red]That Account-name does not exist")
      #Function to display command to the user
      display_commands()

    if short_code == 'copy-pass':

      print(">>> Enter the Account name to copy the Password ")

      search_credential = input()
      print("-"*10)
      print("-"*60)
      if check_existing_credential(search_credential):
        search_credential = copy_password(search_credential)
        print("[bold green]Password copied successfully")

      else:
        print("[bold red]That Account does not exist")
      #Function to display command to the user
      display_commands()

    if short_code == "exit":
      print(f">>> Thank you for using our service we hope to see you back soon'")
      break

  
if __name__ == '__main__':

  main()


   