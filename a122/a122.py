# a122_catch_a_turtle_leaderboard.py
#-----import statements-----
import turtle as trtl
import random as rand
import leaderboard as lb
wn = trtl.Screen()
wn.bgcolor("old lace")

#-----game configuration----
ben_color = "sea green"
ben_size = 1.5
ben_shape = "circle"
score = 0
font_setup = ("Courier", 80, "normal")
font_header_setup = ("Courier", 40, "normal")
font_loser_setup = ("Courier", 75, "normal")
font_winner_setup = ("Courier", 125, "normal")
timer = 3
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#-----leaderboard variables-----
leaderboard_file_name = "a122/a122_leaderboard.txt"
player_name = input("Player name: ")

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

#-----initialize turtle-----
ben = trtl.Turtle()
ben.fillcolor(ben_color)
ben.shapesize(ben_size)
ben.shape(ben_shape)
ben.penup()

pointheader =  trtl.Turtle()
pointheader.hideturtle()
pointheader.penup()
pointheader.goto(-160, 295)
pointheader.write("CATCH-A-TURTLE", font=font_header_setup)

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

#-----game functions--------
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    timer_up = True
    manage_leaderboard()
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
    if timer_up == False:
        update_score()
        change_position()
    if timer_up == True:
        ben.hideturtle()

def manage_leaderboard():

  global score
  global ben

  # get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(leaderboard_file_name)
  leader_scores_list = lb.get_scores(leaderboard_file_name)

  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, ben, score)

  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, ben, score)

#-----events----------------
ben.onclick(ben_clicked)
wn.ontimer(countdown, counter_interval) 
wn.mainloop()