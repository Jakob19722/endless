from tkinter import *
#Creating a win
win = Tk()
#Giving a Function To The Button
def btn1():
  print("I Don't Know Your Name")
#Creating The Button
button1 =  Button(win, text="Click Me To Print SomeThing", command=btn1)
#put on screen
button1.pack()
win.mainloop()
#NB:This programme Will Print Something In The Terminal
#Check My Profile To See How We Print On The Screen Or Type In Google "Tkinter Label"