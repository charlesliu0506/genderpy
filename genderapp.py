# Modules -----------------------------------------------

import numpy as np
from tensorflow import keras
import tkinter as tk

# Functions ---------------------------------------------

def clean(str):
    x = str
    for i in "-_+=:;/?!@#$%^&*()~`<>,.1234567890":
        l = x.split(i)
        x = ""
        for j in l:
            x = x+j
    return x.lower()
    
def contains(name, key):
    for i in range(len(name) - len(key) + 1):
        found = True
        for j in range(len(key)):
            if name[i+j] != key[j]:
                found = False
                break
        if found:
            return 1
    return 0

def perm():
    abcs = "qwertyuiopasdfghjklzxcvbnm"
    rlist = []
    for i in abcs:
        rlist.append(i)
    for j in abcs:
        for k in abcs:
            rlist.append(j + k)
    return rlist

def generate(name):
    permlist = perm()
    rlist = []
    for i in permlist:
        rlist.append(contains(name, i))
    return rlist

# Loading Model -----------------------------------------------------------

model = keras.models.load_model("/Users/charl/python/Project Gender/genderpy models/genmodel78")

# Prediction GUI --------------------------------------------------------------------

window = tk.Tk()
window.attributes('-fullscreen',True)
window.configure(background = "white")
name_var = tk.StringVar()
def enter(event):
    name = clean(name_var.get()).title()
    input.delete(0, tk.END)
    prediction = model.predict(np.array([generate(name)]))
    if prediction[0][0] > prediction[0][1]:
        result["text"] = name + " is a boy"
    else:
        result["text"] = name + " is a girl"
    blue["width"] = int(round(100 * prediction[0][0]))
    pink["width"] = int(round(100 * prediction[0][1]))
    input.focus_set()

window.bind("<Return>", enter)

filler1 = tk.Label(
    fg = "white",
    bg = "white",
    width = 40,
    height = 12
)
filler2 = tk.Label(
    fg = "white",
    bg = "white",
    width = 40,
    height = 5
)
input = tk.Entry(
    fg = "black",
    bg = "white",
    width = 20,
    font = ("Segoe UI", 40),
    relief=tk.FLAT,
    textvariable=name_var
)
result = tk.Label(
    fg = "black",
    bg = "white",
    width = 30,
    font = ("Segoe UI", 60),
)
white = tk.Label(
    bg = "white",
    height = 2,
    width = 40
)
pink = tk.Label(
    bg = "pink",
    height = 2,
    width = 50
)
blue = tk.Label(
    bg = "blue",
    height = 2,
    width = 50
)

filler1.pack()
input.pack()
filler2.pack()
result.pack()
white.pack(side = tk.LEFT)
blue.pack(side = tk.LEFT)
pink.pack(side = tk.LEFT)
input.focus_set()
window.mainloop()