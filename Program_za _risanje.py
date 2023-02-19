import turtle 


wn= turtle.Screen ()
wn.title("Program za risanje 1.0.0")
wn.bgcolor("black")
wn.setup(width=500, height=500)
wn.tracer(0)

mreza=turtle.Turtle ()
mreza.hideturtle()
mreza.penup()
mreza.speed(0.1)
mreza.color("grey")
mreza.goto(-240,240)
mreza.pendown()
for i in range(12):
    mreza.right(90)
    mreza.forward(480)
    mreza.left(90)
    mreza.forward(20)
    mreza.left(90)
    mreza.forward(480)
    mreza.right(90)
    mreza.forward(20)
mreza.penup()
mreza.goto(-240,240)
mreza.pendown()
mreza.forward(480)
mreza.right(90)
mreza.forward(480)
mreza.right(90)
mreza.forward(480)
mreza.right(90)
mreza.forward(480)

mreza.back(20)

mreza.right(90)
for j in range(12):
    mreza.forward(480)
    mreza.right(90)
    mreza.forward(20)
    mreza.right(90)
    mreza.forward(480)
    mreza.left(90)
    mreza.forward(20)
    mreza.left(90)


tipka=turtle.Turtle()
tipka.color("orange")
tipka.shape("square")

def paddle_b_up():
    tipka.pendown()
    tipka.color("orange")
    y= tipka.ycor()
    y+= 20
    tipka.sety(y)
    
   
def paddle_b_down():
    tipka.pendown()
    tipka.color("orange")
    y= tipka.ycor()
    y-= 20
    tipka.sety(y)

def ti_r():
    tipka.pendown()
    tipka.color("orange")
    x= tipka.xcor()
    x+= 20
    tipka.setx(x)

   
def tip_l():
    tipka.pendown()
    tipka.color("orange")
    x= tipka.xcor()
    x-= 20
    tipka.setx(x)
#-------------------------------------------------------------------------------------------
def paddle_b_up_s():
    tipka.penup()
    y= tipka.ycor()
    y+= 20
    tipka.sety(y)

def paddle_b_down_s():
    tipka.penup()
    y= tipka.ycor()
    y-= 20
    tipka.sety(y)

def ti_r_s():
    tipka.penup()
    x= tipka.xcor()
    x+= 20
    tipka.setx(x)
 
def tip_l_s():
    tipka.penup()
    x= tipka.xcor()
    x-= 20
    tipka.setx(x)
#--------------------------------------------------------------------------------------------------------------------

def paddle_b_up_b():
    tipka.pendown()
    tipka.color("grey")
    y= tipka.ycor()
    y+= 20
    tipka.sety(y)
      
def paddle_b_down_b():
    tipka.pendown()
    tipka.color("grey")
    y= tipka.ycor()
    y-= 20
    tipka.sety(y)

def ti_r_b():
    tipka.pendown()
    tipka.color("grey")
    x= tipka.xcor()
    x+= 20
    tipka.setx(x)

def tip_l_b():
    tipka.pendown()
    tipka.color("grey")
    x= tipka.xcor()
    x-= 20
    tipka.setx(x)
#--------------------------------------------------------------------------------------------------------------
def skri():
    tipka.hideturtle()

def pokaži():
    tipka.showturtle()








wn.listen()
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(ti_r, "Right")
wn.onkeypress(tip_l, "Left")
wn.onkeypress(paddle_b_up_s, "w")
wn.onkeypress(paddle_b_down_s, "y")
wn.onkeypress(ti_r_s, "s")
wn.onkeypress(tip_l_s, "a")
wn.onkeypress(paddle_b_up_b, "8")
wn.onkeypress(paddle_b_down_b, "2")
wn.onkeypress(ti_r_b, "6")
wn.onkeypress(tip_l_b, "4")
wn.onkeypress(tip_l_b, "4")
wn.onkeypress(skri, "-")
wn.onkeypress(pokaži, "+")

while True:
    wn.update()
