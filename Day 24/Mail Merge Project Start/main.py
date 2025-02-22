invite = open("Input/Letters/starting_letter.txt")

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
    f = open("Output/ReadyToSend/letter_for_" + fname + ".txt", "w")
   
    for line in invite_cleaned:
        if "[name]" in line: 
            line = str(line).replace("[name]", name) # result of replace should be assigned to var!
            print("BEGIN", line,"END")
        f.write(line)


