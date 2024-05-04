import turtle
import winsound
wn = turtle.Screen()
wn.title("Pong by arvind")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)  

scorea=0
scoreb=0

bat = turtle.Turtle()
bat.speed(0)
bat.shape("square")
bat.color("white")
bat.shapesize(stretch_wid=5, stretch_len=1)
bat.penup()
bat.goto(-350, 0)

bat1 = turtle.Turtle()
bat1.speed(0)
bat1.shape("square")
bat1.color("white")
bat1.shapesize(stretch_wid=5, stretch_len=1)
bat1.penup()
bat1.goto(350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.10  
ball.dy = -0.10  

pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0",align="center" , font=("Courier",24,"normal"))

def batup():
    y = bat.ycor()
    y += 20
    bat.sety(y)

def batdown():
    y = bat.ycor()
    y -= 20
    bat.sety(y)

def bat1up():
    y = bat1.ycor()
    y += 20
    bat1.sety(y)

def bat1down():
    y = bat1.ycor()
    y -= 20
    bat1.sety(y)

wn.listen()
wn.onkeypress(batup, "q")
wn.onkeypress(batdown, "a")
wn.onkeypress(bat1up, "Up")
wn.onkeypress(bat1down, "Down")

while True:

    wn.update()  


    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1  
        winsound.PlaySound("bounc.wav",winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounc.wav",winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0) 
        ball.dx *= -1
        scorea+=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(scorea,scoreb),align="center" , font=("Courier",24,"normal"))
        winsound.PlaySound("bounc.wav",winsound.SND_ASYNC)


    if ball.xcor() < -390:
        ball.goto(0, 0) 
        ball.dx *= -1
        scoreb+=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(scorea,scoreb),align="center" , font=("Courier",24,"normal"))
        winsound.PlaySound("bounc.wav",winsound.SND_ASYNC)

    if (ball.xcor()>340 and ball.xcor() < 350) and (ball.ycor()<bat1.ycor()+40 and ball.ycor()>bat1.ycor()-40):
        ball.setx(340)
        ball.dx *= -1  
        winsound.PlaySound("bounc.wav",winsound.SND_ASYNC)

    if (ball.xcor()<-340 and ball.xcor() >-350) and (ball.ycor() < bat.ycor() + 40 and ball.ycor()>bat.ycor()-40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounc.wav",winsound.SND_ASYNC)


