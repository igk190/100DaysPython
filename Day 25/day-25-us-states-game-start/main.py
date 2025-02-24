import turtle

screen = turtle.Screen()
screen.title("US States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

# read 50 states csv
# get those x and y vals
# ask user for answer through use of an inout

# use 50states.csv to check the user's answer against all states in table, see if match (title case)
# plus write this state name to location of where it exists on the map

# if guess = wrong, nothing happens, reload input box for another guess.

# in title, keep track of how many states user has guessed correctly 4/50 States correct

# get data from csv row

answer_state = screen.textinput(title="Answer this Q", prompt="What's another state name?")

turtle.mainloop() # alt way of keeping screen open, alt to exitonclick







"""Learnings

1. Get coordinates of mouse clicks with turtle.onscreenclick. Example:

def get_mouse_click_coor(x, y):
    print(x, y)
turtle.onscreenclick(get_mouse_click_coor) # pass in click coordinates

2. screen.textinput() requires a title and prompt.
"""