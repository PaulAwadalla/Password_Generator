# Password Generator Project
import random
import time
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
print("Awesome!! We are generating the password for you...")
time.sleep(2)
print("\n")
print("We have generate few different passwords for you...")
time.sleep(2)
print("Pick anyone that you are comfortable with.")
print("\n")
print("------------------------------------------------------")
final_password = []
for letter in range(nr_letters):
    final_password.append(random.choice(letters))

for symbol in range(nr_symbols):
    final_password.append(random.choice(symbols))

for number in range(nr_numbers):
    final_password.append(random.choice(numbers))

final_password_str = ''.join(final_password)
time.sleep(1)
print("Here is your generate password:", final_password_str)
print("\n")
sort_final_password_str = sorted(final_password_str)
sorted_final_password_str = ''.join(sort_final_password_str)
time.sleep(1)
print("Here is your sorted generate password:", sorted_final_password_str)
print("\n")
random_final_password = random.sample(final_password, len(final_password_str))
random_final_password_str = ''.join(random_final_password)
time.sleep(1)
print("Here is your randomised generate password:", random_final_password_str)
time.sleep(1)
print("------------------------------------------------------")
print("\n")
print("Thank you for using password generator!!")
