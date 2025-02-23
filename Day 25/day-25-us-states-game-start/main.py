import turtle

screen = turtle.Screen()
screen.title("US States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor) # passes click coordinates to func

turtle.mainloop() # alt way of keeping screen open, alt to exitonclick





