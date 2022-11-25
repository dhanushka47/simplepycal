#import lib
from tkinter import *
import tkinter as tk
from tkinter.ttk import *

#create window
root = tk.Tk()
root.geometry('700x200')
root.title("Simple calculator 1.0.0 made by Electro BoY")

#functions
def submit():
    num1 = int(user_input1.get())
    num2 = int(user_input2.get())
    add =  num1+num2
    text2= Label(root,text =add,font =('arial',70,'bold')).place(x =400, y= 50)

#text1
text1= Label(root,text = "This calculator can do addition ",font =('arial',18,'bold')).place(x =30, y= 10)

#get user input 1
user_input1= tk.Entry(root)
user_input1.place(x = 40,  y = 55, width=80, height=30)

text1= Label(root,text = "+",font =('arial',18,'bold')).place(x =150, y= 55)

#get user input 2
user_input2= tk.Entry(root)
user_input2.place(x =200,  y = 55, width=80, height=30)


#buttons
btn1= Button(root,text="Submit",width=40,command= submit).place(x=40 ,y=110)

root.mainloop()