#   a124_maze_spiral.py
#----initial setup----
import turtle as trtl
wn = trtl.Screen()

#----configuration variables setup----
num_of_walls = 5 * 5
wall_length = 30
path_width = 12
wall_color = "black"
wall_count = 1

#----wall pen actions----
wall_pen = trtl.Turtle()
wall_pen.hideturtle()
wall_pen.pensize(4)
wall_pen.speed(0)
wall_pen.color(wall_color)
  #---walls and doors---
for r in range(num_of_walls):
  wall_pen.left(90)
  wall_pen.forward(10)
  wall_pen.penup()
  wall_pen.forward(path_width)
  wall_pen.pendown()
  
  #---barriers---
  wall_pen.forward(40)
  wall_pen.left(90)
  wall_pen.forward(path_width*2)
  wall_pen.back(path_width*2)
  wall_pen.right(90)
  wall_pen.forward(wall_length)
  wall_length = wall_length + path_width
  wall_count = wall_count + 1

wn.mainloop()