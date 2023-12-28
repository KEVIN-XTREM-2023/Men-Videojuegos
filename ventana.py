from tkinter import *
from typing import Sized
#from tkinter import messagebox
from Snake.snake import *
from SpaceDefenders.spaceDefenders import *
from Pong.pong import *

class Menu:
    def __init__(self, window):
        self.window = window
        self.window.geometry("650x550")
        self.window.title("Menu Games")
        self.window.resizable(0,0)
        self.frameSnake = None
        self.framePong = None
        self.frameSpaceDfs = None
        self.frameTitle = None
        self.headTitle = None
        self.titleSnake = None
        self.titlePong = None
        self.titleSpaceDfndrs = None
        self.btnSnake = None
        self.btnPong = None
        self.btnSpaceDfds = None
        self.btnRegistSnk = None
        self.btnRegistPng = None
        self.btnRegisSpDs = None
        self.btnExit = None
        self.widgetsMenu()
    
    def widgetsMenu(self):
        self.window.config(background="#5B8A72")
        self.frameSnake = Frame(self.window,bg="#28527A")
        self.frameSnake.place(x=80,y=100,height=100,width=500)
        self.framePong = Frame(self.window,bg="#28527A")
        self.framePong.place(x=80,y=250,height=100,width=500)
        self.frameSpaceDfs = Frame(self.window,bg="#28527A")
        self.frameSpaceDfs.place(x=80,y=400,height=100,width=500)
        self.frameTitle = Frame(self.window,bg="#28527A")
        self.frameTitle.place(x=185,y=25,height=50,width=300)
        self.headTitle = Label(self.frameTitle,text="Menu de Juegos", 
                    font=("time new roman",20,"bold"),fg="#5B8A72",bg="#28527A")
        self.headTitle.place(x=41,y=6)
        self.titleSnake = Label(self.frameSnake,text="SNAKE",
                    font=("time new roman",22,"bold"),fg="#5B8A72",bg="#28527A")
        self.titleSnake.place(x=80,y=32)
        self.titlePong = Label(self.framePong,text="PONG",
                    font=("time new roman",22,"bold"),fg="#5B8A72",bg="#28527A")
        self.titlePong.place(x=82,y=32)
        self.titleSpaceDfndrs = Label(self.frameSpaceDfs,text="SPACE DEFENDERS",
                    font=("time new roman",17,"bold"),fg="#5B8A72",bg="#28527A")
        self.titleSpaceDfndrs.place(x=10,y=35)
        self.btnSnake = Button(self.frameSnake,command=self.playSnake,text="JUGAR",fg="black",
                    bg="#EBEDEF", font=("times new roman",15))
        self.btnSnake.place(x=250,y=35)
        self.btnRegistSnk = Button(self.frameSnake,command=None,text="REGISTRO", fg="black",
                    bg="#EBEDEF",font=("times new roman",15))
        self.btnRegistSnk.place(x=358,y=35)
        self.btnPong = Button(self.framePong,command=self.playPong,text="JUGAR",fg="black",
                    bg="#EBEDEF",font=("times new roman",15))
        self.btnPong.place(x=250,y=35)
        self.btnRegistPng = Button(self.framePong,command=None,text="REGISTRO",fg="black",
                    bg="#EBEDEF",font=("times new roman",15))
        self.btnRegistPng.place(x=358,y=35)
        self.btnSpaceDfds= Button(self.frameSpaceDfs,command=self.playSpaceDefedrs,text="JUGAR",fg="black",
                    bg="#EBEDEF",font=("times new roman",15))
        self.btnSpaceDfds.place(x=250,y=35)
        self.btnRegisSpDs = Button(self.frameSpaceDfs,command=None,text="REGISTRO",fg="black",
                    bg="#EBEDEF",font=("times new roman",15))
        self.btnRegisSpDs.place(x=358,y=35)

    def playSnake(self):
        runSnake()

    def playPong(self):
        runPong()
        
    def playSpaceDefedrs(self):
        #self.window.withdraw()
        runSpace()
        
root = Tk() 
Menu(root)
root.mainloop()     
