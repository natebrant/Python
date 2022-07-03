from email import message
import tkinter as tk
import random
import pandas as pd
from tkinter import END, Variable, simpledialog
import sys
root=tk.Tk()
root.title("ATM")#set window tital
# root.wm_geometry("500x500") #size of windows
root.resizable(0,0)
gamemode="login"
btn=[]
dbal=0
user = " "
newpin=0000
move=0
outputframe=tk.Frame(root,background="Black",highlightbackground="black",highlightcolor="black",highlightthickness=1).grid(column=0,row=0)
class BTN():
    def __init__(self,x,i,a):
        bt=["B1","B2","B3","B4","B5","B6","B7","B8"]
        self=tk.Button(outputframe,width=5,justify=tk.RIGHT,text=bt[x],font=("time",10,"bold"),command=lambda:run(self))
        self.grid(row=a,column=i)
        btn.append(self)
def run(self):
    global gamemode,user,newpin,dbal
    if gamemode == "load":      # on load set all text to the options
        lbl[5].config(text = "Deposit")
        lbl[1].config(text = "Withdrawal")
        lbl[2].config(text = "Balance Inquiry")
        lbl[3].config(text = "Transfer Balance")
        lbl[7].config(text = "Change Pin")
        lbl[6].config(text = "Log Out")
        lbl[0].config(text = " ")
        lbl[4].config(text = " ")
        gamemode ="home"
    elif gamemode == "home": # get what the user click and set to gamemode
        if lbl[btn.index(self)].cget("text") != " ":
            gamemode=(lbl[btn.index(self)].cget("text"))    
    if gamemode == "Deposit": #if deposit give options to set a few numbers or other 
        lbl[0].config(text = "10")
        lbl[1].config(text = "20")
        lbl[2].config(text = "40")
        lbl[3].config(text = "50")
        lbl[4].config(text = "100")
        lbl[5].config(text = "500")
        lbl[6].config(text = "Other: click to set")
        lbl[7].config(text = (f"to deposit: {dbal}"))
        user=(lbl[btn.index(self)].cget("text"))
        if user == "Other: click to set":
            if int(numinput.get()) >= 5 and int(numinput.get()) <=500:
                if int(numinput.get())%5 == 0:# if other check it %5 or in wothin 5-500 
                    dbal=int(numinput.get())
                    lbl[7].config(text = (f"to deposit: {dbal}"))
                else:
                    lbl[7].config(text = (f"5-500 & increments of 5"))
            else:
                lbl[7].config(text = (f"5-500 & increments of 5"))
        elif user == f"to deposit: {dbal}":
            pass
        else:
            dbal = int(lbl[btn.index(self)].cget("text"))
            lbl[7].config(text = (f"to deposit: {dbal}")) 
    elif gamemode == "Log Out":
        sys.exit()
    elif gamemode == "Withdrawal": #same as deposit just takes out instead of put in money
        lbl[0].config(text = "10")
        lbl[1].config(text = "20")
        lbl[2].config(text = "40")
        lbl[3].config(text = "50")
        lbl[4].config(text = "100")
        lbl[5].config(text = "500")
        lbl[6].config(text = "Other: click to set")
        lbl[7].config(text = (f"to Withdraw: {dbal}"))
        user=(lbl[btn.index(self)].cget("text"))
        if user == "Other: click to set":
            if int(numinput.get()) >= 5 and int(numinput.get()) <=500:
                if int(numinput.get())%5 == 0:
                    dbal=int(numinput.get())
                    lbl[7].config(text = (f"to Withdraw: {dbal}"))
                else:
                    lbl[7].config(text = (f"5-500 & increments of 5"))
            else:
                lbl[7].config(text = (f"5-500 & increments of 5"))
        elif user == f"to Withdraw: {dbal}":
            pass
        else:
            dbal = int(lbl[btn.index(self)].cget("text"))
            lbl[7].config(text = (f"to Withdraw: {dbal}"))
    elif gamemode == "Balance Inquiry": #tells saveings and checnking balance
        lbl[0].config(text = "")
        lbl[1].config(text = "")
        lbl[2].config(text = "")
        lbl[4].config(text = "")
        lbl[5].config(text = "")
        lbl[6].config(text = "")
        x=file["Savings"][creditCard.index(ui)]
        lbl[3].config(text = f"Saveings {x}$")
        x=file["Checkings"][creditCard.index(ui)]
        lbl[7].config(text = f"Checking {x}$")
    elif gamemode == "Change Pin": #lets you change your pin
        lbl[0].config(text = "Click to update new pin")
        lbl[1].config(text = "")
        lbl[2].config(text = "")
        lbl[4].config(text = "")
        lbl[5].config(text = "")
        lbl[6].config(text = "")
        lbl[3].config(text = "")
        lbl[7].config(text = "")
        user=(lbl[btn.index(self)].cget("text")) 
        print((lbl[btn.index(self)].cget("text")))
        if user == "Click to update new pin": #if the pin they picked  is 4 long and a number then set to there new pin
            print((str(numinput.get())).isdigit(),len(str(numinput.get())))
            if len(str(numinput.get())) == 4 and (str(numinput.get())).isdigit() == True:
                lbl[4].config(text = (f"click Enter to confirm"))
                lbl[5].config(text = (f""))
                lbl[6].config(text = (f""))
            else:
                lbl[4].config(text = (f"not valid pin"))
                lbl[5].config(text = (f"not four zeros"))
                lbl[6].config(text = (f"4 numbers"))
        else:
            pass
    elif gamemode == "Transfer Balance":
            lbl[0].config(text = "")
            lbl[1].config(text = "")
            lbl[2].config(text = "")
            lbl[4].config(text = "")
            lbl[5].config(text = "")
            lbl[6].config(text = "")
            lbl[3].config(text = "")
            lbl[7].config(text = "")
            login.delete(0,END)
            login2.delete(0,END)
            login.insert(0,"Enter card")
            login2.insert(0,"Amount 5-500")
            # login3.config(text="Who to transfer to")
            login.grid(column=5,row=0)
            login2.grid(column=5,row=1)
            # login3.grid(column=5,row=2)
                
                
                
                
