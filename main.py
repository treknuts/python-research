# Author: Trevor Knutson
# Created on: 03/18/2020
# Description: Simple game in Python during the COVID-19 quarantine

import sys
from tkinter import *
from random import randint


class Game(Frame):

    def __init__(self, canvas):
        super().__init__()
        self.master.title("Python Game")
        self.pack(fill=BOTH, expand=1)

        self.canvas = canvas
        self.ball = self.canvas.create_oval(10, 10, 30, 30, fill="red")

    def move_ball(self):
        deltax = randint(0, 5)
        deltay = randint(0, 5)
        self.canvas.move(self.ball, deltax, deltay)
        self.after(40, self.move_ball)


def main():
    root = Tk()
    root.title("Python Game")
    root.resizable(False, False)
    canvas = Canvas(root, width=400, height=400)
    canvas.pack()

    game = Game(canvas)
    game.move_ball()
    root.mainloop()


if __name__ == '__main__':
    main()
