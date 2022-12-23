#   a125_version1.py
#----initial setup----
import turtle as trtl
import random as rand
import leaderboard as lb
wn = trtl.Screen()

#------variables------
score = 0
font_setup = ("Courier", 80, "normal")
font_header_setup = ("Courier", 40, "normal")
timer = 15
counter_interval = 1000   #1000 represents 1 second
timer_up = False
leaderboard_file_name = "a125/125_leaderboard.txt"
player_name = input("Player name: ")

#-----background color----
wn.bgcolor("forest green")
#-----draws river----
river = trtl.Turtle()
river.speed(0)
river.hideturtle()
river.penup()
river.goto(-160, 150)
river.pendown()
river.fillcolor("dodger blue")
river.begin_fill()
river.goto(160, 150)
river.goto(160, -400)
river.goto(-160, -400)
river.goto(-160, 150)
river.end_fill()
#-----writes game title----
game_title = trtl.Turtle()
game_title.hideturtle()
game_title.penup()
game_title.goto(-135, 295)
game_title.write("RAPID RIVER", font=font_header_setup)
#-----writes score header----
score_header =  trtl.Turtle()
score_header.hideturtle()
score_header.penup()
score_header.goto(-195, 260)
score_header.write("SCORE", font=font_header_setup)
#-----writes score----
score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(-200, 180)
#-----writes countdown header----
counter_header =  trtl.Turtle()
counter_header.hideturtle()
counter_header.penup()
counter_header.goto(105, 260)
counter_header.write("TIMER", font=font_header_setup)
#-----writers countdown----
counter =  trtl.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(100, 180)
#-----fish turtle----
fish_image = "a125/fish.gif"
wn.addshape(fish_image) #size: 70x70
fish = trtl.Turtle()
fish.shape(fish_image)
fish.penup()
fish.goto(0, -245)

#------functions------
def game():
  global timer_up
  #boat setup
  boat_image = "a125/boat.gif"
  wn.addshape(boat_image) #size: 80x128
  boat = trtl.Turtle()
  boat.hideturtle()
  boat.shape(boat_image)
  boat.penup()
  boat.setheading(270)
  #draws boats, moves them, and erases them in a loop
  while timer_up == False:
    boatx = rand.randint(-110, 110)
    boat_speed = rand.randint(0, 2)
    boat.goto(boatx, 80)
    boat.speed(boat_speed)
    boat.showturtle()
    boat.forward(450)
    boat.hideturtle()
    #if the boat is lower than the fish AND touching the fish, game is over
    if int(boat.ycor()) < int(-245):
      if (abs(boat.xcor() - fish.xcor()) < 35):
        game_over()
      else:
        update_score()
    else:
      update_score()

def game_over():
  global timer, timer_up
  timer_up = True
  timer = 0
  score_writer.write(score, font=font_setup)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    timer_up = True
    wn.clear()
    score_writer.penup()
    manage_leaderboard()
  else:
    counter.write(str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)
    
def update_score():
  global score
  score +=10
  score_writer.clear()
  score_writer.write(score, font=font_setup)

def manage_leaderboard():
  global score, fish
  # get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(leaderboard_file_name)
  leader_scores_list = lb.get_scores(leaderboard_file_name)
  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, fish, score)
  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, fish, score)
    
def right_key():
  fish.setheading(0)
  fish.forward(15)
def left_key():
  fish.setheading(180)
  fish.forward(15)

#-----other events-------------
wn.listen()
wn.onkeypress(right_key, "Right")
wn.onkeypress(left_key, "Left")
wn.ontimer(countdown, counter_interval) 
game()

wn.mainloop()