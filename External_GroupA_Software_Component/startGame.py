from logging import root
import tkinter as tk
from tkinter import ttk
from tkinter import *
from player import Player
from gameBoard import *
from playinput import *
from game import *


class RuleWindow(tk.Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.geometry('700x300')
        self.title('Rules')

        scrollbar = tk.Scrollbar(master=self, orient='vertical')
        scrollbar.pack(side=tk.RIGHT, fill='y')

        text = tk.Text(master=self, height=200, width=80, yscrollcommand=scrollbar.set)
        text.pack(side=tk.LEFT)

        fileRulebook = open('rules.md', encoding='utf8')
        text.insert(tk.END, fileRulebook.read())
        text.config(state='disabled')
            

class Window(tk.Toplevel):
    def __init__(self, parent, mainwindow):
        super().__init__(parent)
        self.geometry('200x100')
        self.title('Draw window')
        self.mainwindow = mainwindow
        ttk.Button(self,
                   text='Yes',
                   command=self.acceptDraw).pack(expand=True)
        ttk.Button(self,
                   text='No',
                   command=self.denyDraw).pack(expand=True)
        
        ttk.Button(self,
                   text='Exit',
                   command=self.exit).pack(expand=True)

    def acceptDraw(self):
        print('The player has accepted the draw')
        #initiate draw
        self.destroy()
        self.mainwindow.destroy()
    
    def denyDraw(self):
        print('The player has denied the draw')
        self.destroy()

    def exit(self):
        self.destroy()

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('500x400')
        self.title('Home')

        ttk.Button(self,
                   text='Start Game',
                   command=self.startGame).pack(expand=True)
        ttk.Button(self,
                   text='Rules',
                   command=self.open_rules).pack(expand=True)
        ttk.Button(self,
                   text='Exit the game',
                   command=self.exit).pack(expand=True)
    
    def startGame(self):
        print("From Menu")
        draw = Window(self,self)
        draw.grab_set()
        gameRunner()
    
    def open_rules(self):
        window = RuleWindow(self)
        window.grab_set()
    
    def exit(self):
        self.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()