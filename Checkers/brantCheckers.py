import turtle as t
import random 
def rancolors():
    a = hex(random.randrange(0,256))
    b = hex(random.randrange(0,256))
    c = hex(random.randrange(0,256))
    a = a[2:]
    b = b[2:]
    c = c[2:]
    if len(a)<2:
        a = "0" + a
    if len(b)<2:
        b = "0" + b
    if len(c)<2:
        c = "0" + c
    z = a + b + c
    return "#" + z.upper()

def locate(x,y):
    print(f"{x}, {y}")


def button(x, y):
    black[0].goto(x,y)
def button1(x, y):
    black[1].goto(x,y)
def button2(x, y):
    black[2].goto(x,y)
def button3(x, y):
    black[3].goto(x,y)
def button4(x, y):
    black[4].goto(x,y)
def button5(x, y):
    black[5].goto(x,y)
def button6(x, y):
    black[6].goto(x,y)
def button7(x, y):
    black[7].goto(x,y)
def button16(x, y):
    black[8].goto(x,y)
def button17(x, y):
    black[9].goto(x,y)
def button18(x, y):
    black[10].goto(x,y)
def button19(x, y):
    black[11].goto(x,y)


def button8(x, y):
    reds[0].goto(x,y)
def button9(x, y):
    reds[1].goto(x,y)
def button10(x, y):
    reds[2].goto(x,y)
def button11(x, y):
    reds[3].goto(x,y)
def button12(x, y):
    reds[4].goto(x,y)
def button13(x, y):
    reds[5].goto(x,y)
def button14(x, y):
    reds[6].goto(x,y)
def button15(x, y):
    reds[7].goto(x,y)
def button20(x, y):
    reds[8].goto(x,y)
def button21(x, y):
    reds[9].goto(x,y)
def button22(x, y):
    reds[10].goto(x,y)
def button23(x, y):
    reds[11].goto(x,y)
    




pen=t.Turtle()
pen.shape("square")
pen.penup()
pen.turtlesize(2.5)
pen.speed(0)
listy=[]
listy2=[]
color=0
color3=0
color2=[]
checker=""
#Draw row of dots

y=-250
while y<150:
    y+=50
    x=-200
    while(x<200):
        x+=50
        color+=1
        color3+=1
        if color3%8==0:
            listy.append(x)
            listy2.append(y)
            color2.append(color)
            color+=1
        else:
            listy.append(x)
            listy2.append(y)
            color2.append(color)
end=0
while end<10:
    for i in range(len(listy)):
        
        spot=random.randrange(0,len(listy))
        while listy[spot] == "used":
            spot=random.randrange(0,len(listy))
        checker=color2[spot]
        if checker%2 == 0:
            pen.color("red")
            pen.goto(listy[spot],listy2[spot])
            listy[spot]=("used")
            end+=1
            listy2[spot]=("used")
            pen.stamp()
        elif checker%2 == 1:
            pen.color("black")
            pen.goto(listy[spot],listy2[spot])
            end+=1
            listy[spot]=("used")
            listy2[spot]=("used")
            pen.stamp()
redx=[-100,0,100,200,50,-50,-150,150,-100,0,100,200]
redy=[-200,-200,-200,-200,-150,-150,-150,-150,-100,-100,-100,-100]
reds=[]
bx=[-100,0,100,200,50,-50,-150,150,50,-50,-150,150]
by=[100,100,100,100,150,150,150,150,50,50,50,50]
black=[]
for i in range(12):
    reds.append(t.Turtle(shape="circle"))
    reds[i].color("Darkred")
    reds[i].turtlesize(2.5)
    reds[i].penup()
    black.append(t.Turtle(shape="circle"))
    black[i].color("black")
    black[i].turtlesize(2.5)
    black[i].penup()

for i in range(len(reds)):
    reds[i].goto(redx[i],redy[i])
    reds[i].speed(0)
    black[i].goto(bx[i],by[i])
    black[i].speed(0)



black[0].ondrag((button),1)
black[1].ondrag((button1),1)
black[2].ondrag((button2),1)
black[3].ondrag((button3),1)
black[4].ondrag((button4),1)
black[5].ondrag((button5),1)
black[6].ondrag((button6),1)
black[7].ondrag((button7),1)
black[8].ondrag((button16),1)
black[9].ondrag((button17),1)
black[10].ondrag((button18),1)
black[11].ondrag((button19),1)
reds[0].ondrag((button8),1)
reds[1].ondrag((button9),1)
reds[2].ondrag((button10),1)
reds[3].ondrag((button11),1)
reds[4].ondrag((button12),1)
reds[5].ondrag((button13),1)
reds[6].ondrag((button14),1)
reds[7].ondrag((button15),1)
reds[8].ondrag((button20),1)
reds[9].ondrag((button21),1)
reds[10].ondrag((button22),1)
reds[11].ondrag((button23),1)


t.onscreenclick(locate,1)
'''    x=6
size=17
while size != 0: 
    size-=.1
    pen.turtlesize(size)
    y=-250
    while y<250:
        y+=50
        x=-250
        while(x<250):
            x+=50
            if x == -200:
                pen.goto(x,y)
                pen.color(rancolors())
                pen.stamp()
            else:
                pen.goto(x,y)
                pen.color(rancolors())
                pen.stamp()
        x=0
'''
#hola

wn=t.Screen()
wn.mainloop()




