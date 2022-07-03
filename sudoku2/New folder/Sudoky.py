'''
    Goal of this program is to check and see if the Sudoku puzzle the user enters is correct.
    This program should be ran in the same directory as a text file called Puzzle.txt
    The program will check if the Sudoku puzzle is correct then output to the console if it is correct or not.
    If you've never played Sudoku before, here's the rules:  https://sudoku.com/how-to-play/sudoku-rules-for-complete-beginners/
    I have listed out a couple ideas to create this program.  You do not need to do this my way, but I'm telling ya, it will help in the long run.
'''
from sudoclass import *
#read in the text file into a 2D List so you can iterate through it like we did in Tic Tac Toe
import tkinter as tk
import random
root=tk.Tk()
root.title("Sudoku")#set window tital
root.wm_geometry("500x500") #size of windows
root.resizable(0,0)
board3=[]

files=("1puzzle.txt")
#files=("VerticalIssue.txt")
board=[[],[],[],[],[],[],[],[],[]]
with open (files, 'r') as file:
    puzzleFromFile=file.readlines()

for i in range(len(puzzleFromFile)):
    board[i].append(puzzleFromFile[i].rstrip())
        
#print(board)
rowError=0
#open the file
#utilize a for loop to iterate through the file
    #each line should be converted into a list and appended to the board
#utilize a function where you enter a list or row and check if the row has 1-9 exclusively

def solve():
    global board4,board3,board5
    r=0
    c=0
    lo=0
    temp2=""
    temp3=[]
    board4=[]
    for y in range(9):
        for x in range(9):
            temp=board3[lo].cget("text")
            temp2+=str(temp)
            lo+=1
        temp3.append(temp2)
        board4.append(temp3)
        temp3=[]
        temp2=""
    board5=board4
    worknum=[]
    while c <9:
        num=[1,2,3,4,5,6,7,8,9]
        while r <9:
            try:
                int(board5[c][0][r])
                num.remove(int(board5[c][0][r]))
            except:
                #print(board5[c][0][r])
                pass
            r+=1
        worknum.append(num)
        num=[1,2,3,4,5,6,7,8,9]
        c+=1
        r=0
    for c in range(9):
        temp=[]
        for r in range(9):
            temp.append(board5[c][0][r])
        board5[c]=temp
    print(board5)
    for c in range(9):
        tempw=worknum
        for r in range(9):
            if board5[c][r] == "*":
                board5[c][r] = str(random.choice(tempw[c]))
                print(board5[c][r],board5)

def rowChecker(board):
    numbers=[1,2,3,4,5,6,7,8,9]
    row=1
    rowtrue=[0,0,0,0,0,0,0,0,0]
    for i in range(len(board)): #loops throught each row
        for a in board[i]:  #loops throught each row
            for item in a:         #loops through each item in row
                if int(item) in numbers: #if item is 0-10 then and one to number its in
                    x=numbers.index(int(item),0,9)
                    rowtrue[x]+=1
            for i in rowtrue: #checks if theres only one in each row
                if  int(i) == 1: 
                    continue
                elif int(i)>=2:
                    global rowError
                    rowError=(f"{row}, To many {(rowtrue.index(int(i),0,9))+1}s")
            rowtrue=[0,0,0,0,0,0,0,0,0]
            row+=1
    if rowError == 0:
        return True
    else:
        return False
                
        
    #if the board isn't solved horizontally, then return False


collomError=0
#create a function that takes in your 2D List above and checks if each vertical column has 1-9 exclusively
def verticalCheck(board):
    numbers=[1,2,3,4,5,6,7,8,9]
    collom=[]
    collomtrue=[0,0,0,0,0,0,0,0,0]
    global collomError
    x=0
    for col in range(9): #loops through colloms
        for i in range(len(board)): #makes colloms
            for a in board[i]:
                collom.append(a[x:x+1])
        for check in collom:  #adds one to list where number would be
            if int(check) in numbers:
                true=numbers.index(int(check),0,9)
                collomtrue[true]+=1
        #print(collom)
        for i in collomtrue:
            #print(i)
            if  int(i) == 1: 
                continue
            elif int(i)>=2:
                collomError=(f"{col+1}, To many {(collomtrue.index(int(i),0,9))+1}s")
                return False
        x+=1
        collom=[]
        collomtrue=[0,0,0,0,0,0,0,0,0]         
    return True

