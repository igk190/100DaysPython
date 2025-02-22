invite = open("Input/Letters/starting_letter.txt")

PLACEHOLDER = "[name]"
invite_cleaned = []

for line in invite.readlines():
    invite_cleaned.append(line)

print(invite_cleaned)

names = open("Input/Names/invited_names.txt")
all_names = names.readlines()
print(all_names)

for name in all_names:

    name = name.strip("\n")
    fname = name
    if " " in name:
        fname = name.replace(" ", "_") # if empty space in name, add underscore to filename
    f = open(f"Output/ReadyToSend/letter_for_{fname}.txt", "w")
   
    for line in invite_cleaned:
        if PLACEHOLDER in line: 
            line = line.replace(PLACEHOLDER, name) # result of replace should be assigned to var!
        f.write(line)


""" Learnings
1. Line 24: Assign the result of str.replace() to a var.
2. You could've used with open("filename.txt", "mode") as file: and then modified it.
3. To strip empty spaces and also strip the newline "\n", apply strip() method.
4. When you open a file that doesn't exist, Python will create it for you.
"""
