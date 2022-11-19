#   a121_alogrithm_art.py
import turtle as trtl
bounce = trtl.Turtle()
wn = trtl.Screen()
wn.bgcolor("powder blue")


#RED BALL
#Setting up turtle
bounce.shape("turtle")
bounce.color("light green")
bounce.penup()

#Bouncing loop for turtle. Only bounces if the turtle touches the edges of the window.
while True:
    bounce.forward(6)
    if (bounce.xcor() > 320):
        bounce.setheading(135)
    elif (bounce.xcor() < -330):
        bounce.setheading(300)
    elif (bounce.ycor() > 275):
        bounce.setheading(230)
    elif (bounce.ycor() < -270):
        bounce.setheading(35)

wn.mainloop()