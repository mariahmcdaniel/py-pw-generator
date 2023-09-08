import random

uppercase_pool = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_pool = "abcdefghijklmnopqrstuvwxyz"
number_pool = "0123456789"
special_pool = "!#$%&()*+,-./:;<=>?@[]^_`{|}~"
password = ""

pools = [uppercase_pool, lowercase_pool, number_pool, special_pool]

while True:
    try:
      num_char = int(input("How many total characters would you like in your password? Enter a number: "))
      break
    except ValueError:
       print("This is not a number. Try again.")
print(f"Your password will contain {num_char} characters. \n\nNext, lets break down which types of characters you would like to have in your password. \nThe options are \n-uppercase letters ({uppercase_pool}) \n-lowercase letters ({lowercase_pool}) \n-numbers ({number_pool}) \n-special characters ({special_pool})")

while True:
    try:
      num_upper = int(input(f"Out of the {num_char} characters in your password, how many of them would you like to be uppercase letters? Enter a number: "))
      break
    except ValueError:
       print("This is not a number. Try again.")
print(f"Your password will contain {num_upper} uppercase characters.")

num_left = num_char - num_upper

while True:
    try:
      num_lower = int(input(f"There are {num_left} characters left to account for. How many of these would you like to be lowercase letters? Enter a number: "))
      num_left -= num_lower
      break
    except ValueError:
       print("This is not a number. Try again.")
print(f"Your password will contain {num_lower} lowercase characters.")

while True:
    try:
      num_nums = int(input(f"There are {num_left} characters left to account for. How many of these would you like to be numbers? Enter a number: "))
      num_left -= num_nums
      break
    except ValueError:
       print("This is not a number. Try again.")
print(f"Your password will contain {num_nums} lowercase characters.")

while True:
    try:
      num_special = int(input(f"How many special characters would you like in your password? \n\n Note: There are {num_left} characters left to be assigned. \nif you do not want this many special characters, the remainder will be given a randomly assigned character type. Enter a number: "))
      num_left -= num_special
      break
    except ValueError:
       print("This is not a number. Try again.")
if num_left == 0:       
  print(f"Your password will contain {num_special} special characters.")
else:
  print(f"Your password will contain {num_special} special characters and the {num_left} remaining will be of a random character type")
  types = [num_upper, num_lower, num_nums, num_special]
  
  while num_left > 0:
    for type in types:
     type += 1
     num_left -= 1
     if num_left == 0:
        break


s_uppercase_pool = ''.join(random.sample(uppercase_pool,len(uppercase_pool)))
s_lowercase_pool = ''.join(random.sample(lowercase_pool,len(lowercase_pool)))
s_number_pool = ''.join(random.sample(number_pool,len(number_pool)))
s_special_pool = ''.join(random.sample(special_pool,len(special_pool)))

print(s_lowercase_pool, s_lowercase_pool, s_number_pool, s_special_pool)

for index in range(len(uppercase_pool)):
     password += s_uppercase_pool[index]
     if len(password) == int(num_upper):
        break 

for index in range(len(lowercase_pool)):
     password += s_lowercase_pool[index]
     if len(password) - num_upper == num_lower:
        break

for index in range(len(number_pool)):
     password += s_number_pool[index]
     if len(password) - num_upper - num_lower == num_nums:
        break   

for index in range(len(special_pool)):
     password += s_special_pool[index]
     if len(password) - num_upper - num_lower - num_nums == num_special:
        break 

shuffled_pw = ''.join(random.sample(password,len(password)))

print(f"Your new password is: {shuffled_pw}")                              