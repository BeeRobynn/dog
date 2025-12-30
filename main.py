import tkinter as tk
from tkinter import *
from tkinter import ttk
from winsound import *



root = tk.Tk()
root.title("dog")
root.minsize(400, 400)
root.geometry("300x300+50+50")
root.resizable(0,0)
root.iconbitmap("dog.ico")

def create_window():
    credit = tk.Toplevel(root)
    credit.title("Credits")
    credit.minsize(450, 10)
    credit.resizable(0,0)
    credit.iconbitmap("dog.ico")
    imageCredit = tk.Label(credit, text="Image: https://www.nylabone.com/dog101/10-intelligent-dog-breeds")
    soundCredit = tk.Label(credit, text="Sound by crazymonke9 -- https://freesound.org/s/418107/ -- License: Attribution 4.0")
    imageCredit.pack()
    soundCredit.pack()

button = tk.Button(root)
button.pack()
play = lambda: PlaySound('media/sounds/bark.wav', SND_FILENAME)
image = tk.PhotoImage(file="media/images/dog.png")
button.config(image=image, command=play)
m = tk.Menu(root)
filemenu = tk.Menu(m, tearoff=0)
filemenu.add_command(label="Credits", command=create_window)

linkimage = "https://www.nylabone.com/dog101/10-intelligent-dog-breeds"

#tk.Label(root, image=image).pack()
root.config(menu=filemenu)
root.mainloop()