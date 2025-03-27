# Keyword Method with iterrows()

# {new_key:new_value for (index, row) in df.iterrows()}
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

invalid_word = True
while invalid_word:
    try:
        word = input("Enter a word: ").upper()
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Only letters in the alphabet, please.")
    else:
        invalid_word = False
        print(output_list)

# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.


"""Learnings
1. Or put everything inside a function, and call the function again at end of KeyError."""