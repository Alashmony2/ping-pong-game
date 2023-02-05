import turtle

wind = turtle.Screen()
wind.title("Ping Pong By AlASHMONY")
wind.bgcolor("orange")
wind.setup(width=800, height=600)
wind.tracer(0)  # stop window from updating automaticly

# madrab1
madrab1 = turtle.Turtle()
madrab1.shape("square")
madrab1.color("blue")
madrab1.shapesize(stretch_wid=5, stretch_len=1)
madrab1.penup()  # to not drawing any line during moving
madrab1.speed(0)
madrab1.goto(-350, 0)
# madrab2
madrab2 = turtle.Turtle()
madrab2.shape("square")
madrab2.color("red")
madrab2.shapesize(stretch_wid=5, stretch_len=1)
madrab2.penup()  # to not drawing any line during moving
madrab2.speed(0)
madrab2.goto(350, 0)
# ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("black")
ball.penup()  # to not drawing any line during moving
ball.speed(0)
ball.goto(0, 0)
ball.dx = .5
ball.dy = .5

# score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("purple")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("player 1: 0 player 2: 0", align="center",
            font=("Courier", 24, "normal"))

# functions

# to move up


def madrab1_up():
    y = madrab1.ycor()  # get the y cordinate of madrab1
    y += 20  # set the y to increas be 20
    madrab1.sety(y)  # set the y of madrab1 to the new cord

# to move down


def madrab1_down():
    y = madrab1.ycor()
    y -= 20  # set the y to decrease be 20
    madrab1.sety(y)

# to move uo


def madrab2_up():
    y = madrab2.ycor()
    y += 20
    madrab2.sety(y)

# to move down


def madrab2_down():
    y = madrab2.ycor()
    y -= 20
    madrab2.sety(y)


# keybord bindings
wind.listen()  # tell window to expect input from keybord
wind.onkeypress(madrab1_up, "w")  # when press w call the function madrab1_up
wind.onkeypress(madrab1_down, "s")
wind.onkeypress(madrab2_up, "Up")
wind.onkeypress(madrab2_down, "Down")

# main game loop
while True:
    wind.update()
    # move the ball
    # ball starts at 0 and every time loops run -->+ 0.8 x
    ball.setx(ball.xcor()+ball.dx)
    # ball starts at 0 and every time loops run -->+ 0.8 x
    ball.sety(ball.ycor()+ball.dy)
    # ball check , top border +300 px , botom border -300 px , ball 20px
    if ball.ycor() > 290:  # if ball is at top border
        ball.sety(290)  # set y cordinate at +290
        ball.dy *= -1  # reverse direction  making +2.5 -->-2.5

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:  # if ball is at the right border
        ball.goto(0, 0)  # return ball to the center
        ball.dx *= -1  # reverse the x direction
        score1 += 1
        score.clear()
        score.write(f"player 1: {score1} player 2: {score2}",
                    align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write(f"player 1: {score1} player 2: {score2}",
                    align="center", font=("Courier", 24, "normal"))
    # madrab touch the ball
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < madrab2.ycor()+40 and ball.ycor() > madrab2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < madrab1.ycor()+40 and ball.ycor() > madrab1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
