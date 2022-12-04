#   a123_apple_1.py
import turtle as trtl
import random as rand
rand.randint()

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

letters_list = ["a", "s", "d", "f", "g", "h", "i", "j", "k", "l"]
letter = letters_list.pop()

# letter_instruct
letter_instruct = trtl.Turtle()
letter_instruct.hideturtle()
letter_instruct.penup()
letter_instruct.goto(-20, 100)
letter_instruct.color("white")
letter_instruct.write(letter, font=("Arial", 50))

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

# drops apple from tree
def drop_apple():
  apple.goto(0, -160)
  letter_instruct.clear()
  apple.hideturtle()

#-----function calls-----
draw_apple(apple)

wn.onkeypress(drop_apple, letter)
wn.listen()
wn.mainloop()