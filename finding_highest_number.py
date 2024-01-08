# Ask user to input 3 numbers. Find and print the biggest number using only if-else statement

# pseudocode
# use tkinter
import tkinter
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import PhotoImage

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

greetings=tkinter.Label(frame_heading,text="GOOD DAY!!", fg="#000000",bg='#97FFFF',font=('Georgia',18,'bold'))
greetings.place(x=150,y=10)

heading=tkinter.Label(frame_heading,text="LET US FIND THE BIGGEST NUMBER", fg="#000000",bg='#97FFFF',font=('impact',31))
heading.place(x=11,y=40)

# note
frame_note=tkinter.Frame(window,width=562,height=50,bg='#97FFFF')
frame_note.place(x=20,y=120)

note=tkinter.Label(frame_note,text="PLEASE INPUT A NUMBER", fg="#000000",bg='#97FFFF',font=('Helvetica',18,'bold'))
note.place(x=95,y=10)

# input 1
def on_enter(e):
    input_one.delete(0,'end')
def on_leave(e):
    if input_one.get()=='':
        input_one.insert(0,'INPUT 1')

input_one = tkinter.Entry(window,width=37,fg='black',border=0,bg='#97FFFF',font=('Microsoft Yahei UI Light',20))
input_one.place(x=30,y=200)
input_one.insert(0,  'INPUT 1')
input_one.bind("<FocusIn>",on_enter)
input_one.bind("<FocusOut>",on_leave)

# input 2
def on_enter(e):
    input_two.delete(0,'end')
def on_leave(e):
    if input_two.get()=='':
        input_two.insert(0,'INPUT 2')

input_two = tkinter.Entry(window,width=37,fg='black',border=0,bg='#97FFFF',font=('Microsoft Yahei UI Light',20))
input_two.place(x=30,y=270)
input_two.insert(0,  'INPUT 2')
input_two.bind("<FocusIn>",on_enter)
input_two.bind("<FocusOut>",on_leave)

# input 3
def on_enter(e):
    input_three.delete(0,'end')
def on_leave(e):
    if input_three.get()=='':
        input_three.insert(0,'INPUT 3')

input_three = tkinter.Entry(window,width=37,fg='black',border=0,bg='#97FFFF',font=('Microsoft Yahei UI Light',20))
input_three.place(x=30,y=340)
input_three.insert(0,  'INPUT 3')
input_three.bind("<FocusIn>",on_enter)
input_three.bind("<FocusOut>",on_leave)

# Input 3 numbers
# num1=int(input("Enter number 1: "))
# num2=int(input("Enter number 2: "))
# num3=int(input("Enter number 3: "))

# # finding the highest number
# if num1 > num2 and num1 > num3:
#     result = num1
# elif num2 > num1 and num2 > num3 :
#     result = num2
# else:
#     result= num3

# print("The highest number", result)

#23
window.mainloop()