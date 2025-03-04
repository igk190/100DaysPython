import turtle
import pandas
from state_writer import StateTracker
from tkinter import messagebox

screen = turtle.Screen()
screen.title("US States Game") # set title upon initialization
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

state_tracker = StateTracker()

data = pandas.DataFrame(pandas.read_csv("50_states.csv"))

while state_tracker.all_guessed_states != 50:
    answer_state = screen.textinput(title=state_tracker.states_guessed_title, 
                                    prompt="What's another state name?").title()
    if answer_state in set(data['state']):
            
            if answer_state in state_tracker.all_guessed_states:
                 messagebox.showinfo("showinfo", "You already guessed this State correctly.") 
            state, x, y = data.loc[data['state'] == answer_state].iloc[0]
            state_tracker.write_state(state, x, y)
            state_tracker.update_state(state)

messagebox.showinfo("showinfo", "Congrats, you guessed all 50 US States!") 

turtle.mainloop() # alt way of keeping screen open, alt to exitonclick

"""Learnings

1. Get coordinates of mouse clicks with turtle.onscreenclick. Example:

def get_mouse_click_coor(x, y):
    print(x, y)
turtle.onscreenclick(get_mouse_click_coor) # pass in click coordinates

2. screen.textinput() requires a title and prompt.

3. df.isin(values) works on a set or list-like. 

4. "The .loc function allows you to select rows and columns of a dataframe based on labels or conditions."
    alternative = data.loc[data['state'] == answer_state].iloc[0] gives a subset of the dataframe
     first_row, x, y = data.loc[data['state'] == answer_state].iloc[0] how you extract vals apparently

5. Title wasn't updating because it showed len(states) at the time of creating it.    
     """


"""Tried 
1. 
temp_list = []
answer_state = screen.textinput(title=state_tracker.states_guessed_title, prompt="What's another state name?").title()
temp_list.append(answer_state) # to test isin on line 19
print(data['state'].isin(temp_list))  but returns the entire series state

2.  print(data[data['state'].str.contains(answer_state)]) 
but this returns anything that matches the string, eg.
"new" retursn New Hampshire, New Jersey, New Mexico, New York

3. test = print(answer_state in data['state'].unique())  returns a Bool

What works:
4. state, x, y = data.loc[data['state'] == answer_state].iloc[0] 
or
data[data.state == answer state]
turtle.goto(data.x.item(), data.y.item())


"""