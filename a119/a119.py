#   a119_alogrithm_art.py

#Initial setup
import turtle as trtl
wn = trtl.Screen()
bounce = trtl.Turtle()
wn.bgcolor("black")

#Empty list of turtles
turtles = []

#Shapes and colors lists
turtle_shapes = ["turtle", "circle", "square", "circle"]
colors = ["red", "gold", "powder blue", "light green"]

for s in turtle_shapes:
  bounce = trtl.Turtle(shape=s)
  turtles.append(bounce)
  new_color = colors.pop()

bounce.penup()

#Bouncing loop for turtle. Only bounces if the turtle touches the edges of the window.
while True:
    for t in turtles:
        bounce.forward(5)
        if (bounce.xcor() > 320):
            bounce.setheading(135)
            bounce.fillcolor(new_color)
        elif (bounce.xcor() < -330):
            bounce.setheading(300)
        elif (bounce.ycor() > 275):
            bounce.setheading(230)
        elif (bounce.ycor() < -270):
            bounce.setheading(35)


wn.mainloop()