import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = []

letters_length = len(letters) #54, index 53
numbers_length = len(numbers) #10, index 9
symbols_length = len(symbols) #9, index 8
# take random number 0-length of a list
very_random_index = random.randint(0, numbers_length) #not including last index, so keep this

# for i in range(0,symbols_length):
#     print(symbols[i])

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
for i in range(0,nr_letters):
    random_int = random.randint(0,letters_length) # get random value inside list length
    password.append(letters[random_int]) # add value to password at random_int index
    print(password)

nr_symbols = int(input(f"How many symbols would you like?\n"))
for i in range(0,nr_symbols):
    random_int_symbol = random.randint(0,symbols_length) # get random value inside list length
    print(random_int_symbol)
    password.append(symbols[random_int_symbol]) # add value to password at random_int index
    print(password)

nr_numbers = int(input(f"How many numbers would you like?\n"))
for i in range(0,nr_numbers):
    random_int_numbers = random.randint(0,numbers_length) # get random value inside list length
    print(random_int_numbers)
    password.append(numbers[random_int_numbers]) # add value to password at random_int index
    print(password)

print("Your new password is:")
print("before shuffle: " + str(password))
random.shuffle(password)
print("after shuffle: " + str(password))
joined_password = ''.join(password)
print(joined_password)
#why out of range if I press enter too fast when code is running?