#   a124_maze_spiral.py
#----INITIAL SETUP----
import turtle as trtl
import random as rand
wn = trtl.Screen()

#----VARIABLES SETUP----
num_of_walls = 5 * 5
wall_length = 50
path_width = 12
wall_color = "black"
wall_count = 1

#----MAZE PEN SETUP----
wall_pen = trtl.Turtle()
wall_pen.hideturtle()
wall_pen.pensize(4)
wall_pen.speed(0)
wall_pen.color(wall_color)

#---DRAWING THE MAZE---
for r in range(num_of_walls):
  #---random door and barrier setup---
  door = rand.randint(path_width*2, (wall_length - path_width*2))
  barrier = rand.randint(path_width*2, (wall_length - path_width*2))
  
  #---skip over first 4 walls---
  if wall_count > 4:
    wall_pen.pendown()
    while abs(door - barrier) < path_width*2:
      door = rand.randint(path_width*2, (wall_length - path_width*2))
  else:
    wall_pen.penup()
  
  wall_pen.left(90)

#if door comes first
  if (door < barrier):
    #---draws doors---
    wall_pen.forward(door)
    wall_pen.penup()
    wall_pen.forward(path_width*2)
    if wall_count > 4:
      wall_pen.pendown()
    #---draws barriers---
    wall_pen.forward(barrier - door - path_width*2)
    wall_pen.left(90)
    wall_pen.forward(path_width*2)
    wall_pen.back(path_width*2)
    wall_pen.right(90)
    wall_pen.forward(wall_length - barrier)

    #---final variable changes---
    wall_length = wall_length + path_width
    wall_count = wall_count + 1
#if barrier comes first
  else:
    #---draws barriers---
    wall_pen.forward(barrier)
    wall_pen.left(90)
    wall_pen.forward(path_width*2)
    wall_pen.back(path_width*2)
    wall_pen.right(90)
    
    #---draws doors---
    wall_pen.forward(door - barrier)
    wall_pen.penup()
    wall_pen.forward(path_width*2)
    if wall_count > 4:
      wall_pen.pendown()
    wall_pen.forward(wall_length - door - path_width*2)

    #---final variable changes---
    wall_length = wall_length + path_width
    wall_count = wall_count + 1

wn.mainloop()