uppercase_pool = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_pool = uppercase_pool.lower()
number_pool = "0123456789"
special_pool = "!#$%&()*+,-./:;<=>?@[]^_`{|}~"


while True:
    try:
      num_char = int(input("How many total characters would you like in your password? Enter a number: "))
      break
    except ValueError:
       print("This is not a number. Try again.")
print(f"Your password will contain {num_char} characters. Next, lets break down which types of characters you would like to have in your password. The options are \n-uppercase letters \nlowercase letters \nnumbers \nspecial characters")

while True:
    try:
      num_upper = int(input(f"Out of the {num_char} characters in your password, how many of them would you like to be uppercase letters? Enter a number: "))
      break
    except ValueError:
       print("This is not a number. Try again.")
print(f"Your password will contain {num_upper} uppercase characters.")

while True:
    try:
      num_lower = int(input(f"There are {num_char - num_upper} characters left to account for. How many of these would you like to be lowercase letters? Enter a number: "))
      break
    except ValueError:
       print("This is not a number. Try again.")
print(f"Your password will contain {num_lower} lowercase characters.")

