import turtle as t
import tkinter as tk
import random as r
import threading
import time
speed = 1
def threadFunc():
    global loop
    while True:
        while len(ts) < 1:
            loop+=1
            x=ball()
            print(ts)
        for i in ts:
            i.update()
            
th = threading.Thread(target=threadFunc)

wn = t.Screen()
ts=[]
WINDOW_WIDTH=100
def k2():
    global ts
    for i in ts:
        if i.t.xcor()> -24 and i.t.xcor()<1:
            ts.remove(i)
            i.t.hideturtle()
        
            print(ts)
            break
    # t.update()

def k1():
    global ts
    for i in ts:
        if i.t.xcor()> -49 and i.t.xcor()<-24:
            ts.remove(i)
            i.t.hideturtle()
        
            print(ts)
            break
    # t.update()
def k3():
    global ts
    for i in ts:
        if i.t.xcor()> 1 and i.t.xcor()<26:
            ts.remove(i)
            i.t.hideturtle()
        
            print(ts)
            break
    # t.update()

def k4():
    global ts
    for i in ts:
        if i.t.xcor()> 26 and i.t.xcor()< 51:
            ts.remove(i)
            i.t.hideturtle()
        
            print(ts)
            break
    # t.update()

def up():
    global speed
    speed+=1
def down():
    global speed
    speed-=1


class ball():
  def __init__(self):
    global ts,speed
    spot=[-25,0,25,50]
    self.t = t.Turtle()
    self.t.shape("circle")
    self.t.penup()
    self.t.goto(r.choice(spot),100)
    ts.append(self)
    # t.update()
  def update(self):
    self.t.goto(self.t.xcor(),self.t.ycor()-speed)
    # t.update()

loop=0
            

th.start()
            
wn.onkeypress(k1, "d")
wn.onkeypress(k2, "f")
wn.onkeypress(k3, "j")
wn.onkeypress(k4, "k")  
wn.onkeypress(up, "n")
wn.onkeypress(down, "m")  
# t.update()   
wn.listen()
wn.mainloop()
th.join()