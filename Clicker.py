from cProfile import label
from math import perm
from re import L
from tabnanny import check
import tkinter
from tkinter import *
from tkinter.font import Font
from tkinter import ttk
from unittest import TextTestResult
import os.path
import threading

def check_values():
    global perm_power
    global clicked
    global click_power
    global rebirthamount
    global rebirths
    global rebirthtoken
    global perm_poweradd
    global extramoney
    global autoclickcheck

    if os.path.exists("DATAclicks.txt") == True:
        pass
    else:
        saveclicks = open("DATAclicks.txt", "w")
        saveclicks.writelines(["0", "\n1", "\n1000000", "\n0", "\n0", "\n0", "\n0"])
        saveclicks.close()


    saveclicks = open("DATAclicks.txt", "r")
    val1clicks = saveclicks.readlines()
    val1clickspower = saveclicks.readlines()

    with open("DATAclicks.txt") as f:
        [int(x) for x in f]
            
    perm_power = int(val1clicks[5])

    clicked = int(val1clicks[0])
    click_power = int(val1clicks[1]) + perm_power

    rebirthamount = int(val1clicks[2])
    rebirths = int(val1clicks[3])
    rebirthtoken = int(val1clicks[4])

    autoclickcheck = int(val1clicks[6])

    perm_poweradd = 2000

check_values()

checkifon = True


root = Tk()
root.config(bg="#697ace")

frame = Frame(root, bg="#697ace")
frame.grid(row=2, column=0, pady=10, padx=10, sticky="w")

frame2 = Frame(root, bg="#697ace")
frame2.grid(row=0, column=0, pady=10, padx=10, sticky="w")

rebirthshop = Frame(root, bg="#697ace")
rebirthshop.grid(row=1, column=2, pady=10, padx=10, sticky="w")

def timesclicked():
    global clicked
    global click_power
    

    clicked += int(int(click_power) * 1.1 ** int(rebirths))
    print(clicked)
    clicks.config(text=f"You Have Clicks: {clicked}")
    clicks.grid(row=1, column=0, pady=10, padx=10, sticky="w")

def more_click_power():
    global click_power
    global clicked

    if clicked < 200:
        return

    if combo.get() == "Multi Buy":
        combo.current(1)
    
    checkmoney = 0

    for x in range(int(combo.get())):

        checkmoney += 200

    if clicked < checkmoney:
        return

    for x in range(int(combo.get())):
        click_power += 1
        clicked = clicked - 200
    
    clicks.config(text=f"You Have Clicks: {clicked}")
    clickpower.config(text=f"Your Click Power is: {click_power}")

def rebirthadd():
    global rebirthamount
    global clicked
    global click_power
    global rebirths
    global rebirthtoken

    if clicked < rebirthamount:
        return

    clicked = 0 
    click_power = 1 + perm_power
    clicks.config(text=f"You Have Clicks: {clicked}")
    clickpower.config(text=f"Your Click Power is: {click_power}")
    
    rebirthamount += int(rebirthamount/4)
    rebirths += 1
    rebirthtoken += 1

    rebirth.config(text=f"Buy 1 Rebirth Coin ({rebirthamount})")
    rebirthlabl.config(text=f"Rebirths: {rebirths}")
    rebirthtokenlabl.config(text=f"Rebirths Tokens: {rebirthtoken}")

    print(rebirthamount)

def megapower():
    global rebirthtoken
    global click_power
    global perm_power

    if rebirthtoken < 2:
        return

    rebirthtoken = rebirthtoken - 2
    rebirthtokenlabl.config(text=f"Rebirths Tokens: {rebirthtoken}")
    perm_power += 2000
    click_power += perm_poweradd


    clickpower.config(text=f"You Click Power is: {click_power}")

def autoclickerbuy():
    global autoclickcheck
    global rebirthtoken

    rebirthtoken = rebirthtoken - 5
    rebirthtokenlabl.config(text=f"Rebirths Tokens: {rebirthtoken}")
    autoclickcheck += 1

