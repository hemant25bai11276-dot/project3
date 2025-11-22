#Import the necesary modules
import random
from tkinter import messagebox
from tkinter import *
#pasward generator function 
def generate_password():
    try:
        repeat = int(repeat_entry.get())
        length = int(length_entry.get())
    except:
        messagebox.showerror(message="please enter the key in the required inputs")
        return
    #check if user allows repetition of characters
    if repeat == 1:
        passward = random.sample(character_string,length)
    else:
        passward = random.choices(character_string,k=length)
    #Since the returned value is a list, we convert to a string using join
    passward=''.join(passward)
    #Declare a string variabe
    passward_v = StringVar()
    passward="created passward: "+str(passward)
    #Assign the passward to the declared string variables 
    passward_v.set(passward)
    #Create a read only entry box to view the output, position using place 
    passward_label = Entry(passward_gen, bd=0, bg="gray85", textvariable=passward_v, state="readonly")
    passward_label.place(x=10, y=140, height=50, width=320)

#Define a string containing letters, symbols and numbers 
character_string = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0123456789!@#$%^&*()/?,."

#define the user interface
passward_gen  = Tk()
passward_gen.geometry("450x300")
passward_gen.title("Random Passward Generator")

#Mension the title of the app 
title_lable = Label(passward_gen,  text="Random passward Generator", font=('ubuntu Mono',12))
title_lable.pack()

#Read length
length_label = Label(passward_gen, text="Enter length of passward:")
length_label.place(x=20,y=30)
length_entry= Entry(passward_gen, width=3)
length_entry.place(x=190,y=30)
#Read repetition
repeat_label = Label(passward_gen, text="Repetition? 1: no repeatition, 2: otherwise")
repeat_label.place(x=20,y=60)
repeat_entry = Entry(passward_gen, width=3)
repeat_entry.place(x=300,y=60)
#Generate passward
passward_button = Button(passward_gen, text="Generate Passward", command=generate_password)
passward_button.place(x=100,y=100)
#Exit and close the app
passward_gen.mainloop()