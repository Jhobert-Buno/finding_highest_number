# Ask user to input 3 numbers. Find and print the biggest number using only if-else statement

# pseudocode
# use tkinter
import tkinter
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import PhotoImage

window = tkinter.Tk()
window.title("FINDING THE BIGGEST NUMBER")
window.geometry('925x500+300+200')
window.wm_resizable(False,False)

image_path=PhotoImage(file=r"C:\BsCpE 1st Year\Programming Logic and Design\Python Projects\Assignment #4\finding_highest_number\Background for python.png")
bg_image=tkinter.Label(window,image=image_path)
bg_image.place(relheight=1, relwidth=1)

# Ask for name
# Input 3 numbers
# finding the highest number


window.mainloop()