def autoclicker():
    global clicked
    global click_power
    global checkifon

    if checkifon == False:
            print(checkifon)
            return

    while True:
        t = threading.Event()
        t.wait(0.5)

        clicked += int(int(click_power) * 1.1 ** int(rebirths))
        print(clicked)
        clicks.config(text=f"You Have Clicks: {clicked}")
        clicks.grid(row=1, column=0, pady=10, padx=10, sticky="w")

        checkifon = False


def autoclicker_start():
    global checkifon

    if autoclickcheck == 0:
        print(autoclickcheck)
        return         

    
    t = threading.Thread(target=autoclicker)
    t.start()

    

clickspot = Button(root, text="Click Me", width=50, height=10, bg="#69cea1", fg="white" ,command=timesclicked)
clickspot.grid(row=1, column=0, pady=10, padx=10, sticky="n")

clicks = Label(frame, text=f"You Have Clicks: {clicked}", bg="#697ace", fg="white")
clicks.grid(row=1, column=0, pady=10, padx=10, sticky="w")

morepower = Button(frame, text="Buy More Power (200)", bg="#697ace", fg="white", command=more_click_power)
morepower.grid(row=1, column=3, pady=10, padx=10, sticky="w")

clickpower = Label(frame, text=f"You Click Power is: {click_power}", bg="#697ace", fg="white")
clickpower.grid(row=2, column=0, pady=10, padx=10, sticky="w")

rebirth = Button(frame2, text=f"Buy 1 Rebirth Coin ({rebirthamount})", bg="#697ace", fg="white", command=rebirthadd)
rebirth.grid(row=0, column=0, pady=10, padx=2, sticky="w")

rebirthlabl = Label(frame2, text=f"Rebirths: {rebirths}", bg="#697ace", fg="white")
rebirthlabl.grid(row=0, column=1, pady=10, padx=10, sticky="w")

rebirthtokenlabl = Label(frame2, text=f"Rebirths Tokens: {rebirthtoken}", bg="#697ace", fg="white")
rebirthtokenlabl.grid(row=0, column=2, pady=10, padx=10, sticky="w")

megaclick = Button(rebirthshop, text="Mega Power (2 RebirthTokens) +2000 power", bg="#697ace", fg="white", command=megapower)
megaclick.grid(row=0, column=0, pady=10, padx=10, sticky="n")

autoclick = Button(rebirthshop, text="Auto Clicker(5 RebirthTokens)", bg="#697ace", fg="white", command=autoclickerbuy)
autoclick.grid(row=1, column=0, pady=10, padx=10, sticky="n")


# var = StringVar()

# autoclicktoggle = Checkbutton(frame, text="Toggle Auto Clicker", bg="#697ace", fg="white", variable=var, onvalue=autoclicker_start)
# autoclicktoggle.grid(row=1, column=4, pady=10, padx=10, sticky="n")
# autoclicktoggle.deselect()

selectauto = Button(frame, text="Toggle Auto Clicker", bg="#697ace", fg="white", command=autoclicker_start)
selectauto.grid(row=1, column=4, pady=10, padx=10, sticky="n")


options = [
    "Multi Buy",
    "1",
    "10",
    "25",
    "50",
    "100",
]

multbuy = StringVar()
multbuy.set(options[0])

combo = ttk.Combobox(frame, value=options)
combo.current(0)
combo.bind("<<ComboboxSelected>>")
combo.grid(row=2, column=3, pady=10, padx=10, sticky="w")



mainloop()

def save_values():
    saveclicks = open("DATAclicks.txt", "w")
    saveclicks.writelines([f"{clicked}", f"\n{click_power}", f"\n{rebirthamount}", f"\n{rebirths}", f"\n{rebirthtoken}", f"\n{perm_power}", f"\n{autoclickcheck}"])
    saveclicks.close()

save_values()
