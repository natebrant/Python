import random
# from wheelOfFort import *

class Person:#creates each person with a fname lnameand money
    def __init__(self,fname,lname):
        self.money=0
        self.fname=fname
        self.lname=lname
        self.kidney=True
        self.car=False
        self.Curise=False
        self.right=True
        
class weal: #creates a board with random items from board list
    global right
    def __init__(self,board):
        self.bored=[]
        for i in range(25):
            self.bored.append(random.choice(board))
    
    def newRound(self,board):
        self.board=[]
        for i in range(25):
            self.bored.append(random.choice(board))

    def round4(self,board):
        self.board=[]
        for i in range(23):
            self.bored.append(random.choice(board))
        self.bored.append("1000000")

class Puzzle:#uses some code from hang man to create puzzles
    def __init__(self,phrase,end):
        for i in range(len(phrase)):
            if phrase[i] == " ":
                end.append(" ")
            else:
                end.append("#")
    
    def guess(self,person,phrase,end,cat,v=False):
        tryagain = True
        while tryagain == True:
            tryagain = False
            out=""  
            for i in range(len(end)):
                out+=end[i]
            print(out)            
            guess=input(f"The word is in - {cat} - catagory Guess a letter/vowel \n")

            while guess.isdigit():
                guess=input("Guess a letter ")
            guess=guess.upper()
            vowel=["A","E","I","O","U"]
            if v == True:
                if person.money > 250 and str(guess) in vowel:
                    print("Vowel guess you will lose 250$")
                    person.money-=250
                elif person.money < 250 and str(guess) in vowel:
                    print("You dont have the money to afford a Vowel try again")
                else:
                    print("not a vowel")
            if guess not in vowel:
                amount=0
                person.right=False
                for i in range(len(phrase)):
                    if guess == phrase[i]:
                        person.right=True
                        end[i]=guess
                        amount+=1

                if guess not in phrase:
                    print("Ohh not a good letter, Next players turn")
                out=""  
            else:
                print("Cant Guess a vowel") 
            for i in range(len(end)):
                out+=end[i]
            print(out)            


