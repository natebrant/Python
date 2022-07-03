import random

    
def number():
    y=0
    ui=input("Enter a Number 1-6 ")
    while not ui.isdigit():     #makes sure you cannont input a letter or symbol
        ui=input("Enter a Number 1-6 ")
    y+=1
    while ui == "":     #makes it so you cannon enter nothing
        print("You did not input anything")
        ui = input("Enter a Number 1-6 ")
    y+=1
    while int(ui) >= 7 or int(ui) == 0:     #makes sure you cannot enter a number greater than 7 or 0
        print("that is not a number 1-6 ")
        number()

    y+=1
    if y==3:
        return (int(ui)-1)






#creating the bored
def start(bored):
    for c in range(6):
        for i in range(6):
            bored[i].append("[~]")
    top=""
    for i in range(7):
        top+=f"{i}\t"



def game(bored,top):
    for i in range(25):
        print("\n")
    print(top)
    print("\n")
    x=""
    for c in range(6):
        x=str(c+1)
        x+="\t"
        for i in range(6):
            x+=str(bored[c][i])
            x+="\t"
        print(x)
        print("\n")

def boreds2(cards,bored2,endbored):
    cardleft=36
    for c in range(6):
        for i in range(6):
            x=random.randint(0,cardleft-1)
            bored2.append(cards[x])
            cards.pop(x)
            cardleft-=1
    y=0
    for c in range(6):
        for i in range(6):
            endbored[c].append(bored2[y])
            if y < 35:
                y+=1
    return endbored

