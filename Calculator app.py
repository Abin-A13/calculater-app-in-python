from tkinter import *
win = Tk()
type_Box = Entry(win)
type_Box.grid(row=0, columnspan=7)#using grid to align properly
"""function for user input"""
i=0
def get_values(num):
    global i
    type_Box.insert(i,num)
    i += 1
"""adding clear function"""
def clear_all():
     type_Box.delete(0,END)
"""Add buttons and color to them """
Button(text="c",fg="black",bg="yellow").grid(row=1,column=0)
Button(text="+/-",fg="black",bg="yellow").grid(row=1,column=1)
Button(text="%",fg="black",bg="yellow").grid(row=1,column=2)
Button(text="DEL",fg="black",bg="yellow").grid(row=1,column=3)
Button(text="7",fg="black",bg="yellow",command=lambda :get_values(7)).grid(row=2,column=0)
Button(text="8",fg="black",bg="yellow",command=lambda :get_values(8)).grid(row=2,column=1)
Button(text="9",fg="black",bg="yellow",command=lambda :get_values(9)).grid(row=2,column=2)
Button(text="4",fg="black",bg="yellow",command=lambda :get_values(4)).grid(row=3,column=0)
Button(text="5",fg="black",bg="yellow",command=lambda :get_values(5)).grid(row=3,column=1)
Button(text="6",fg="black",bg="yellow",command=lambda :get_values(6)).grid(row=3,column=2)
Button(text="3",fg="black",bg="yellow",command=lambda :get_values(3)).grid(row=4,column=0)
Button(text="2",fg="black",bg="yellow",command=lambda :get_values(2)).grid(row=4,column=1)
Button(text="1",fg="black",bg="yellow",command=lambda :get_values(1)).grid(row=4,column=2)
Button(text="c",fg="black",bg="yellow",command=lambda :clear_all()).grid(row=1,column=0)
"""add operators """
Button(text="/",fg="dark red",bg="light grey").grid(row=2,column=3)
Button(text="*",fg="dark red",bg="light grey").grid(row=3,column=3)
Button(text="-",fg="dark red",bg="light grey").grid(row=4,column=3)
Button(text="+",fg="dark red",bg="light grey").grid(row=5,column=3)
"""signes add"""
Button(text="=",fg="white",bg="dark red").grid(row=5,column=2)
Button(text=".",fg="black",bg="yellow").grid(row=5,column=1)
Button(text="0",fg="black",bg="yellow",command=lambda :get_values(0)).grid(row=5,column=0)

win.mainloop()
