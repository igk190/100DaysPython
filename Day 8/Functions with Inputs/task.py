# def greet():
#     print("Hi")
#     print("this is line 2")
#     print("And line 3 lol")
#
# greet()

# def greet_with_name(name):
#     print(f"Hi {name}")
#     print(f"Wassup {name}")
#     print("And line 3 lol")
#
# greet_with_name("henkie")

# def greet_with(name = "Jack", location = "Berlin"):
#     print(f"Wassup {name}")
#     print(f"What's it like to live in {location}?")
#
# greet_with()

def calculate_love_score(name1, name2):
    names = name1.lower() + name2.lower()
    true = ["t","r","u","e"]
    love = ["l", "o", "v", "e"]
    true_score = 0
    love_score = 0
    true_love_score = ""

    for letter in names:
        if letter in true:
            true_score += 1
        if letter in love:
            love_score += 1

    true_love_score += str(true_score)
    true_love_score += str(love_score)
    print("Let's see how well you two love birds truly match up.")
    print(f"Your names: {name1}, {name2}")
    print(f"Your true love score is: {true_love_score}")

calculate_love_score("Kanye West", "Kim Kardashian")