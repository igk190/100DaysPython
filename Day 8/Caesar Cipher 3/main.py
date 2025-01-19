import art
# TODO-1: Import and print the logo from art.py when the program starts.
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?
# split into cleaned_text and weird_symbols, below the code only checks cleaned text
def caesar(encode_or_decode,original_text, shift_amount):

    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in cleaned_text:
        new_index = alphabet.index(letter) + shift_amount
        output_text += alphabet[new_index]
        #print(output_text)
    print(f"Here is the {direction}d result: {output_text}{weird_symbols}")

# TODO-3: Can you figure out a way to restart the cipher program?
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()

    cleaned_text = ""
    weird_symbols = ""
    for letter in text:
        if letter in alphabet:
            cleaned_text += letter
        else:
            weird_symbols += letter
    print(cleaned_text, weird_symbols)
    shift = int(input("Type the shift number:\n"))

    caesar(encode_or_decode=direction, original_text=text, shift_amount=shift)

    restart = input("Do you want to encode or decode more? Type 'yes' or 'no'\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")