a=0
i=0
x=0
for Bt in range(8):
    Bt=BTN(x,i,a)
    a+=1
    x+=1
    if a%4 == 0: #a and i for row and colloum it will be in
        i+=3
        a=0


lbl=[]
class LBL():
    def __init__(self,i,a):
        global lbl
        #Lb=['LB1',"LB2","LB3","LB4","LB5","LB6","LB7","LB8"]
        self=tk.Label(outputframe,width=20,text=" ",font=("time",10,"bold"))# creates lbl objects with a number to be linked with object buttons
        self.grid(row=a,column=i)
        lbl.append(self)
        
        
a=0
i=1
for lb in range(20,28,1):
    lb=LBL(i,a)
    a+=1
    if a%4 == 0: #a and i for row and colloum it will be in
        i+=1
        a=0     
numinput=tk.IntVar()
outputframe2=tk.Frame(root,background="Black",highlightbackground="black",highlightcolor="black",highlightthickness=1)
outputframe2.grid(column=1,row=4,columnspan=2) # makes frames
inputs=tk.Entry(outputframe2,width=6,justify=tk.RIGHT,font=("time",10,"bold"),textvariable=numinput)
inputs.grid(column=4,row=3) # ands the input spot that the user will use to tpye most things
class numpad():
    def __init__(self,x,a,i):
        num=[7,8,9,4,5,6,1,2,3," ",0," "]
        self= tk.Button(outputframe2,width=5,justify=tk.RIGHT,text=num[x],font=("time",10,"bold"),command=lambda:numm(self.cget("text")))
        self.grid(column=a,row=i,padx=2,pady=2) # makes numpad
def numm(self):  
    temp=str(numinput.get())      
    temp+=str(self)
    numinput.set(temp)
    

a=0
i=0
for label in range(12):
    label=numpad(label,a,i)
    a+=1
    if a%3 == 0: #a and i for row and colloum it will be in
        i+=1
        a=0

def cancel():
    global gamemode #send the user hack to home screen
    if gamemode == "login":    
        login.delete(0,END)
        login2.delete(0,END)
        login.insert(0,0)
        login2.insert(0,0)
    elif gamemode == "Transfer Balance":
        login.grid_remove()
        login2.grid_remove()
        login3.grid_remove()
        gamemode = "load"
        run(btn[1])
    else:
        gamemode = "load"
        run(btn[1])
def clear():
    global gamemode  # clears then number in inputs
    if gamemode == "login":   
        login.delete(0,END)
        login2.delete(0,END)
        login.insert(0,0)
        login2.insert(0,0)
    else:
        numinput.set(0)

def save():
    global file #updates text file
    file.to_csv("db.csv")
