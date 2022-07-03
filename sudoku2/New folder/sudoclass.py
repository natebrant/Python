import tkinter as tk
board3=[]
class Buttons():
    global board3
    def __init__(self,i,a,outputframe,board2,label):
        self= tk.Button(outputframe, bd = 0,width=5,height=2,justify=tk.RIGHT,command=lambda:click(self,self.cget('text')),text=board2[label],font=("time",10,"bold"))
        self.grid(column=a,row=i,padx=2,pady=2)
        board3.append(self)
        if self.cget("text") != "*":
            self["state"] = tk.DISABLED
        def click(self,number):
            try:
                if int(number) > 8:
                    self.config(text="*")
                else :
                    self.config(text=(int(self.cget("text"))+1))
            except:
                self.config(text=1)
        
# class Boards():
#     global board3
#     def Solved(board):
#         global board3
#         for c in range(9):
#             for r in range(9):
#                 board3[c]


        
