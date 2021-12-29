import turtle
import time as tm

#Setting up the screen
win = turtle.Screen()
win.bgcolor("black")
win.title("Ping Pong Game")
win.setup(width=800, height=600)
win.tracer(0)


# Creating class
class User(turtle.Turtle): #turtle module is parameter for class
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.score = 0
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.speed(0)
        
class Ball(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.shape("circle")
        self.color("cyan")
        self.penup()
        self.goto(0, 0)
        self.ball_dx = 0.4 #ball speed x-axis --> increase to make ball move faster
        self.ball_dy = 0.4 #ball speed y-axis --> increase to make ball move faster
        
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.write("Player A: 0         Player B: 0",
                align="center", font=("Courier", 24, "normal")) #Score board
        

# initializing users and positions
user1 = User()
user2 = User()
user1.goto(-350, 0)
user2.goto(350, 0)

#initializing other classes
ball = Ball()
pen = Pen()

try:
    #Moving User1 using the keyboard
    def user1_up(): #Moving up
        y = user1.ycor()
        y += 35
        user1.sety(y)
        
    def user1_down(): #Moving down
        y = user1.ycor()
        y -= 35
        user1.sety(y)
        
    def user2_up(): #Moving up
        y = user2.ycor()
        y += 35
        user2.sety(y)

    def user2_down(): #Moving down
        y = user2.ycor()
        y -= 35
        user2.sety(y)
except Exception as e:
    print(e)
    
    
# Keyboard binding
try:
    win.listen()
    win.onkeypress(user1_up, "w")
    win.onkeypress(user1_down, "s")
    win.onkeypress(user2_up, "Up")
    win.onkeypress(user2_down, "Down")
except Exception as e:
    print(e)

#Main Game loop

while True:
    win.update() # mandatory for the screen to update
    
    #moving the ball
    ball.setx(ball.xcor() + ball.ball_dx)
    ball.sety(ball.ycor() + ball.ball_dy)
    
    try:
        #setting up the border
        if ball.ycor() > 290:
            ball.sety(290)
            ball.ball_dy *= -1
            
        if ball.ycor() < -290:
            ball.sety(-290)
            ball.ball_dy *= -1
            
        if ball.xcor() > 390:
            user1.score += 1
            ball.goto(0, 0)
            ball.ball_dx *= -1
            tm.sleep(0.2)
            pen.clear()
            pen.write("Player A: {}         Player B: {}".format(user1.score, user2.score),
                    align="center", font=("Courier", 24, "normal"))
        
        if ball.xcor() < -390:
            user2.score += 1
            ball.goto(0, 0)
            ball.ball_dx *= -1
            tm.sleep(0.2)
            pen.clear()
            pen.write("Player A: {}         Player B: {}".format(user1.score, user2.score),
                    align="center", font=("Courier", 24, "normal"))

    except Exception as e:
        print(e)
        
    #handling the collision with the paddle
    
    try:
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < user2.ycor() + 40 and ball.ycor() > user2.ycor() - 40):
            ball.setx(340)
            ball.ball_dx *= -1
            
        if(ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < user1.ycor() + 40 and ball.ycor() > user1.ycor() - 40):
            ball.setx(-340)
            ball.ball_dx *= -1
            
        if user1.score == 11:
            pen.clear()
            pen.color("cyan")
            pen.write("Player A wins", align="center", font=("Courier", 24, "normal"))
            tm.sleep(4)
            exit()
        elif user2.score == 11:
            pen.clear()
            pen.color("cyan")
            pen.write("Player B wins", align="center", font=("Courier", 24, "normal"))
            tm.sleep(4)
            exit()
        else:
            continue
    except Exception as e:
        print(e)


        