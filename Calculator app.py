from tkinter import *
import parser
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
"""undo function for del key"""
def undo():
    full_string=type_Box.get()
    if len(full_string):
        new_string=full_string[:-1]
        clear_all()
        type_Box.insert(0, new_string)
    else:
        clear_all()
        type_Box.insert(0, "invalid key")
"""operaters funtion for user input"""
def operat(opr):
    global i
    length = len(opr)
    type_Box.insert(i, opr)
    i += length
"""for equation action import parser for compile expertion"""
def equalls():
    all_string = type_Box.get()
    try:        #make the funtion exception
        n = parser.expr(all_string).compile()
        result = eval(n)
        clear_all()
        type_Box.insert(0, result)
    except Exception:
        clear_all()
        type_Box.insert(0, "calculation error")
"""additional plus or minus key"""
def plus_minus(op):
    global i
    op1 = len(op)
    type_Box.insert(i, op)
    i += op1
"""Add buttons and color to them"""
Button(text="c",fg="black",bg="yellow",command=lambda :clear_all()).grid(row=1,column=0)
Button(text="&",fg="black",bg="yellow",command=lambda:plus_minus('&')).grid(row=1,column=1)
Button(text="%",fg="black",bg="yellow",command=lambda :operat('%')).grid(row=1,column=2)
Button(text="DEL",fg="black",bg="yellow",command=lambda :undo()).grid(row=1,column=3)
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
Button(text="/",fg="dark red",bg="light grey",command=lambda :operat('/')).grid(row=2,column=3)
Button(text="*",fg="dark red",bg="light grey",command=lambda :operat('*')).grid(row=3,column=3)
Button(text="-",fg="dark red",bg="light grey",command=lambda :operat('-')).grid(row=4,column=3)
Button(text="+",fg="dark red",bg="light grey",command=lambda :operat('+')).grid(row=5,column=3)
"""signes add"""
Button(text="=",fg="white",bg="dark red",command=lambda :equalls()).grid(row=5,column=2)
Button(text=".",fg="black",bg="yellow",command=lambda :get_values('.')).grid(row=5,column=1)
Button(text="0",fg="black",bg="yellow",command=lambda :get_values(0)).grid(row=5,column=0)

win.mainloop()
