from cgitb import text
from functools import cache
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from random import randint

# Maak een nieuw window met een titel
window = Tk()
window.title("Dobbelen")

# Functies voor het menu
def show_thing_1():
    window.title("Dobbelen")
    boterkaasei.pack_forget()
    frame_thing_1.pack()

def show_thing_2():
    window.title("Boter, kaas en eieren")
    boterkaasei.pack()
    frame_thing_1.pack_forget()

# Menu maken
menubar = Menu(window)
window.config(menu=menubar)

# Menu items maken
mainmenu = Menu(menubar)
mainmenu.add_command(label="Dobbelen", command=show_thing_1)
mainmenu.add_command(label="Boter, kaas en eieren", command=show_thing_2)          
mainmenu.add_separator()
mainmenu.add_command(label="Afsluiten", command=window.quit)
# Menu toevoegen aan menubar
menubar.add_cascade(label="Spellen", menu=mainmenu)

# FRAME VOOR THING 1 --------------------------------
frame_thing_1 = Frame(borderwidth=10, bg="pink")
hint = tk.Label(frame_thing_1 ,text="Druk op dobbelen om te dobbelen", bg="beige")
hint2 = tk.Label(frame_thing_1 ,text="Aantal dobbelstenen:", bg="beige")
keren = tk.Entry(frame_thing_1 ,text="Keren dobbelen", bg='beige')
button = tk.Button(frame_thing_1 ,text='Dobbelen')
gegooid = tk.Label(frame_thing_1 ,text="", bg="beige")

hint.pack()
hint2.pack()
keren.pack()
button.pack()
gegooid.pack()

def dobbelen(event):
    gegooid["text"] = ""
    kerenD = keren.get()
    if kerenD.isnumeric() == True and kerenD != "0":
        for keer in range(int(kerenD)):
            gegooid["text"] = gegooid["text"]+str(randint(1,6))+", "
    else:
        gegooid["text"] = str(randint(1,6))


button.bind("<Button-1>",dobbelen)

# FRAME VOOR THING 2 --------------------------------
boterkaasei = Frame(borderwidth=10, bg="bisque")
lbl = Label(boterkaasei, text="Boter kaas en eieren!", bg="#FFDEAD", font=('Helvetica', '15'))
lbl.grid(row=0, column=0)
lbl = Label(boterkaasei, text="Speler 1: X", bg="#FFDEAD", font=('Helvetica', '10'))
lbl.grid(row=1, column=0)
lbl = Label(boterkaasei, text="Speler 2: O", bg="#FFDEAD", font=('Helvetica', '10'))
lbl.grid(row=2, column=0)

turn = 1  # For first person turn.

flag = Canvas()

def clickedproccessing():
    global turn
    if turn == 1:
        turn = 2
        return "X"
    elif turn == 2:
        turn = 1
        return "O"


def clicked1():
    global turn
    if btn1["text"] == " ":  # For getting the text of a button
        btn1["text"] = clickedproccessing()
        check()


def clicked2():
    global turn
    if btn2["text"] == " ":
        btn2["text"] = clickedproccessing()
        check()


def clicked3():
    global turn
    if btn3["text"] == " ":
        btn3["text"] = clickedproccessing()
        check()


def clicked4():
    global turn
    if btn4["text"] == " ":
        btn4["text"] = clickedproccessing()
        check()


def clicked5():
    global turn
    if btn5["text"] == " ":
        btn5["text"] = clickedproccessing()
        check()


def clicked6():
    global turn
    if btn6["text"] == " ":
        btn6["text"] = clickedproccessing()
        check()


def clicked7():
    global turn
    if btn7["text"] == " ":
        btn7["text"] = clickedproccessing()
        check()


def clicked8():
    global turn
    if btn8["text"] == " ":
        btn8["text"] = clickedproccessing()
        check()


def clicked9():
    global turn
    if btn9["text"] == " ":
        btn9["text"] = clickedproccessing()
        check()


