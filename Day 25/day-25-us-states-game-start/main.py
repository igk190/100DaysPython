import turtle
import pandas
from state_writer import StateWriter

screen = turtle.Screen()
screen.title("US States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

state_writer = StateWriter()

states_correct = 0 # update if correct player guess x/50 St
states_guessed = f"{states_correct} States Correct"

data = pandas.DataFrame(pandas.read_csv("50_states.csv"))
answer_state = screen.textinput(title=states_correct, prompt="What's another state name?").title()
first_row = data.loc[data['state'] > answer_state].iloc[0]
print(first_row)
if data.query("state" == answer_state).iloc[0]:
    
    x = data.query("state" == answer_state)
    print(x)
    guessed_state = data["state"].values == answer_state
    states_correct += 1 
    x_val = guessed_state["x"]
    y_val = guessed_state["y"]
    print(states_guessed, x_val, y_val)
    # write_state(x_val, y_val, answer_state)

    # write_state(x, y, answer_state)
else:
    print("Noooope u answered wrong")

# df.filter(items=['one', 'three'])

# print(data[data.state == answer_state])  # check if user answer is match
# state, x, y, states in col 2 (first is index)


# df.isin(value)
print("you answered: ", answer_state)


# If user correct, write state name to location of where it exists on map
# if guess = wrong, nothing happens, reload input box for another guess.




turtle.mainloop() # alt way of keeping screen open, alt to exitonclick







"""Learnings

1. Get coordinates of mouse clicks with turtle.onscreenclick. Example:

def get_mouse_click_coor(x, y):
    print(x, y)
turtle.onscreenclick(get_mouse_click_coor) # pass in click coordinates

2. screen.textinput() requires a title and prompt.

3. df.isin(values) works on a set or list-like. 
"""