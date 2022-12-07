#   a123_apple_1.py
import turtle as trtl
import random as rand

#-----setup-----
apple_image = "a123/apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgpic("a123/background.gif")
wn.addshape(apple_image) # Make the screen aware of the new file

letters_template = ["a", "s", "d", "f", "g", "h", "i", "j", "k", "l"]
rand_letter = rand.randint(0, 9)
letters_list = []

apple_list = []

for n in range(5):
  apple = trtl.Turtle()
  apple.penup()
  apple_list.append(apple)

# letter_instruct
letterx = -100
for n in range(5):
  letter_instruct = trtl.Turtle()
  letter_instruct.hideturtle()
  letter_instruct.penup()
  letter_instruct.goto(letterx, 100)
  letterx = letterx + 40
  letter_instruct.color("white")
  letter = letters_template.pop(rand_letter)
  letters_list.append(letter)
  letter_instruct.write(letter, font=("Arial", 50))

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
xcor = int(-140)
ycor = int(60)
def draw_apple(active_apple):
  global xcor, ycor
  active_apple.goto(xcor, ycor)
  active_apple.shape(apple_image)
  wn.update()

# drops apple from tree
def drop_apple():
  apple.sety(-160)
  letter_instruct.clear()
  apple.hideturtle()

#-----function calls-----
for b in range(5):
  draw_apple(apple_list.pop())
  xcor = xcor + 80
  ycor = ycor - 20

wn.onkeypress(drop_apple, letter)
wn.listen()
wn.mainloop()