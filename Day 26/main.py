import pandas as pd

# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }
# for (key, value) in student_dict.items(): #Looping through dictionaries:
#     #Access key and value
#     pass
# student_df = pd.DataFrame(student_dict)
# nato_df = pd.DataFrame("")

# for (index, row) in student_df.iterrows(): #Loop through rows of a data frame
#     #Access index and row
#     #Access row.student or row.score
#     pass

# {new_key:new_value for (index, row) in df.iterrows()} #Keyword Method with iterrows()

# #TODO 1. Create a dictionary in this format:
# #{"A": "Alfa", "B": "Bravo"}

# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.

df = pd.read_csv('nato_phonetic_alphabet.csv')
# nato_dict = {}
# #df_as_dict = df.to_dict()
# for (index, row) in df.iterrows():
#     if index == 0:
#         print(index, row.letter, row.code)

nato_dict2 = {row.letter:row.code for (index, row) in df.iterrows()}    
print(nato_dict2)

# {'letter': 
#     {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'}, 
#  'code':
#     {0: 'Alfa', 1: 'Bravo', 2: 'Charlie', 3: 'Delta', 4: 'Echo', 5: 'Foxtrot', 6: 'Golf', 7: 'Hotel', 8: 'India', 9: 'Juliet', 10: 'Kilo', 11: 'Lima', 12: 'Mike', 13: 'November', 14: 'Oscar', 15: 'Papa', 16: 'Quebec', 17: 'Romeo', 18: 'Sierra', 19: 'Tango', 20: 'Uniform', 21: 'Victor', 22: 'Whiskey', 23: 'X-ray', 24: 'Yankee', 25: 'Zulu'}}

