from ctypes import c_int
import pdb

# pdb.set_trace()
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceaser(encode_or_decode,original_text, shift_amount):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        new_index = alphabet.index(letter) + shift_amount
        output_text += alphabet[new_index]
        print(output_text)
    print(f"Here is the {direction}d result: {output_text}")

ceaser(encode_or_decode=direction,original_text=text, shift_amount=shift)



# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# def decrypt(original_text,shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         new_index = alphabet.index(letter) - shift_amount
#         print(new_index)
#         cipher_text += alphabet[new_index]
#         print(cipher_text)
#
# # TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
# #  by the shift amount and print the decrypted text.
# # TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
# #  Use the value of the user chosen 'direction' variable to determine which functionality to use.
#
# def encrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet)
#         cipher_text += alphabet[shifted_position]
#     print(f"Here is the encoded result: {cipher_text}")

#encrypt(original_text=text, shift_amount=shift)
# decrypt(original_text=text, shift_amount=shift)


