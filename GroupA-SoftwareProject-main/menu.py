import tkinter as tk
from tkinter import ttk
from player import Player




class Window(tk.Toplevel):
    def __init__(self, parent, mainwindow):
        super().__init__(parent)
        self.geometry('300x100')
        self.title('Draw window')
        self.mainwindow = mainwindow
        ttk.Button(self,
                   text='Yes',
                   command=self.acceptDraw).pack(expand=True)
        ttk.Button(self,
                   text='No',
                   command=self.denyDraw).pack(expand=True)

    def acceptDraw(self):
        print('The player ', players[1][0], ' has accepted the draw')
        #initiate draw
        self.destroy()
        self.mainwindow.destroy()
    
    def denyDraw(self):
        print('The player ', players[1][0], ' has denied the draw')
        self.destroy()


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('300x200')
        self.title('Main Window')

        # place a button on the root window

        ttk.Button(self,
                   text='Draw',
                   command=self.open_window).pack(expand=True)

        ttk.Button(self,
                   text='Exit the game',
                   command=self.Exited).pack(expand=True)

    def open_window(self):
        print('Player ',players[0][0],' has requested a draw')
        window = Window(self,self)
        window.grab_set()

    

    def Exited(self):
        print('The player ', players[0][0], ' has exited the game')
        self.destroy()
        # end game function


# temp creation of players
player1 = ['Calle', True]
player2 = ['Bobby', False]
players = [player1, player2]

# Creates menu
if __name__ == "__main__":
    app = App()
    app.mainloop()
