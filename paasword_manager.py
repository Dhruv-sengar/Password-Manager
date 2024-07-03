
from colorama import init, Fore, Back, Style
import os
import getpass
from cryptography.fernet import Fernet



init()

import shutil

def get_terminal_width():
    """Get the width of the terminal window"""
    return shutil.get_terminal_size().columns

def center_text(text):
    """Center text in the terminal"""
    width = get_terminal_width()
    padding = (width - len(text)) // 2
    return ' ' * padding + text


def add_password():
    with open("password.txt", "a") as f:
        f.write(f"{service}:{password}\n")



def view_password():
    service_name = input(Fore.BLUE + "Enter the service name: " + Fore.RESET)
    if os.path.exists("password.txt"):
        found = False
        with open("password.txt", "r") as f:
            for line in f:
                service, password = line.strip().split(":")
                if service == service_name:
                    print(f"Service: {service}, Password: {password}")
                    found = True
                    break
        if not found:
            if service_name:
                print(f"No password found for service: {service_name}")
            else:
                print("No passwords stored yet.")
    else:
        print("Password file not found.")




print(center_text(Fore.RED + Back.GREEN + Style.BRIGHT + "WELCOME TO THE ANONYMOUS PASSWORD MANAGER!! " + Style.RESET_ALL))



while True:
    master_key = getpass.getpass(Fore.BLUE + "ENTER THE MASTER KEY:- " + Fore.RESET)
    if len(master_key) == 0:
        print(center_text(Fore.YELLOW + "MASTER KEY CANNOT BE EMPTY!!" + Fore.RESET))
        continue
    elif master_key != "ANONYMOUS@4u" and  len(master_key) != 12 :
        print(center_text(Fore.RED + "INCORRECT MASTER KEY!" + Fore.RESET))
        continue
    else:
        print(center_text(Fore.GREEN + "CORRECT MASTER KEY!" + Fore.RESET))
        task = input(Fore.BLUE + "ENTER THE TASK(view,add,quit):- " + Fore.RESET)
        if task == "view":
         view_password()
    
        elif task == "add":
         service = input(Fore.BLUE + "ENTER THE SERVICE:- " + Fore.RESET)
         password = getpass.getpass(Fore.MAGENTA + "ENTER THE PASSWORD:- " + Fore.RESET)
         add_password()
    
        elif task == "quit":
         print(center_text(Fore.RED + "THANK YOU FOR USING THE ANONYMOUS PASSWORD MANAGER!!" + Fore.RESET))
         break
        else:
         print(center_text(Fore.RED + "INCORRECT TASK!!" + Fore.RESET))
         continue
    
    
