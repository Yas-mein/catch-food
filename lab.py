


import  turtle
import os
import random
import time


"creat playing screen"
scr= turtle.Screen()
scr.title('falling food')
scr.bgcolor('blue')
scr.setup(width=505,height=505)

" photos on screen and shapes"
scr.bgpic("74s4f7.gif") ## background picture

scr.register_shape("PLAYER.gif")   ## dolphin picture
scr.register_shape("HUNTER.gif")   ## hunter picture
scr.register_shape("FOOD.gif")     ## food picture


score=0  #add score panle

"add player which eat falling food" #\\yasmin fayed
player = turtle.Turtle()
player.shape("PLAYER.gif")
player.color("yellow")
player.penup() # to hide the line created bcs the animation
player.speed(20)  # give shap animation speed
player.goto(0,-210) #animation direction from up to down location to startfrom
player.direction = "stop" # stop shape in  final position

"add hunter guy "
guys=[] # list of guys

for _ in range(10):
    guy = turtle.Turtle()
    guy.shape("HUNTER.gif")
    guy.color("green")
    guy.speed(20)  # give shap animation speed
    guy.speed = random.randint(21,25)
    guy.penup() # to hide the line created bcs the animation
    guy.goto(0,-210) #animation direction from up to down location to startfrom
    guys.append(guy)


"add food which falling down"  #\\yasmin fayed

foods=[] # list of food falling

for _ in range(10):
    food = turtle.Turtle()
    food.shape("FOOD.gif")
    food.color("red")
    food.speed(20)  # give shap animation speed
    food.speed = random.randint(21,25)
    food.penup() # to hide the line created bcs the animation
    food.goto(0,-210) #animation direction from up to down location to startfrom
    foods.append(food)


" print score on screen "
pan = turtle.Turtle()
pan.hideturtle()
pan.color("blue")
pan.penup() # to hide the line created bcs the animation
pan.goto(0,210) #animation direction from up to down location to startfrom
font=("Courier",20,"bold")
pan.write("Score:: {} ".format(score),align="center",font=font)



"function to control the player shape by keyes"
def move_left():
    player.direction="left"
def move_right():
    player.direction="right"
def move_up():
    player.direction="up"
def move_down():
    player.direction="down"

scr.listen()
scr.onkeypress(move_left , "Left")
scr.onkeypress(move_right ,"Right")
scr.onkeypress(move_up , "Up")
scr.onkeypress(move_down ,"Down")

"main loop => while game started" #\\yasmin fayed
while True:

    scr.update()   #screen shapes move  while playing

    "player move "
    if player.direction == "left":
        x = player.xcor()
        x-=5
        player.setx(x)

    if player.direction == "right":
        x = player.xcor()
        x+=5
        player.setx(x)
    if player.direction == "up":
        y = player.ycor()
        y+=5
        player.sety(y)

    if player.direction == "down":
        y = player.ycor()
        y-=10
        player.sety(y)

    " move hunter guy(>>guys) falling down "
    for guy in guys :
        y=guy.ycor()
        y-= guy.speed
        guy.sety(y)

        if y <-300 : # screen off
            x= random.randint(-220,220)
            y= random.randint(300,400)
            guy.goto(x,y)

            "check collision with player and falling hunter/food"
        if guy.distance(player) <20:
            x = random.randint(-220, 220)
            y = random.randint(300, 400)
            guy.goto(x, y)
            score-=10
            pan.clear()
            pan.write("Score:: {} ".format(score), align="center", font=font)

    " move food (>>foods) falling down "
    for food in foods :
        y=food.ycor()
        y-= food.speed
        food.sety(y)

        if y <-300 : # screen off
            x= random.randint(-220,220)
            y= random.randint(300,400)
            food.goto(x,y)

            "check collision with player and falling hunter/food"
        if food.distance(player) <20:
            x = random.randint(-250, 250)
            y = random.randint(300, 400)
            food.goto(x, y)
            score+=10
            pan.clear()
            pan.write("Score:: {} ".format(score), align="center", font=font)

scr.mainloop()  #\\yasmin fayed



