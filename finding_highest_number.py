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
window.geometry('500x500+300+200')
window.wm_resizable(False,False)

image_path=PhotoImage(file=r"C:\BsCpE 1st Year\Programming Logic and Design\Python Projects\Assignment #4\finding_highest_number\Background_for_python.png")
bg_image=tkinter.Label(window,image=image_path)
bg_image.place(relheight=1, relwidth=1)

# greetings
frame_heading=tkinter.Frame(window,width=462,height=80,bg='#97FFFF')
frame_heading.place(x=20,y=20)

greetings=tkinter.Label(frame_heading,text="GOOD DAY!!", fg="#000000",bg='#97FFFF',font=('Georgia',18,'bold'))
greetings.place(x=150,y=10)

heading=tkinter.Label(frame_heading,text="LET US FIND THE BIGGEST NUMBER", fg="#000000",bg='#97FFFF',font=('ARIAL',19,'bold'))
heading.place(x=6,y=40)

# Input 3 numbers
num1=int(input("Enter number 1: "))
num2=int(input("Enter number 2: "))
num3=int(input("Enter number 3: "))

# finding the highest number
if num1 > num2 and num1 > num3:
    result = num1
elif num2 > num1 and num2 > num3 :
    result = num2
else:
    result= num3

print("The highest number", result)

#23
window.mainloop()