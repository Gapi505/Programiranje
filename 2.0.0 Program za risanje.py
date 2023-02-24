import turtle 


wn= turtle.Screen ()
wn.title("Program za risanje 2.0.0_Narejeno: PRIMOŽ KOLMAN")
wn.bgcolor("black")
wn.setup(width=1500, height=500)
wn.tracer(0)


mreza=turtle.Turtle ()
mreza.hideturtle()
mreza.penup()
mreza.speed(1)
mreza.color("grey")
mreza.goto(150,240)
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
mreza.goto(150,240)
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
tipka.penup()
tipka.goto(390,0)
tipka.pendown()

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

def počisti():
    tipka.clear()


besedilo=turtle.Turtle()
besedilo.penup()
besedilo.hideturtle()
besedilo.goto(-700,200)
besedilo.color("white")
oblika=("Courier", 30, "italic")
oblika_1=("Courier", 10, "italic")

besedilo.write("PROGRAM ZA RISANJE", font=oblika,align="left")
besedilo.goto(-700,150)
besedilo.write("1) Puščica gor --> predmet se premakne za eno polje višje in za sabo pusti sled.", font=oblika_1,align="left")
besedilo.goto(-700,125)
besedilo.write("2) Puščica dol --> predmet se premakne za eno polje nižje in za sabo pusti sled.", font=oblika_1,align="left")
besedilo.goto(-700,100)
besedilo.write("3) Puščica levo--> predmet se premakne za eno polje v levo in za sabo pusti sled.", font=oblika_1,align="left")
besedilo.goto(-700,75)
besedilo.write("4) Puščica desno --> predmet se premakne za eno polje v desno in za sabo pusti sled.", font=oblika_1,align="left")
besedilo.goto(-700,50)
besedilo.write("5) W --> predmet se premakne za eno polje višje, ampak ne pusti sledi. ", font=oblika_1,align="left")
besedilo.goto(-700,25)
besedilo.write("6) Y --> predmet se premakne za eno polje nižje, ampak ne pusti sledi. ", font=oblika_1,align="left")
besedilo.goto(-700,0)
besedilo.write("7) S --> predmet se premakne za eno polje v levo, ampak ne pusti sledi. ", font=oblika_1,align="left")
besedilo.goto(-700,-25)
besedilo.write("8) A --> predmet se premakne za eno polje v desno, ampak ne pusti sledi. ", font=oblika_1,align="left")
besedilo.goto(-700,-50)
besedilo.write("9) 8 --> predmet se premakne za eno polje višje in za sabo puša sivo sled(prvotno barvo).", font=oblika_1,align="left")
besedilo.goto(-700,-75)
besedilo.write("10) 2 --> predmet se premakne za eno polje nižje in za sabo puša sivo sled(prvotno barvo). ", font=oblika_1,align="left")
besedilo.goto(-700,-100)
besedilo.write("11) 6 --> predmet se premakne za eno polje v levo in za sabo puša sivo sled(prvotno barvo). ", font=oblika_1,align="left")
besedilo.goto(-700,-125)
besedilo.write("12) 4  --> predmet se premakne za eno polje v desno in za sabo puša sivo sled(prvotno barvo). ", font=oblika_1,align="left")
besedilo.goto(-700,-150)
besedilo.write("13) - --> predmet se skrije. ", font=oblika_1,align="left")
besedilo.goto(-700,-175)
besedilo.write("14) + --> predmet se pojavi. ", font=oblika_1,align="left")
besedilo.goto(-700,-200)
besedilo.write("15) * --> Vse, kar je bilo narisano se izbriše. ", font=oblika_1,align="left")
besedilo.goto(-700,-225)





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
wn.onkeypress(počisti, "*")


while True:
    wn.update()