#GUI For Data Project
from tkinter import *

def click():
    print("Something is happening")
###main:
window = Tk()
window.title("FDIC Data - DS5100")

def definitions():
    textOutput = "New Bank: A New Bank is a bank that has been created in the corresponding year. New banks have xyz.\n Failed Bank: A failed bank is a bank that has failed.\nLiquidated Bank: A bank that has been liquidated means that everyone inside has been turned into a giant smoothie to give to Jeff Besos to drink."
    output.insert(END, textOutput)
#create label
#include image
photo1 = PhotoImage(file="brand.gif")
Label(window, image=photo1, bg = "black").grid(row=0, column=0, sticky=E)

#create entry for years
Label(window, text= "Min Year:", bg="white", fg = "black", font="none 12 bold").grid(row=3,  column=2, sticky=W)
minyear = Entry(window, width = 10, bg = "white")
minyear.grid(row=3, column = 3, sticky =W)

Label(window, text= "Max Year:", bg="white", fg = "black", font="none 12 bold").grid(row=3,  column=4, sticky=W)
maxyear = Entry(window, width = 10, bg = "white")
maxyear.grid(row=3, column = 5, sticky =W)
#create label for text
Label(window, text= "See New Banks:", bg="white", fg = "black", font="none 12 bold").grid(row=6,  column=2, sticky=W)
Button(window, text="NEW BANKS", width = 15, command=click).grid(row=7, column = 3, sticky = W)
Label(window, text= "See Failed Banks:", bg="white", fg = "black", font="none 12 bold").grid(row=6,  column=4, sticky=W)
Button(window, text="FAILED BANKS", width = 15, command=click).grid(row=7, column = 5, sticky = W)
Label(window, text= "See Liquidated Banks:", bg="white", fg = "black", font="none 12 bold").grid(row=6,  column=6, sticky=W)
Button(window, text="LIQUIDATED BANKS", width = 15, command=click).grid(row=7, column = 7, sticky = W)


Label(window, text = "Definitions",bg="white", fg = "black", font="none 12 bold").grid(row=9,  column=6, sticky=W) 
Button(window, text="DEFINITIONS HELP", width = 30, command=definitions).grid(row=10, column = 6, columnspan=2, sticky = W)

output = Text(window, width=75, height=6, wrap = WORD, background = "white")
output.grid(row=11, column=6, columnspan=2, sticky=W)
window.mainloop()