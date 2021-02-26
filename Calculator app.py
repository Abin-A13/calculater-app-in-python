from tkinter import *
win = Tk()
type_Box = Entry(win)
type_Box.grid(row=0, columnspan=7)#using grid to align properly
"""Add buttons and color to them """
Button(text="c",fg="black",bg="yellow").grid(row=1,column=0)
Button(text="+/-",fg="black",bg="yellow").grid(row=1,column=1)
Button(text="%",fg="black",bg="yellow").grid(row=1,column=2)
Button(text="DEL",fg="black",bg="yellow").grid(row=1,column=3)
Button(text="7",fg="black",bg="yellow").grid(row=2,column=0)
Button(text="8",fg="black",bg="yellow").grid(row=2,column=1)
Button(text="9",fg="black",bg="yellow").grid(row=2,column=2)
Button(text="4",fg="black",bg="yellow").grid(row=3,column=0)
Button(text="5",fg="black",bg="yellow").grid(row=3,column=1)
Button(text="6",fg="black",bg="yellow").grid(row=3,column=2)
Button(text="3",fg="black",bg="yellow").grid(row=4,column=0)
Button(text="2",fg="black",bg="yellow").grid(row=4,column=1)
Button(text="1",fg="black",bg="yellow").grid(row=4,column=2)
Button(text="c",fg="black",bg="yellow").grid(row=1,column=0)

win.mainloop()
