
import random
name=[]# the word the players guessing
guess=[] #the ___ the player will see
puzzles=["jukebox","keyhole","subway","beekeeper","zipper","scratch","pneumonia","zombie","flopping"]
trys=6 #amount of trys the user will get

def image(trys): #this is the images ive tryed to make for each try
    if trys==6:
        print('''   
        
        |
        |
        |
        |               ''')
    elif trys==5:
        print('''
               
        |
        |
        |
        |                
       /
      /
     /                   ''')
    elif trys==4:
        print('''
               
        |
        |
        |
        |                
       / |
      /   |
     /     |              ''')#cant use \ causes error in code
    elif trys==3:
        print('''
               
                
        | /
        |/
        |
        |                
       / |
      /   |
     /     |              ''')
    elif trys==2:
        print('''
               
                
        | /
       /|/
      / |
        |                
       / |
      /   |
     /     |              ''')
    elif trys==1:
        print('''
       ___   
      |_ _|     
      |___|         
        | /
       /|/
      / |
        |                
       / |
      /   |
     /     |              ''')




def players1(name,guess,trys,players1Name):
    name2=random.choice(players1Name) #random item in players1name list    
    for i in range(len(name2)):
        name+=(name2[i])
        guess+=("_")


def players2(name,guess,trys):
    good=0
    go=True
    while go==True:     #creates the word the user has to guess
        ui=(input("What would you like the word to be."))
        if len(ui) < 6: #checks its more then 5 letters
            print("Has to be longer then 5 letters")
        else:
            for i in ui:
                if ord(i) in range(97,122) or ord(i) in range(65,90) : #checks its cap or lower
                    good+=1
                    if good == len(ui): 
                        for x in ui:
                            name.append(x.lower())  #makes list or right answers
                            guess.append("_") #makes list same size as the name
                        go=False    
                else:
                    print("Has to have only letters")





def mainloop(name,guess,trys):
    go=True
    while go==True:     #runs the main hang man part
        image(trys)     
        guess2=""
        x=10
        for i in guess:
            guess2+=i
        print(guess2)
        letter=input("Guess a letter ")
        if trys != 1:
            if len(letter)==1:#checks its only one thing 
                if ord(letter.lower()) in range(97,122):#checks if letter
                    for i in range(len(name)):
                        if letter.lower() == name[i]:
                            guess[i]=letter.lower()
                            x-=1
                            
                            if "_" not in guess:    # if no _ in the guess the the user has won
                                print("You Did it goodjob!!!")
                                go=False  
                    if x == 10: #checks if it was wrong by if any where right then it wold be lower then 10
                        trys-=1
                        print(f"{trys} trys left, try again.")
                        
                else:
                    print("Make sure its only one letter")
            else:
                print("Make sure its only one letter")
        
        else:
            print("you are out of trys")
            go=False # brakes loop when out of trys
player=input("One or Two players (1,2)")
if player == "2":
    players2(name,guess,trys)
    mainloop(name,guess,trys)
elif player=="1":
    players1(name,guess,trys,players1Name)
    mainloop(name,guess,trys)






name2=""
guess2=""
for i in name:
    name2+=i
print(f"The word was {name2}") #tells them what the word was 
for i in guess:
    guess2+=i
print(f"Your final guess ended at {guess2}") #retells them there guess to show how close they where