failedSection=1
#create a function checks the different sections of board.  You could make the function dynamic by passing in which section to check.
def sectionCheck(board):
    global failedSection 
    failedSection=1
    numbers=[1,2,3,4,5,6,7,8,9]
    sections=[]
    sectiontrue=[0,0,0,0,0,0,0,0,0]
    loop=-3
    x=0
    for Repeat in range(3):   
        start=-3
        finish=0
        loop+=3
        for i in range(3): #loops through the 3 section colloms
            con=0
            start+=3
            finish+=3
            for i in range(3): #loops through the 3 virtical colloms
                sections=[]
                for i in range(start,finish): #checks what level of rows its on
                    if con <3:
                        x=0
                    elif con >=3 and con <6:
                        x=3
                    else:
                        x=6
                    for c in range(3): #loops through first 3 items
                        for a in board[(i+loop)]:
                            sections.append(a[x:x+1])
                            x+=1
                    #print(a,x,con)
                    con+=1
                    sectiontrue=[0,0,0,0,0,0,0,0,0]
                    for check in sections:
                        if int(check) in numbers:
                            k=numbers.index(int(check),0,9)
                            sectiontrue[k]+=1
                #print (sections,sectiontrue)
                for i in sectiontrue:
                    if  int(i) == 1: 
                        continue
                    elif int(i)>=2:
                        failedSection=(f"{failedSection}, To many {(sectiontrue.index(int(i),0,9))+1}s")
                        return False
                failedSection+=1
        return True
            
    
board2=[]
for i in range(81):
    (i)=tk.IntVar()
    board2.append(i.get())
def update():
    x=0
    for i in range(9):
        for a in range(9):
            board2[x]=board[i][0][a]
            x+=1

update()
outputframe=tk.Frame(root,height=500,width=500,background="Black",highlightbackground="black",highlightcolor="black",highlightthickness=1)
outputframe.pack()
def checks():
    update()
    global board3,board4
    lo=0
    temp2=""
    temp3=[]
    board4=[]
    for y in range(9):
        for x in range(9):
            temp=board3[lo].cget("text")
            temp2+=str(temp)
            lo+=1
        temp3.append(temp2)
        board4.append(temp3)
        temp3=[]
        temp2=""
        #print(board4)
    blank=False
    for i in range(len(board4)):
        for a in range(len(board4)):
            if board4[i][0][a] == "*":
                errorN.config(text=f"Still A Blank Spot")
                blank=True
                break       
    if blank == False:
        errorN.config(text="")
        if verticalCheck(board4):
            errorC.config(text="passed")
        else:
            errorC.config(text=f"Collom {collomError}")
        if rowChecker(board4):
            errorR.config(text="passed")
        else:
            errorR.config(text=f"Row {rowError}")
        if sectionCheck(board4): 
            errorS.config(text="passed")
        else:
            errorS.config(text=f"Section {failedSection}")
board5=[]
board4=[]
def solved():
    global board5
    x=""
    for i in range(9):
        for a in range(9):
            x+=board5[i][a]
    print(x)
    i=0
    a=0
    for label in range(81):
        label=Buttons(i,a,outputframe,x,label)
        a+=1
        if a%9 == 0:
            i+=1
            a=0

i=0
a=0
for label in range(81):
    label=Buttons(i,a,outputframe,board2,label)
    a+=1
    if a%9 == 0:
        i+=1
        a=0


errorC = tk.Label(outputframe,width=17,height=2,text="Collumn",font=("time",10,"bold"))
errorC.grid(column=0,row=10,padx=2,pady=2,columnspan=3)
errorS=tk.Label(outputframe,width=17,height=2,text="Section",font=("time",10,"bold"))
errorS.grid(column=3,row=10,padx=2,pady=2,columnspan=3)
errorR=tk.Label(outputframe,width=17,height=2,text="Row",font=("time",10,"bold"))
errorR.grid(column=6,row=10,padx=2,pady=2,columnspan=3)



clear=tk.Button(outputframe, bd = 0,width=17,height=2,justify=tk.RIGHT,text="Check",command=checks,font=("time",10,"bold"))
clear.grid(column=0,row=11,padx=2,pady=2,columnspan=3)
errorN=tk.Label(outputframe,width=17,height=2,text="Errors",font=("time",10,"bold"))
errorN.grid(column=3,row=11,padx=2,pady=2,columnspan=3)
solves=tk.Button(outputframe,width=17,height=2,text="slove",command=solve,font=("time",10,"bold"))
solves.grid(column=6,row=11,padx=2,pady=2,columnspan=3)
root.mainloop()