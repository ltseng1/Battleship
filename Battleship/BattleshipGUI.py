from tkinter import *
from shipPlace import *
from Gameboard import *
import tkinter.messagebox
from random import *
from Player import *
import sys
import os


class BattleshipGUI(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.master.geometry("250x200")
        self.master.title("Battleship")

        self.w = Canvas(width=250, height=200, bg="grey")
        self.w.pack()

        self.playGame = Button(self.w, text="Begin Game",
                               command=self.newWindow)
        self.window = self.w.create_window(88, 145, window=self.playGame)
        self.quit = Button(self.w, text="Quit", command=quit)
        self.window2 = self.w.create_window(168, 145, window=self.quit)
        self.w.create_text(125, 80, text="Battleship",
                           font=("MS Serif", "40", "bold"), justify="center")

    def newWindow(self):
        self.master.geometry("500x700")
        self.w.delete("all")
        self.w.config(width=1000, height=700)

        self.Player = Player()
        self.Comp = Player()
        self.hit = False
        self.compRow = 0
        self.compCol = 0
        self.hitDirection = 1
        self.hitCount = 1

        alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        y = 70
        for elem in alphabet:
            self.w.create_text(25, y, text=elem,
                               font=("MS Serif", "14", "bold"))
            y += 40

        x = 70
        for y in range(1, 11):
            self.w.create_text(x, 25, text=str(y),
                               font=("MS Serif", "14", "bold"))
            x += 40

        self.button1 = Button(self.w, text="Place Ships",
                              command=self.shipPlacement, bg="grey")
        self.button1Window = self.w.create_window(250, 500,
                                                  window=self.button1)
        self.button2 = Button(self.w, text="Quit", command=quit)
        self.button2Window = self.w.create_window(213, 660,
                                                  window=self.button2)
        self.button3 = Button(self.w, text="Restart", command=self.restart)
        self.button3Window = self.w.create_window(277, 660,
                                                  window=self.button3)

        self.userLabel = self.w.create_text(250, 468, text="User Board",
                                            font=("MS Serif", "14", "bold"))

        x = 50
        y = 50
        self.playerL = []
        for a in range(1, 101):
            b = self.w.create_rectangle(x, y, x+40, y+40, fill="dodger blue")
            if a % 10 == 0:
                x = 50
                y += 40
            else:
                x += 40
            self.playerL.append(b)

        self.radioGet = IntVar()
        self.LabelEntry1 = self.w.create_text(268, 535, text="Enter letter:",
                                              justify="right")
        self.entryY = Entry(self.w, width=9, justify="center")
        self.entryWindowY = self.w.create_window(360, 535, window=self.entryY)
        self.LabelEntry2 = self.w.create_text(260, 565, text="Enter number:",
                                              justify="right")
        self.entryX = Entry(self.w, width=9, justify="center")
        self.entryWindowX = self.w.create_window(360, 565, window=self.entryX)
        self.radioButtonDown = Radiobutton(self.w, text="Down", value=1,
                                           width=7,
                                           justify="left",
                                           variable=self.radioGet)
        self.LabelRadio = self.w.create_text(275, 608, text="Direction:")
        self.radioWindow = self.w.create_window(350, 600,
                                                window=self.radioButtonDown)
        self.radioButtonRight = Radiobutton(self.w, text="Right", value=2,
                                            width=7,
                                            justify="left",
                                            variable=self.radioGet)
        self.radioWindow2 = self.w.create_window(349, 624,
                                                 window=self.radioButtonRight)

        self.shipLabel = self.w.create_text(120, 545,
                                            text="Placing Aircr" +
                                            "aft Carrier:\n" +
                                            "(5 long)", justify="center")

        self.counter = 0
        self.playerGrid = Grid()
        self.computerGrid = Grid()

    def restart(self):
        python = sys.executable
        os.execl(python, python,  * sys.argv)

    def quit(self):
        destroy()

    def shipPlacement(self):
        self.ships = [5, 4, 3, 3, 2]
        self.letters = {"A": "0", "B": "1", "C": "2", "D": "3", "E": "4",
                        "F": "5", "G": "6", "H": "7", "I": "8", "J": "9"}
        try:
            newBoard = shipPlace(self.playerGrid,
                                 self.letters[self.entryY.get().upper()],
                                 int(self.entryX.get()) - 1,
                                 self.radioGet.get(), self.ships[self.counter])
        except:
            tkinter.messagebox.showerror("Error", "Enter correct coordinates.")
        else:
            if not newBoard:
                tkinter.messagebox.showerror("Error",
                                             "Ship placed incorrectly.")
            else:
                self.colorBoard()
                if self.counter == 5:
                    self.resetBoard()
                    self.computerBoard()

    def colorBoard(self):
        self.shipNames = ["Aircraft Carrier (5 long)", "Battleship (4 long)",
                          "Submarine (3 long)",
                          "Destroyer (3 long)", "Patrol Boat (2 long)"]
        for x in range(self.ships[self.counter]):
            row = self.letters[self.entryY.get().upper()]
            col = self.entryX.get()
            if self.radioGet.get() == 1:
                listIndex = str(int(row) + x) + \
                    str(int(col) - 1)
                self.w.itemconfigure(self.playerL[int(listIndex)],
                                     fill="grey")
            else:
                listIndex = row + \
                            str((int(col)) + x - 1)
                self.w.itemconfigure(self.playerL[int(listIndex)],
                                     fill="grey")
        self.counter += 1
        try:
            self.w.itemconfigure(self.shipLabel,
                                 text="Placing " +
                                 self.shipNames[self.counter] + ":")
        except:
            self.w.itemconfigure(self.shipLabel, text="Now Attacking",
                                 font=("MS Serif", "14", "bold"),
                                 justify="center", fill="red")
            self.w.coords(self.shipLabel, 500, 468)

    def computerBoard(self):
        for x in range(5):
            direction = randint(1, 2)
            if direction == 1:
                y = 0
                while y == 0:
                    row = randint(0, 10 - self.ships[x])
                    column = randint(0, 9)
                    newBoard = shipPlace(self.computerGrid, row, column,
                                         direction, self.ships[x])
                    if newBoard:
                        # To display comp ships
                        # for z in range(self.ships[x]):
                        #    listIndex = str(row + z) + str(column)
                        #    self.w.itemconfigure(self.compL[int(listIndex)],
                        #                        fill="grey")
                        y += 1
            else:
                y = 0
                while y == 0:
                    row = randint(0, 9)
                    column = randint(0, 10 - self.ships[x])
                    newBoard = shipPlace(self.computerGrid, row, column,
                                         direction, self.ships[x])
                    if newBoard:
                        # for z in range(self.ships[x]):
                        #    listIndex = str(row) + str(column + z)
                        #    self.w.itemconfigure(self.compL[int(listIndex)],
                        #                         fill="grey")
                        y += 1

    def resetBoard(self):
        self.master.geometry("1000x700")
        self.w.delete(self.button1Window)
        self.w.delete(self.radioWindow)
        self.w.delete(self.radioWindow2)
        self.w.delete(self.LabelRadio)
        self.entryX.delete(0, END)
        self.entryY.delete(0, END)
        self.attack = Button(self.w, text="Attack", command=self.attack)
        self.attackWindow = self.w.create_window(250, 500, window=self.attack)
        self.w.coords(self.LabelEntry1, 203, 536)
        self.w.coords(self.LabelEntry2, 195, 564)
        self.w.coords(self.button2Window, 217, 600)
        self.w.coords(self.button3Window, 281, 600)
        self.w.coords(self.entryWindowY, 360, 540)
        self.w.coords(self.entryWindowX, 360, 570)
        self.w.coords(self.entryWindowY, 290, 535)
        self.w.coords(self.entryWindowX, 290, 565)

        alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        y = 70
        for elem in alphabet:
            self.w.create_text(975, y, text=elem,
                               font=("MS Serif", "14", "bold"))
            y += 40

        x = 570
        for y in range(1, 11):
            self.w.create_text(x, 25, text=str(y),
                               font=("MS Serif", "14", "bold"))
            x += 40

        self.userLabel = self.w.create_text(750, 468, text="Computer Board",
                                            font=("MS Serif", "14", "bold"))

        x = 550
        y = 50
        self.compL = []
        for a in range(1, 101):
            b = self.w.create_rectangle(x, y, x+40, y+40, fill="dodger blue")
            if a % 10 == 0:
                x = 550
                y += 40
            else:
                x += 40
            self.compL.append(b)

    def attack(self):
        self.shipNames2 = ["Patrol Boat", "Destroyer", "Submarine",
                           "Battleship", "Aircraft Carrier"]
        try:
            row = self.letters[self.entryY.get().upper()]
            col = int(self.entryX.get()) - 1
            if self.computerGrid.checkAttack(int(row), col):
                result = self.computerGrid.attack(int(row), col)
                if result[0] and len(result) == 1:
                    self.w.itemconfigure(self.compL[int(row + str(col))],
                                         fill="red")
                    self.Player.setHits(self.Player.getHits() + 1)
                    self.Player.setShots(self.Player.getShots() + 1)
                    self.compAttack()
                    self.entryX.delete(0, END)
                    self.entryY.delete(0, END)
                elif result[0] and len(result) != 1:
                    self.w.itemconfigure(self.compL[int(row + str(col))],
                                         fill="red")
                    self.Player.setHits(self.Player.getHits() + 1)
                    self.Player.setShots(self.Player.getShots() + 1)
                    tkinter.messagebox.showinfo("Sunk Battleship",
                                                "You sunk the " +
                                                self.shipNames2[result[1] - 2])
                    if self.Player.getHits() == 17:
                        hits = self.Player.getHits()
                        shots = self.Player.getShots()
                        percent = self.Player.getPercentHit()
                        tkinter.messagebox.showinfo("Winner",
                                                    "You won!\nStatistics:\n" +
                                                    "  Hits: " +
                                                    str(hits) +
                                                    "\n  Shots: " +
                                                    str(shots) +
                                                    "\n  Percent hit: " +
                                                    str(percent))
                    else:
                        self.compAttack()
                    self.entryX.delete(0, END)
                    self.entryY.delete(0, END)
                else:
                    self.w.itemconfigure(self.compL[int(row + str(col))],
                                         fill="white")
                    self.Player.setShots(self.Player.getShots() + 1)
                    self.compAttack()
                    self.entryX.delete(0, END)
                    self.entryY.delete(0, END)
            else:
                tkinter.messagebox.showerror("Error", "You have already" +
                                             " shot there. Please try again.")
        except:
            tkinter.messagebox.showerror("Error", "Incorrect coordinates. " +
                                         "Please try again.")

    def compAttack(self):
        if self.hit:
            self.smartCompAttack()
        else:
            self.compRandAttack()

    def smartCompAttack(self):
        y = 0
        while y == 0:
            if self.hitDirection == 1:
                try:
                    result = self.smartDown()
                    if result:
                        y += 1
                    else:
                        pass
                except:
                    if self.hitCount == 1:
                        self.hitDirection += 1
                    else:
                        self.hitDirection = 1
                        self.compRandAttack()
                        y += 1
            elif self.hitDirection == 2:
                try:
                    result = self.smartRight()
                    if result:
                        y += 1
                    else:
                        pass
                except:
                    if self.hitCount == 1:
                        self.hitDirection += 1
                    else:
                        self.hitDirection = 1
                        self.hitCount = 1
                        self.compRandAttack()
                        y += 1
            elif self.hitDirection == 3:
                try:
                    result = self.smartUp()
                    if result:
                        y += 1
                    else:
                        pass
                except:
                    if self.hitCount == 1:
                        self.hitDirection += 1
                    else:
                        self.hitDirection = 1
                        self.hitCount = 1
                        self.compRandAttack()
                        y += 1
            elif self.hitDirection == 4:
                try:
                    result = self.smartLeft()
                    if result:
                        y += 1
                    else:
                        pass
                except:
                    if self.hitCount == 1:
                        self.hitDirection += 1
                    else:
                        self.hitDirection = 1
                        self.hitCount = 1
                        self.compRandAttack()
                        y += 1

    def compRandAttack(self):
        y = 0
        while y == 0:
            self.compRow = randint(0, 9)
            self.compCol = randint(0, 9)
            if self.playerGrid.checkAttack(self.compRow, self.compCol):
                if self.playerGrid.attack(self.compRow, self.compCol)[0]:
                    self.w.itemconfigure(self.playerL[int(str(self.compRow) +
                                                          str(self.compCol))],
                                         fill="red")
                    self.Comp.setHits(self.Comp.getHits() + 1)
                    y += 1
                    self.hit = True
                    self.hitDirection = 1
                    if self.Comp.getHits() == 17:
                        hits = self.Player.getHits()
                        shots = self.Player.getShots()
                        percent = self.Player.getPercentHit()
                        tkinter.messagebox.showinfo("Loser",
                                                    "You lost." +
                                                    "\nStatistics:\n" +
                                                    "  Hits: " +
                                                    str(hits) +
                                                    "\n  Shots: " +
                                                    str(shots) +
                                                    "\n  Percent hit: " +
                                                    str(percent))
                else:
                    self.w.itemconfigure(self.playerL[int(str(self.compRow) +
                                                          str(self.compCol))],
                                         fill="white")
                    y += 1
                    self.hit = False
                    self.hitDirection = 1

    def smartDown(self):
        if self.playerGrid.checkAttack(self.compRow + self.hitCount,
                                       self.compCol):
            if self.playerGrid.attack(self.compRow + self.hitCount,
                                      self.compCol)[0]:
                self.w.itemconfigure(self.playerL[int(str(self.compRow +
                                                          self.hitCount) +
                                                      str(self.compCol))],
                                     fill="red")
                self.Comp.setHits(self.Comp.getHits() + 1)
                self.hit = True
                self.hitCount += 1
                if self.Comp.getHits() == 17:
                    hits = self.Player.getHits()
                    shots = self.Player.getShots()
                    percent = self.Player.getPercentHit()
                    tkinter.messagebox.showinfo("Loser",
                                                "You lost." +
                                                "\nStatistics:\n" +
                                                "  Hits: " +
                                                str(hits) +
                                                "\n  Shots: " +
                                                str(shots) +
                                                "\n  Percent hit: " +
                                                str(percent))
                return True
            else:
                self.w.itemconfigure(self.playerL[int(str(self.compRow +
                                                          self.hitCount) +
                                                      str(self.compCol))],
                                     fill="white")
                if self.hitCount == 1:
                    self.hitDirection += 1
                    return True
                else:
                    self.hitDirection = 1
                    self.hit = False
                    self.hitCount = 1
                    return True
        else:
            if self.hitCount == 1:
                self.hitDirection += 1
            else:
                self.compRandAttack()
                self.hitCount = 1
                self.hitDirection = 1
                return True

    def smartRight(self):
        if self.playerGrid.checkAttack(self.compRow, self.compCol +
                                       self.hitCount):
            if self.playerGrid.attack(self.compRow, self.compCol +
                                      self.hitCount)[0]:
                self.w.itemconfigure(self.playerL[int(str(self.compRow) +
                                                      str(self.compCol +
                                                          self.hitCount))],
                                     fill="red")
                self.Comp.setHits(self.Comp.getHits() + 1)
                self.hit = True
                self.hitCount += 1
                if self.Comp.getHits() == 17:
                    hits = self.Player.getHits()
                    shots = self.Player.getShots()
                    percent = self.Player.getPercentHit()
                    tkinter.messagebox.showinfo("Loser",
                                                "You lost." +
                                                "\nStatistics:\n" +
                                                "  Hits: " +
                                                str(hits) +
                                                "\n  Shots: " +
                                                str(shots) +
                                                "\n  Percent hit: " +
                                                str(percent))
                return True
            else:
                self.w.itemconfigure(self.playerL[int(str(self.compRow) +
                                                      str(self.compCol +
                                                          self.hitCount))],
                                     fill="white")
                if self.hitCount == 1:
                    self.hitDirection += 1
                    return True
                else:
                    self.hitDirection = 1
                    self.hit = False
                    self.hitCount = 1
                    return True
        else:
            if self.hitCount == 1:
                self.hitDirection += 1
            else:
                self.compRandAttack()
                self.hitCount = 1
                self.hitDirection = 1
                return True

    def smartUp(self):
        if self.playerGrid.checkAttack(self.compRow - self.hitCount,
                                       self.compCol):
            if self.playerGrid.attack(self.compRow - self.hitCount,
                                      self.compCol)[0]:
                self.w.itemconfigure(self.playerL[int(str(self.compRow -
                                                          self.hitCount) +
                                                      str(self.compCol))],
                                     fill="red")
                self.Comp.setHits(self.Comp.getHits() + 1)
                self.hit = True
                self.hitCount += 1
                if self.Comp.getHits() == 17:
                    hits = self.Player.getHits()
                    shots = self.Player.getShots()
                    percent = self.Player.getPercentHit()
                    tkinter.messagebox.showinfo("Loser",
                                                "You lost." +
                                                "\nStatistics:\n" +
                                                "  Hits: " +
                                                str(hits) +
                                                "\n  Shots: " +
                                                str(shots) +
                                                "\n  Percent hit: " +
                                                str(percent))
                return True
            else:
                self.w.itemconfigure(self.playerL[int(str(self.compRow -
                                                          self.hitCount) +
                                                      str(self.compCol))],
                                     fill="white")
                if self.hitCount == 1:
                    self.hitDirection += 1
                    return True
                else:
                    self.hitDirection = 1
                    self.hit = False
                    self.hitCount = 1
                    return True
        else:
            if self.hitCount == 1:
                self.hitDirection += 1
                return True
            else:
                self.compRandAttack()
                self.hitCount = 1
                self.hitDirection = 1
                return True

    def smartLeft(self):
        if self.playerGrid.checkAttack(self.compRow,
                                       self.compCol - self.hitCount):
            if self.playerGrid.attack(self.compRow,
                                      self.compCol - self.hitCount)[0]:
                self.w.itemconfigure(self.playerL[int(str(self.compRow) +
                                                      str(self.compCol -
                                                          self.hitCount))],
                                     fill="red")
                self.Comp.setHits(self.Comp.getHits() + 1)
                self.hit = True
                self.hitCount += 1
                if self.Comp.getHits() == 17:
                    hits = self.Player.getHits()
                    shots = self.Player.getShots()
                    percent = self.Player.getPercentHit()
                    tkinter.messagebox.showinfo("Loser",
                                                "You lost." +
                                                "\nStatistics:\n" +
                                                "  Hits: " +
                                                str(hits) +
                                                "\n  Shots: " +
                                                str(shots) +
                                                "\n  Percent hit: " +
                                                str(percent))
                return True
            else:
                self.w.itemconfigure(self.playerL[int(str(self.compRow) +
                                                      str(self.compCol -
                                                          self.hitCount))],
                                     fill="white")
                if self.hitCount == 1:
                    self.compRandAttack()
                    return True
                else:
                    self.hitDirection = 1
                    self.hit = False
                    self.hitCount = 1
                    return True
        else:
            if self.hitCount == 1:
                self.compRandAttack()
                self.hitDirection = 1
                return True
            else:
                self.compRandAttack()
                self.hitCount = 1
                self.hitDirection = 1
                return True
