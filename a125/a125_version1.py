#   a125_version1.py
#----initial setup----
import turtle as trtl
import random as rand
import leaderboard as lb
wn = trtl.Screen()

score = 0
font_setup = ("Courier", 80, "normal")
font_header_setup = ("Courier", 40, "normal")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#-----leaderboard variables-----
leaderboard_file_name = "a125/a125_leaderboard.txt"
player_name = input("Player name: ")

#-----game functions--------
def initial_game_setup():
    #bckgd color
    wn.bgcolor("forest green")
    #-----draws river----
    river = trtl.Turtle()
    river.hideturtle()
    river.penup()
    river.goto(-160, 150)
    river.pendown()
    river.fillcolor("dodger blue")
    river.begin_fill()
    river.goto(160, 150)
    river.goto(160, -300)
    river.goto(-160, -300)
    river.goto(-160, 150)
    river.end_fill()
    #-----writes game title----
    game_title =  trtl.Turtle()
    game_title.hideturtle()
    game_title.penup()
    game_title.goto(-160, 295)
    game_title.write("RAPID RIVER", font=font_header_setup)
    #-----writers score header----
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

def game():
    #boat setup
    boat_image = "a125/boat.gif"
    wn.addshape(boat_image) #size: 160x160
    #draws boats randomly
    #moves boat down
    while timer_up == False:
        boat1 = trtl.Turtle()
        boat1.shape(boat_image)
        boat1.penup()
        boat1x = rand.randint(-80, 80)
        boat_speed = rand.randint(1, 5)
        boat1.goto(boat1x, 70)
        boat1.speed(boat_speed)
        boat1.setheading(270)
        boat1.forward(290)
        boat1.hideturtle()


'''def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    timer_up = True
    if level == 1:
        #enter code hereeeeeee for level 1
  else:
    counter.write(str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)'''
    
def update_score():
    global score
    score +=1
    score_writer.clear()
    score_writer.write(score, font=font_setup)

def manage_leaderboard():
  global score
  global fish

  # get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(leaderboard_file_name)
  leader_scores_list = lb.get_scores(leaderboard_file_name)

  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, fish, score)
  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, fish, score)

#-----other events-------------
initial_game_setup()
game()

wn.ontimer(countdown, counter_interval) 

wn.mainloop()