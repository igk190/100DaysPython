import pandas as pd

""" student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items(): 
    #Access key and value
    pass

student_df = pd.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_df.iterrows(): 
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
{new_key:new_value for (index, row) in df.iterrows()} """


# TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}

df = pd.read_csv('nato_phonetic_alphabet.csv')
nato_dict2 = {row.letter:row.code for (index, row) in df.iterrows()}    
print(nato_dict2)

# TODO 2. Create a LIST of the phonetic code words from a word that the user inputs.

user_name = input("\nWhat is your name?").upper()
user_name_in_nato = [nato_dict2[letter] for letter in user_name]
print(user_name_in_nato)



# car["color"] = "white"


""" Learnings
1. Optional: df_as_dict = df.to_dict()

2. With df.iterrows(), access values through dot notation: row.code, row.letter, keep index in there to access elements

3. split() we don't need, we can iterate over it later.
"""