def check():
    global flag
    b1 = btn1["text"] # Getting value from each button,
    b2 = btn2["text"] # to check for any possible win event
    b3 = btn3["text"]
    b4 = btn4["text"]
    b5 = btn5["text"]
    b6 = btn6["text"]
    b7 = btn7["text"]
    b8 = btn8["text"]
    b9 = btn9["text"]
    flag += 1
    # Check every possible win on map
    if b1 == b2 and b1 == b3 and b1 == "O" or b1 == b2 and b1 == b3 and b1 == "X":
        win(b1)
    if b4 == b5 and b4 == b6 and b4 == "O" or b4 == b5 and b4 == b6 and b4 == "X":
        win(b4)
    if b7 == b8 and b7 == b9 and b7 == "O" or b7 == b8 and b7 == b9 and b7 == "X":
        win(b7)
    if b1 == b4 and b1 == b7 and b1 == "O" or b1 == b4 and b1 == b7 and b1 == "X":
        win(b1)
    if b2 == b5 and b2 == b8 and b2 == "O" or b2 == b5 and b2 == b8 and b2 == "X":
        win(b2)
    if b3 == b6 and b3 == b9 and b3 == "O" or b3 == b6 and b3 == b9 and b3 == "X":
        win(b3)
    if b1 == b5 and b1 == b9 and b1 == "O" or b1 == b5 and b1 == b9 and b1 == "X":
        win(b1)
    if b7 == b5 and b7 == b3 and b7 == "O" or b7 == b5 and b7 == b3 and b7 == "X":
        win(b7)
    elif flag == 9:
        messagebox.showinfo("Gelijkspel!", "Gelijkspel")
        flag = 0
        btn1["text"] = " " # Getting value from each button,
        btn2["text"] = " " # to check for any possible win event
        btn3["text"] = " "
        btn4["text"] = " "
        btn5["text"] = " "
        btn6["text"] = " "
        btn7["text"] = " "
        btn8["text"] = " "
        btn9["text"] = " "

def win(player):
    ans = "Spel voltooid, speler " + player + " wint !!!"
    messagebox.showinfo("Winnaar!!!", ans)
    global flag
    flag = 0
    btn1["text"] = " " # Getting value from each button,
    btn2["text"] = " " # to check for any possible win event
    btn3["text"] = " "
    btn4["text"] = " "
    btn5["text"] = " "
    btn6["text"] = " "
    btn7["text"] = " "
    btn8["text"] = " "
    btn9["text"] = " "
    

btn1 = Button(boterkaasei, text=" ", bg="orange", fg="Black", width=3, height=1, font=('Helvetica', '20'), command=clicked1)
btn1.grid(column=1, row=1)
btn2 = Button(boterkaasei, text=" ", bg="orange", fg="Black", width=3, height=1, font=('Helvetica', '20'), command=clicked2)
btn2.grid(column=2, row=1)
btn3 = Button(boterkaasei, text=" ", bg="orange", fg="Black", width=3, height=1, font=('Helvetica', '20'), command=clicked3)
btn3.grid(column=3, row=1)
btn4 = Button(boterkaasei, text=" ", bg="orange", fg="Black", width=3, height=1, font=('Helvetica', '20'), command=clicked4)
btn4.grid(column=1, row=2)
btn5 = Button(boterkaasei, text=" ", bg="orange", fg="Black", width=3, height=1, font=('Helvetica', '20'), command=clicked5)
btn5.grid(column=2, row=2)
btn6 = Button(boterkaasei, text=" ", bg="orange", fg="Black", width=3, height=1, font=('Helvetica', '20'), command=clicked6)
btn6.grid(column=3, row=2)
btn7 = Button(boterkaasei, text=" ", bg="orange", fg="Black", width=3, height=1, font=('Helvetica', '20'), command=clicked7)
btn7.grid(column=1, row=3)
btn8 = Button(boterkaasei, text=" ", bg="orange", fg="Black", width=3, height=1, font=('Helvetica', '20'), command=clicked8)
btn8.grid(column=2, row=3)
btn9 = Button(boterkaasei, text=" ", bg="orange", fg="Black", width=3, height=1, font=('Helvetica', '20'), command=clicked9)
btn9.grid(column=3, row=3)

flag = 0  # Flag used to apeend (1) in every turn is occurred
# MAIN --------------------------------
# Begin met frame 1
show_thing_1()
# Start the application
window.mainloop()