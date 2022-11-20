# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
wn = trtl.Screen()

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

#-----game configuration----
ben_color = "sea green"
ben_size = 1.5
ben_shape = "circle"
score = 0
font_setup = ("Courier", 80, "normal")
font_header_setup = ("Courier", 40, "normal")
font_loser_setup = ("Courier", 75, "normal")
font_winner_setup = ("Courier", 125, "normal")
timer = 15
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#-----initialize turtle-----
ben = trtl.Turtle()
ben.fillcolor(ben_color)
ben.shapesize(ben_size)
ben.shape(ben_shape)
ben.penup()

pointheader =  trtl.Turtle()
pointheader.hideturtle()
pointheader.penup()
pointheader.goto(-150, 295)
pointheader.write("15 PTS TO WIN", font=font_header_setup)

score_header =  trtl.Turtle()
score_header.hideturtle()
score_header.penup()
score_header.goto(-195, 260)
score_header.write("SCORE", font=font_header_setup)

score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(-200, 180)

counter_header =  trtl.Turtle()
counter_header.hideturtle()
counter_header.penup()
counter_header.goto(105, 260)
counter_header.write("TIMER", font=font_header_setup)

counter =  trtl.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(100, 180)

loser = trtl.Turtle()
loser.hideturtle()
loser.penup()
loser.goto(-340, 10)

winner = trtl.Turtle()
winner.hideturtle()
winner.penup()
winner.goto(-340, 40)

#-----images-------
minionW = trtl.Turtle()
wn.addshape("minions_happy.gif")
minionW.shape("minions_happy.gif")

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
        wn.clear()
        score_header.goto(-75, 260)
        score_writer.goto(-40, 180)
        score_header.write("SCORE", font=font_header_setup)
        score_writer.write(score, font=font_setup)
        if score >= 15:
            wn.bgcolor("light green")
            winner.write("W YOU WON", font=font_winner_setup)
        elif score < 15:
            wn.bgcolor("red")
            winner.write("L BOZO YOU LOST", font=font_loser_setup)

#-----events----------------
ben.onclick(ben_clicked)
wn.bgcolor("old lace")
wn.ontimer(countdown, counter_interval) 
wn.mainloop()