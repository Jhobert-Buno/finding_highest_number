# Ask user to input 3 numbers. Find and print the biggest number using only if-else statement

# pseudocode
# use tkinter
import tkinter
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import PhotoImage, messagebox

def enter():
    try:
        input1 = float(input_one.get())
        input2 = float(input_two.get())
        input3 = float(input_three.get())
    
        if input1 > input2 and input1 > input3:
            result = input1
        elif input2 > input1 and input2 > input3 :
            result = input2
        else:
                result= input3
        
        print("The highest number:", result)
    except ValueError:
        messagebox.showwarning("Error", "Please enter a valid number.")

def cancel():
    window.destroy()

# window
window = tkinter.Tk()
window.title("FINDING THE BIGGEST NUMBER")
window.geometry('604x550+300+200')
window.wm_resizable(False,False)

image_path=PhotoImage(file=r"C:\BsCpE 1st Year\Programming Logic and Design\Python Projects\Assignment #4\finding_highest_number\Background_for_python.png")
bg_image=tkinter.Label(window,image=image_path)
bg_image.place(relheight=1, relwidth=1)

# greetings
frame_heading=tkinter.Frame(window,width=562,height=94,bg='#97FFFF')
frame_heading.place(x=20,y=20)

greetings=tkinter.Label(frame_heading,text="HELLO THERE", fg="#000000",bg='#97FFFF',font=('Helvetica',18,'bold'))
greetings.place(x=198,y=9)

heading=tkinter.Label(frame_heading,text="LET US FIND THE BIGGEST NUMBER", fg="#000000",bg='#97FFFF',font=('impact',31))
heading.place(x=11,y=35)

# note
frame_note=tkinter.Frame(window,width=562,height=50,bg='#97FFFF')
frame_note.place(x=20,y=120)

note=tkinter.Label(frame_note,text="PLEASE INPUT A NUMBER", fg="#000000",bg='#97FFFF',font=('Helvetica',20,'bold'))
note.place(x=110,y=8)

# input 1
def on_enter(e):
    input_one.delete(0,'end')
def on_leave(e):
    if input_one.get()=='':
        input_one.insert(0,' Input 1st number')


input_one = tkinter.Entry(window,width=35,fg='black',border=2,bg='#97FFFF',font=('Microsoft Yahei UI Light',20,'bold'))
input_one.place(x=20,y=200)
input_one.insert(2,  ' Input 1st number')
input_one.bind("<FocusIn>",on_enter)
input_one.bind("<FocusOut>",on_leave)

# input 2
def on_enter(e):
    input_two.delete(0,'end')
def on_leave(e):
    if input_two.get()=='':
        input_two.insert(0,' Input 2nd number')

input_two = tkinter.Entry(window,width=35,fg='black',border=2,bg='#97FFFF',font=('Microsoft Yahei UI Light',20,'bold'))
input_two.place(x=20,y=270)
input_two.insert(2,  ' Input 2nd number')
input_two.bind("<FocusIn>",on_enter)
input_two.bind("<FocusOut>",on_leave)

# input 3
def on_enter(e):
    input_three.delete(0,'end')
def on_leave(e):
    if input_three.get()=='':
        input_three.insert(0,' Input 3rd number')

input_three = tkinter.Entry(window,width=35,fg='black',border=2,bg='#97FFFF',font=('Microsoft Yahei UI Light',20,'bold'))
input_three.place(x=20,y=340)
input_three.insert(2,  ' Input 3rd number')
input_three.bind("<FocusIn>",on_enter)
input_three.bind("<FocusOut>",on_leave)

submit_button = tkinter.Button(window,width=62, text="Submit", command=enter, font='Arial, 11', fg='#DCDCDC')
submit_button.place(x=20, y=395)
submit_button.configure(bg='#1A1A1A')

cancel_button = tkinter.Button(window,width=62, text="Cancel", command=cancel, font='Arial, 11', fg='#000000')
cancel_button.place(x=20, y=435)
cancel_button.configure(bg='#F0F8FF')


window.mainloop()