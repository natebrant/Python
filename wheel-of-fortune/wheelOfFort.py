from wheelOfFortClasses import *
import random
import pandas

import turtle as t
import random
import time
pen=t.Turtle()
pen2=t.Turtle(visible=False)
pen.penup()
pen2.penup()
pen2.pensize(15)
pen2.setx(-20)

pen.shape("circle")
t.colormode(255)
pen.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
pen.shapesize(15)

end=[] #the ___ the player will see
file=tempdata=pandas.read_excel("Puzzles.xlsx",header=0)

players=["player1","player2","player3"]
wheel=[]
prizes=[500,500,750,750,900,900,2500,3500,5000,0,0,"BANKRUPT","Cruise ship trip","This Free Car","glass of orange juice","Plus one kidney","lose a kidney",300,350,800,700,125,550,1110,420,690]
#list of could be prises on list

#---Introduction---
print("America's game, Wheeeeeeeeel of Fortune! The world's most popular game show! And now, from the Sony Studios, here they are the stars of our show, Pat Sajak and Vanna White!")
print("Pat Sajak: Hello and welcome to Wheel of Fortune! I'm Pat Sajack, and this is Vanna White!")
for i in range(3):#loops 3 time to get 3 players
    fname= input("Pat Sajak: what is your first name ")
    lname= input("Pat Sajak: what is your last name ")
    players[i] = Person(fname,lname)
    #print(players)


#---Wheel and 1ame---
wheel=weal(prizes)
board=(wheel.bored)
def spin(person,wheel):
    for i in range(20):
        pen.clear()
        pen2.clear()
        pen.color(random.randint(0,255),random.randint(0,255),random.randint(0,255)) 
        pen.stamp()
        pen2.color("Black")
        prize=random.choice(wheel)
        pen2.write(prize,font=("Arial", 15, "normal"))
        time.sleep(0.01*i)
    try:
        int(prize)
        person.money+=prize
        print(f"Pat Sajak: You have won ${prize}!")
        print(f'${person.money}')
    except:
        if prize=="BANKRUPT":
            person.money=0
            print("Pat Sajak: Ohhhh you hit BANKRUPT!")
            print(f'${person.money}')
            nextplayer(player)
        if prize == "Curise ship trip":
            for i in range(len(prizes)):

                if prizes[i] =="Curise ship trip":
                    prizes[i]=500
            for i in range(len(wheel)):
                if wheel[i] =="Curise ship trip":
                    wheel[i]=500
            person.Curise = True
            print("Pat Sajak: You just won a fantastic Cruise trip!")
        if prize == "This Free Car":
            for i in range(len(prizes)):
                if prizes[i]=="This Free Car":
                    prizes[i]=500
            for i in range(len(wheel)):
                if wheel[i] =="This Free Car":
                    wheel[i]=500
            person.car== True
            print("Pat Sajak: You just won a car!")
        if prize == "glass of orange juice":
            print("Pat Sajak: Here is a drink for the game, you deserve it.")
        if prize == "Plus one kidney":
            if person.kidney==True:
                print("Pat Sajak: Well you already have one so you just get $2500.")
                person.money+2500
                print(f'${person.money}')
            else:
                print("Pat Sajak: Good thing you got this, you needed it!")
                person.kidney=True
        if prize == "lose a kidney":
            if person.kidney == True:
                print("Pat Sajak: Damn you should have read the fine print for what could happen.")
                person.kidney=False
            else:
                print("Pat Sajak: We already took one kidney we won't take the other, but we will take all your money.")
                person.money=0
                print(f'${person.money}')
#---Which player goes first--- 
turn=0 
def nextplayer(player):
    global newround,turn
    if player == 2:
        player = 0
    else:
        player+=1
    turn+=1
    if turn%3 == 0:
        newround=True
        print("Pat Sajak: Time for the next round, New puzzle and board!! ")
    return player 
print(f'Pat Sajak: Welcome {players[0].fname} {players[0].lname}, {players[1].fname} {players[1].lname}, and {players[2].fname} {players[2].lname}')
print("Pat Sajak: Time to see how will go first ... ")
player=random.randint(0,2)
print(f"{players[player].fname} will be going first")
#---SPIN TIME---
newround=True
while True:
    if newround == True:
        x=random.randint(0,780)
        cat=(file["Catag"][x])
        word=(file["questions"][x])
        end=[]
        puz=Puzzle(word,end)
        wheel=weal(prizes)
        board=(wheel.bored)
        print("\n\n\nCurrent players Balence")
        for i in range(3):
            print(f"{players[i].fname}, {players[i].lname} with {players[i].money}")
        newround=False
    # s=input(f"{players[player].fname} spin (type spin) ")
    s=""
    if s != "spin" and s != "vowel":
        s=input(f"{players[player].fname} Time to spin (type spin/vowel) \n")
    if s == "vowel":
            puz.guess(players[player],word,end,cat,v=True)
    if s == "spin":
        while players[player].right == True :
            print("Now Spinning... ")
            print("Pat Sajak: Big money big money big money big money!!!")
            spin(players[player],board)
            print("\nPat Sajak: Time for puzzle")
            puz.guess(players[player],word,end,cat)
    if players[player].right == False and s == "spin":
        s=""
        players[player].right = True
        player=nextplayer(player)

                
# x=Puzzle("cat in the hat",end) how to starts puzzles
# x.guess(players[0],"cat in the hat",end)
# need welcome and gameplay front end things 
# i have all the functions and classes i think for the WOF project if im missing something you cant do just ask 