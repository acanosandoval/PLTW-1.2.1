#   a118_turtles_in_traffic.py
import turtle as trtl
wn = trtl.Screen()
wn.screensize(canvwidth =.5, canvheight=.5)

# creates empty lists of turtles
horiz_turtles = []
vert_turtles = []

# uses shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]
tloc = 50 
for s in turtle_shapes:

  ht = trtl.Turtle(shape=s)
  horiz_turtles.append(ht)
  ht.penup()
  new_color = horiz_colors.pop()
  ht.fillcolor(new_color)
  ht.goto(-350, tloc) 
  ht.setheading(0) 

  vt = trtl.Turtle(shape=s)
  vert_turtles.append(vt)
  vt.penup()
  new_color = vert_colors.pop()
  vt.fillcolor(new_color)
  vt.goto( -tloc, 350) 
  vt.setheading(270) 
  
  tloc += 50

# TODO: move turtles across and down screen, stopping for collisions

steps = 0
while steps < 50:
  for t in horiz_turtles:
    t.forward(3)
  for t in vert_turtles:
    t.forward(3)
	
  for h in horiz_turtles:
    for v in vert_turtles:
      if (abs(h.xcor() - v.xcor()) < 20):
        if (abs(h.ycor() - v.ycor()) < 20):
          h.right(180)
          v.right(180)
          

wn = trtl.Screen()
wn.mainloop()
