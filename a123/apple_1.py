#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "a123/apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgpic("a123/background.gif")
wn.addshape(apple_image) # Make the screen aware of the new file

apple = trtl.Turtle()
apple.penup()

xcor = apple.xcor()
ycor = apple.ycor()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

def drop_apple(active_apple):
  active_apple.setheading(270)
  active_apple.forward(140)

#-----function calls-----
draw_apple(apple)

wn.onkeypress(drop_apple, "a")

wn.mainloop()