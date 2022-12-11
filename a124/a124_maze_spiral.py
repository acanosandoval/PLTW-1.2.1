#   a124_maze_spiral.py
#----initial setup----
import turtle as trtl
wn = trtl.Screen()

#----configuration variables setup----
num_of_walls = 5 * 5
wall_length = 20
path_width = 12
wall_color = "black"
 
#----maze pen actions----
wall_pen = trtl.Turtle()
wall_pen.pensize(4)
wall_pen.speed(0)
wall_pen.color(wall_color)
for r in range(num_of_walls):
 wall_pen.left(90)
 wall_pen.forward(wall_length)
 wall_length = wall_length + path_width

wn.mainloop()