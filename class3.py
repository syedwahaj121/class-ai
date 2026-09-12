from colorama import Fore as color, Style
a = "wahaj"
b = "syed"
user = input("Enter your name: ")
password = input("Enter your password: ")
if(user == a and password == b):
    print(color.GREEN + "wellcome " + user)
else:
    print(color.RED + "  bhag " + user)