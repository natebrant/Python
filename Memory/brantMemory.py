#import stuff
from brantmemoryclass import *
import random
#lists
bored=[[],[],[],[],[],[]]
endbored=[[],[],[],[],[],[]]
x=""
cards=[]
bored2=[]
top=""
#variables
p1=0
p2=0
guess1,guess2=0,0
start(bored)
for i in range(4):
    for j in range(9):
        cards.append(j+1)

boreds2(cards,bored2,endbored)

for i in range(7):
    top+=f"{i}\t"

taken=False
end=0
con=0
player=0
game(bored,top)
print("You get 2 Guesses if the numbers a match they you get a point and go again 2 times,but if not then its the next players turn")#rules
x=0
while end!=36:
    x+=1
    if x==3:
        x=1
    if player%2==0:         #here gets whos turn it is and askes for a number for both x and y
        print(f"player 1 Turn {x}")
    else:
        print(f"player 2 Turn {x}")
    print("horizontal")
    ui2 = number() 
    print("vertical")
    ui = number()

    if bored[ui][ui2] != "[~]":     #makes sure you cannont choose a spot that has already been chosen
        print("Spot taken, Try again.")
        x-=1
    else:
        bored[ui][ui2]=endbored[ui][ui2]
        con+=1
        if con == 2:
            guess2=endbored[ui][ui2]
            con=0
            if guess1==guess2:
                bored[ui][ui2]="   "
                bored[ui3][ui4]="   "
                endbored[ui][ui2]="   "
                endbored[ui3][ui4]="   "
                game(bored,top)
                #making point system work
                if player%2==0:
                    print("player 1 got a point")
                    p1+=1
                    end+=2
                else:
                    print("player 2 got a point")
                    p2+=1
                    end+=2
            else:
                game(bored,top)     #if not match set bored back to [~]
                print("not a match")
                bored[ui][ui2]="[~]"
                bored[ui3][ui4]="[~]"
                player+=1
        else:
            game(bored,top)
            ui3=ui
            ui4=ui2
            guess1=endbored[ui][ui2]
#choosing winner of the game by points     
if end == 36:
    if p1 == p2:
        print("Its a Tie")
    elif p1>p2:
        print("player 1 wins")
        print(f"player 1 has {p1} points while player 2 had {p2}")
    else:
        print("player 2 Wins")
        print(f"player 2 has {p2} points while player 1 had {p1}")