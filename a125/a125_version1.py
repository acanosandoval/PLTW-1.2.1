#   a125_version1.py
#----initial setup----
import turtle as trtl
import random as rand
import leaderboard as lb
wn = trtl.Screen()
wn.bgcolor("forest green")

#-----fish turtle----
'''fish_image = "a125/fish.gif"
wn.addshape(fish_image)
fish = trtl.Turtle()
fish.shape(fish_image)
fish.turtlesize = 0.5'''


score = 0
font_setup = ("Courier", 80, "normal")
font_header_setup = ("Courier", 40, "normal")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#-----leaderboard variables-----
leaderboard_file_name = "a125/a125_leaderboard.txt"
player_name = input("Player name: ")

#-----river----
river = trtl.Turtle()
river.hideturtle()
river.penup()
river.goto(-325, 150)
river.pendown()
river.fillcolor("dodger blue")
river.begin_fill()
river.goto(325, 150)
river.goto(325, -300)
river.goto(-325, -300)
river.goto(-325, 150)
river.end_fill()

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

wn.mainloop()