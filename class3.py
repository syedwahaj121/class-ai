"""n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))
n4 = int(input("Enter the fourth number: "))
print(f"addition of {n1} and {n2} is: {n1 + n2} multi of  {n1} and {n2} is: {n1 * n2}")
print(f"addition of {n3} and {n4} is: {n3 + n4} multi of  {n3} and {n4} is: {n3 * n4}")
print(f"mod  of {n1} and {n2} is: {n1 % n2} div of  {n1} and {n2} is: {n1 // n2}")
print(f"mod  of {n1} and {n2} is: {n1 % n2} div of  {n1} and {n2} is: {n1 / n2}")
print(f"addition of {n3} and {n4} is: {n3 + n4} multi of  {n3} and {n4} is: {n3 * n4}")"""
a = input("Enter the first name: ")
b = input("Enter the second name: ")
if a<b:
    print(f"{a} is less than {b}")
elif a==b:
    print(f"{a} is equal to {b}")
else:
    print(f"{a} is greater than {b}")
print(ord('A'))   # 65  → character to number
print(ord('a'))   # 97
print(chr(65))    # 'A' → number to character
print(chr(97))    # 'a'