#!/usr/local/bin/python3.9

from tkinter import *
import tkinter as tk
import tkmacosx
import random
#from PIL import Image, ImageTk

# Creating the Window and text block
window = tk.Tk()
txt_block = tk.Text(window, bg="#252525", fg="#FFFFFF", borderwidth=0)
#img_to_insert = tk.PhotoImage(file="venv/lib/rapid7-r7-bullet-solid.png")


class Dinner:
    def __init__(self, name, ingredients, prep_time):
        self.name = name
        self.ingredients = ingredients
        self.preptime = prep_time

    def myfunc(self):
        txt_block.delete(1.0, "end")
#        txt_block.image_create(1.0, image=img_to_insert)
        txt_block.insert("end", self.name + '\n' + self.ingredients + '\n' + self.preptime)


p1 = Dinner("Chicken Alfredo: ", 'noodles, chicken, alfredo sauce', "1 hour")
p2 = Dinner('Chilli: ', 'beans, meat, tomato sauce', '6 hours')
p3 = Dinner("Pulled Pork: ", 'pork chuck, root beer, barbecue sauce', '8 hours')
p4 = Dinner('Spaghetti: ', 'noodles, marinara, beef,', '30 minutes')
p5 = Dinner('Grilled Cheese & Tomato soup: ', 'bread, cheese, butter, tomato soup, milk', '30 minutes')
p6 = Dinner('Stir fry: ', 'rice, chicken, broccoli, soy sauce, teriyaki', '1 hour')


Dinner = ['alfredo', 'chilli', 'pulledPork', 'spaghetti', 'grilled cheese', 'stir fry']


def generator():
    for x in random.choices(Dinner):
        if x == 'alfredo':
            p1.myfunc()
        elif x == 'chilli':
            p2.myfunc()
        elif x == 'pulledPork':
            p3.myfunc()
        elif x == 'spaghetti':
            p4.myfunc()
        elif x == 'grilled cheese':
            p5.myfunc()
        elif x == 'stir fry':
            p6.myfunc()


# Window configurations
window.title("Dinner Generator")
window.geometry("400x100")
window.configure(highlightbackground="#151515")
window.rowconfigure(0, minsize=100, weight=1)
window.columnconfigure(1, minsize=300, weight=1)

# Frame dimensions
fr_buttons = tk.Frame(window, bg="#151515")
fr_buttons.grid(row=0, column=0, sticky="ns")

# Buttons
btn_pick = tk.Button(fr_buttons, text="Choose", command=generator, highlightbackground="#151515")
btn_pick.pack()
btn_pick.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

#btn_add = tk.Button(fr_buttons, text="Add", highlightbackground="#151515")
#btn_add.pack()
#btn_add.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

# Text Block
txt_block.grid(row=0, column=1, sticky="nsew")


window.mainloop()
