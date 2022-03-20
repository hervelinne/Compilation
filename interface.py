import tkinter
from click import command
from myLexer import MyLexer
from myParser import MyParser
import sys
from os import path
from tkinter import ttk  
from tkinter import *

myLex = MyLexer()
lex = myLex.lexer
myPars = MyParser(myLex)
parser = myPars.parser
import tkinter.simpledialog as sd

def start():
    root = tkinter.Tk()
  
    root.geometry("500x500")
    panedwindow=ttk.Panedwindow(root, orient=tkinter.HORIZONTAL)  
    panedwindow.pack(fill=tkinter.BOTH, expand=True)  
    fram1=ttk.Frame(panedwindow, width=500, height=500, relief=tkinter.GROOVE)  
    panedwindow.add(fram1, weight=1)  
    
    fram2 = tkinter.Frame(root, relief=tkinter.GROOVE, height=100)
    fram2.pack(ipadx=15, ipady=1, side="bottom", fill="x")

    T = tkinter.Text(fram1)
    
    T.pack(fill=tkinter.BOTH, expand=True)

    def compileInput():
        line = T.get("1.0","end-1c")
        parsing(line)
    tkinter.Button(fram2, text="run", width = 100,  bg="silver", command=compileInput).pack(ipadx=5,ipady=10, side="bottom")  
    tkinter.mainloop()
    
def parsing(input):
    #print(line)
    r=parser.parse(input)
    print(r)

start()