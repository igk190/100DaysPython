alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
list_len = len(alphabet) #len=26, last index = 25
print(list_len)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
# fix there cannot be spaces in your word.

shift = int(input("Type the shift number:\n"))

# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
def encrypt(original_text, shift_amount):
    original_text.lower()
# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.
    encrypted_text = ""
    for letter in original_text: #hello
        new_index = alphabet.index(letter) + shift

        if new_index > 25: # is 26 or higher, bc it'll be out of range & you start index from beginning
            when_out_of_range_index = new_index - 26
            encrypted_text += alphabet[when_out_of_range_index]
            print(f"old index is {alphabet.index(letter)}, new index is {when_out_of_range_index}")
        else:
            encrypted_text += alphabet[new_index]
            print(f"old index is {alphabet.index(letter)}, new index is {new_index}")
    print(f"Original text: {original_text}, encrypted text: {encrypted_text}")

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?
# see if else statement line 19-22

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.
encrypt(original_text=text, shift_amount=shift)

