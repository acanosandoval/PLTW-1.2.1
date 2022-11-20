# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand

#-----ben box limits background (additional custom code)----
box_limits = trtl.Turtle()
box_limits.hideturtle()
box_limits.penup()
box_limits.goto(-325, 150)
box_limits.pendown()
box_limits.fillcolor("navajo white")
box_limits.begin_fill()
box_limits.goto(325, 150)
box_limits.goto(325, -300)
box_limits.goto(-325, -300)
box_limits.goto(-325, 150)
box_limits.end_fill()

'''#MAKE NMBRS OLD LACE'''

#-----game configuration----
ben_color = "sea green"
ben_size = 1.5
ben_shape = "circle"
score = 0
font_setup = ("Arial", 80, "normal")
timer = 15
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#-----initialize turtle-----
ben = trtl.Turtle()
ben.fillcolor(ben_color)
ben.shapesize(ben_size)
ben.shape(ben_shape)
ben.penup()

score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(-200, 180)

counter =  trtl.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(100, 180)

#-----game functions--------
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write(str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)

def change_position():
    new_xpos = rand.randint(-290, 290)
    new_ypos = rand.randint(-265, 115)
    ben.goto(new_xpos,new_ypos)
    
def update_score():
    global score
    score +=1
    score_writer.clear()
    score_writer.write(score, font=font_setup)
    
def ben_clicked(x,y):
    global timer
    if timer_up == (False):
        update_score()
        change_position()
    elif timer_up == (True):
        ben.hideturtle()

#-----events----------------
ben.onclick(ben_clicked)
wn = trtl.Screen()
wn.bgcolor("old lace")
wn.ontimer(countdown, counter_interval) 
wn.mainloop()