def submit():
    global move,dbal
    if gamemode == "Deposit":
        file["Checkings"][creditCard.index(ui)]=file["Checkings"][creditCard.index(ui)]+dbal 
        #this and withdraw are to same just + or a -
        x=file["Checkings"][creditCard.index(ui)]
        tk.messagebox.showwarning(title="Withdrawal",message=f"{dbal} was Withdrawen {x}$ remain")
        # shows warning wor what you did and then saves it
        move +=1
        save()
    elif gamemode == "Withdrawal":
        file["Checkings"][creditCard.index(ui)]=file["Checkings"][creditCard.index(ui)]-dbal
        x=file["Checkings"][creditCard.index(ui)]
        tk.messagebox.showwarning(title="Withdrawal",message=f"{dbal} was Withdrawen {x}$ remain")
        move +=1
        save()
    elif gamemode == "Change Pin":
        file["Pin"][creditCard.index(ui)]=numinput.get()
        dbal=file["Pin"][creditCard.index(ui)]
        # updates the pin and shows warning
        tk.messagebox.showwarning(title="Pin",message=f"{dbal} is your new pin")
        move +=1
        save()
    elif gamemode == "Transfer Balance":
        print(creditCard,ui,int(login2.get()))
        if int(login2.get()) >= 5 and int(login2.get()) <=500:
            if int(login2.get())%5 == 0:
                if int(login.get()) in creditCard:
                    file["Checkings"][creditCard.index(ui)]=file["Checkings"][creditCard.index(ui)]-int(login2.get())
                    file["Checkings"][creditCard.index(int(login.get()))]=file["Checkings"][creditCard.index(int(login.get()))]+int(login2.get())
                    x=file["Checkings"][creditCard.index(ui)]
                    dbal=login2.get()
                    tk.messagebox.showwarning(title="transfer",message=f"{login2.get()} was tranferd to {login.get()}, {x}$ remain in account")
                    move+=1
                    save()
                else:
                    login.delete(0,END)
                    tk.messagebox.showwarning(title="erroe",message=f"Invaliad account")
        
            else:
                login2.delete(0,END)
                tk.messagebox.showwarning(title="error",message="can only go by 5$ increments up to 500")
        else:
            login2.delete(0,END)
            tk.messagebox.showwarning(title="error",message="can only go by 5$ increments up to 500")
        
        
        
    with open("log.txt","a") as f:
        x=file["CustomerName"][creditCard.index(ui)] # makes a log file that tracks what was saved 
        f.writelines(f"{x} had a {gamemode} for/to {dbal} <<line {creditCard.index(ui)}>>\n")
    if move == 3:
        tk.messagebox.showwarning(title="moves",message=f"Transaction limit reached relog for more")
        sys.exit()
    cancel()
Clear= tk.Button(outputframe2,width=5,justify=tk.RIGHT,text="Clear",font=("time",10,"bold"),background="yellow",command=clear)
Clear.grid(column=4,row=0)
Cancel= tk.Button(outputframe2,width=5,justify=tk.RIGHT,text="Cancel",font=("time",10,"bold"),background="red",command=cancel)
Cancel.grid(column=4,row=1)
Enter= tk.Button(outputframe2,width=5,justify=tk.RIGHT,text="Enter",font=("time",10,"bold"),background="green",command=submit)
Enter.grid(column=4,row=2)
btn.append(Enter)
ui=" "
ui2=" " #some variables 
row=''
run(1)
file=pd.read_csv("db.csv",header=0) #reads file
# file.to_csv("db2.csv",header=0)
creditCard=[]
for i in file["CreditCard"]:
    creditCard.append(i)          #made card to do .index cuse caused numphy error without
pin=[]
for i in file["Pin"]:
    pin.append(i) 



card=tk.StringVar()
pins=tk.StringVar()
def signin():       # sigh in fucntion
    global gamemode,trys,ui,ui2,creditCard,pin,row
    if gamemode == "Transfer Balance":
        print(login.get())
    else:
        if trys > 3:
            tk.messagebox.showwarning(title="out of trys",message="restart program to try again")
            sys.exit()
        try:
            ui=int(login.get())
            ui2=int(login2.get())
            try:
                row=(creditCard.index(ui)) #checks if pin and card are in the same row if true remove login box and long set game mode to load
                row2=(pin.index(ui2))
                if row == row2:
                    login.grid_remove()
                    login2.grid_remove()
                    login3.grid_remove()
                    gamemode = "load"
                    run(btn[1])
            except:
                1/0
        except:
            tk.messagebox.showwarning(title="Error",message="make sure it is a number")
            ui,ui2=" "," "
            return False
        trys+=1
if gamemode == "login":
    trys=0
    login=tk.Entry(outputframe2,width=15,justify=tk.RIGHT,font=("time",10,"bold"),textvariable=card,text="Enter card")
    login.insert(0,"Enter card")
    login.grid(column=5,row=0)      #creates the login menue 
    login2=tk.Entry(outputframe2,width=15,justify=tk.RIGHT,font=("time",10,"bold"),textvariable=pins,text="Enter pin")
    login2.insert(0,"Enter Pin")
    login2.grid(column=5,row=1)
    login3=tk.Button(outputframe2,width=15,justify=tk.RIGHT,font=("time",10,"bold"),text="Sign in",command=signin)
    login3.grid(column=5,row=2)

root.mainloop()