from tkinter import *
import tkinter as tk
import random

def createPassword(entry):
  characters = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*'

  #entry = input(entry)
  entry = int(entry)
   
 
  password = ''
  for c in range(entry):
    password += random.choice(characters)
  print("Randomly Generated Password: " + password)

def passwordPrint():
 print("Here is your randomly generated password: " + password )


window = tk.Tk()
window.title("Random Password Generator")


canvas = tk.Canvas(window,width=500, height=260)
#canvas.grid(columnspan=3, rowspan=3)
canvas.pack()


background = tk.PhotoImage(file='rainbow.png')
bkglabel=tk.Label(window,image=background)
bkglabel.place(relwidth=1,relheight=1)

frame = tk.Frame(window, bg="#6ec2d0",bd=5)
frame.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.16,anchor='n')

label = tk.Label(window,text="Enter Password Length",bg="#6ec2d0")
label.place(relx=0.1260,rely=.15,relwidth=.751,relheight=.1)

entry = tk.Entry(frame)
entry.place(relwidth=0.65,relheight=1.2)

button = tk.Button(frame,text="Generate",bg='#58c696',command=lambda: createPassword(entry.get()))
button.place(relx=0.7,relheight=1,relwidth=0.3)



bottom = tk.Frame(window,bg='#6ec2d0',bd=10)
bottom.place(relx=0.5,rely=0.4,relwidth=0.75,relheight=0.4,anchor='n')

bottomlabel = tk.Label(bottom)
bottomlabel.place(relx=0.0,rely=00.,relwidth=1,relheight=1 )



#top = tk.Toplevel()
#msg = tk.Label(window, command=passwordPrint())
#msg.pack()


canvas.mainloop()
