import turtle as t
import secrets
import random
import time
t.speed(0)
wn = t.Screen()

listy_1=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18"]
listy_2=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18"]
best_listy=[]



def randoms():
    thing = (secrets.choice(listy_1))
    listy_1.remove(thing)
    
    thing_2 = (secrets.choice(listy_2))
    listy_2.remove(thing_2)
    
    best_listy.append(thing)
    best_listy.append(thing_2)
    
    
colors=[]
colors2=[]
colors3=[] #wanted 1 list but all colors where dark
for i in range(36):
    colors.append(random.randint(0,255))
    colors2.append(random.randint(0,255))
    colors3.append(random.randint(0,255))


for i in range (18):    
    randoms()
board = []
loop=0
def clear():
    global board,tocheck
    try:
        if tocheck[0].hiddenNum == tocheck[1].hiddenNum:
            if player1.Turn == True:
                player1.score +=1
                player1.update(p1t)
            else:
                player2.score +=1
                player2.update(p2t)
            tocheck[0].correct = tocheck[1].correct = True
            pturn(turn)

        for i in tocheck:
            if i.correct == False:
                i.color("Black")
        tocheck=[]
    except:
        pass
tocheck = []

def play(self,x=None,y=None):
    if self.correct == False:
        global loop,tocheck,colors,colors2,colors3,best_listy
        # print(colors,colors2,colors3)
        t.colormode(255)   
        self.color(colors[best_listy.index(self.hiddenNum)],colors2[best_listy.index(self.hiddenNum)],colors3[best_listy.index(self.hiddenNum)])
        t.colormode(1)   
        tocheck.append(self)
        loop+=1
        if loop%2 == 0:
            time.sleep(.5)
            pturn(turn)
        clear()

class Btn():
    global board,best_listy,colors
    def __init__(self,x,y,spot):
        self = t.Turtle() 
        self.hiddenNum=best_listy[spot]
        self.correct= False
        self.penup()
        self.shape("square")
        self.shapesize(2)
        self.goto(x,y)
        self.color("Black")  
        self.onclick(lambda x,y: play(self))
        board.append(self)
        spot+=1

spot=0
for i in range(6):
    for c in range(6):
        x=str(i)+str(c)
        x=Btn((c*50)-150,(i*50)-150,spot)
        spot+=1

class player():
    def __init__(self,turn,name):
        self.name = name
        self.score=0
        self.Turn = turn
    def update(self,t):
        t.clear()
        t.write(f"{self.name} score: {self.score}")

player1=player(True, "Player1")
player2=player(False, "Player2")
turn=t.Turtle()
turn.penup()
turn.hideturtle()
turn.goto(-25,150) 
def pturn(turn):
    turn.clear()
    if player1.Turn == True:
        player1.Turn = False
        player2.Turn = True
        turn.color("red")   
        turn.write("<-- Turn")

    else:
        player2.Turn=False
        player1.Turn=True
        turn.color("Blue")   
        turn.write("Turn -->")
pturn(turn)

p1t=t.Turtle()
p1t.penup()
p1t.hideturtle()
p1t.goto(-150,150)
p1t.color("red")   

p2t=t.Turtle()
p2t.penup()
p2t.hideturtle()
p2t.goto(25,150)
p2t.color("blue")   

player1.update(p1t)
player2.update(p2t)
wn.mainloop()