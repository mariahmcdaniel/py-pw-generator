uppercase_pool = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_pool = uppercase_pool.lower()

print(lowercase_pool)

while True:
    try:
      num_char = int(input("How many total characters would you like in your password? Enter a number: "))
      break
    except ValueError:
       print("This is not a number. Try again.")
print(f"Your password will contain {num_char} characters.")

