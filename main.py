import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import random

from PIL import ImageTk, Image
from pathlib import Path

userScore = 0
computerScore = 0

class MainGame(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        mainWidth = self.winfo_screenwidth()
        mainHeight = self.winfo_screenheight()
        menu_size = f'{mainWidth}x{mainHeight}'
        self.game_size = f'{mainHeight}x{mainHeight}'
        self.geometry(menu_size)
        self.title('Rock, Paper and Scissors')


    def startMainGame(self):
        global entry
        global string

        topName = tk.Label(self, text="Please tell me your topName :", font=("Courier 22 bold"))
        initilizeTheGame = tk.Button(self, text='Start Game')
        initilizeTheGame.place(relheight=0.1, relwidth=0.2, rely=0.7, relx=0.4)
        topName.pack(side=tk.TOP, pady=100)

        initilizeTheGame['command'] = lambda: self.startingThemenu()

        entry = tk.Entry(self, width=100)
        entry.focus_set()
        entry.pack(side=TOP)

    def startingThemenu(self):
        string = entry.get()
        global playerImageLoaded, playerPaper, pl_pick, playerRock, playerScissors, playerPaper, rockImage, computerPicker, computerScissor, computerScoreCurrent, computerPaper, computerCurrentImage, resultingScore, scoringLabel
        global userScore , pcScore
        pl_score = 0
        computerScoreCurrent = 0
        rockImage = ImageTk.PhotoImage(Image.open('rock.jpeg'))
        computerPaper = ImageTk.PhotoImage(Image.open('paper.jpeg'))
        playerRock = ImageTk.PhotoImage(Image.open('rock.jpeg'))
        playerPaper = ImageTk.PhotoImage(Image.open('paper.jpeg'))
        playerScissors = ImageTk.PhotoImage(Image.open('scisscors.jpeg'))
        mainRockImage = ImageTk.PhotoImage(Image.open('rock.jpeg'))
        paper_i = ImageTk.PhotoImage(Image.open('paper.jpeg'))
        scissors_i = ImageTk.PhotoImage(Image.open('scisscors.jpeg'))
        computerScissor = ImageTk.PhotoImage(Image.open('scisscors.jpeg'))

        # tk.withdraw()
        computerPicker = 0
        pl_pick = 0

        global winningGameActivate
        winningGameActivate = tk.Toplevel(self)
        winningGameActivate.geometry(self.game_size)

        computerCurrentImage = tk.Label(winningGameActivate)
        playerImageLoaded = tk.Label(winningGameActivate)
        winningGameActivate.resizable(False, False)
        score_title = tk.Label(winningGameActivate, text='Score:', font=('italic', 32))
        scoringLabel = tk.Label(winningGameActivate, text=f'{userScore} : {computerScore}', font=('italic', 24, 'bold'))
        resultingScore = tk.Label(winningGameActivate, text=' ', font=('italic', 32))
        pc_title = tk.Label(winningGameActivate, text='PC:', font=('italic', 24, 'bold'))
        pl_title = tk.Label(winningGameActivate, text=f'{string}:', font=('italic', 24, 'bold'))
        self.rock_button = tk.Button(winningGameActivate, image=mainRockImage)
        self.rock_button.image = mainRockImage
        self.paper_button = tk.Button(winningGameActivate, image=paper_i)
        self.paper_button.image = paper_i
        self.mainScissorButton = tk.Button(winningGameActivate, image=scissors_i)
        self.mainScissorButton.image = scissors_i
        back_button = tk.Button(winningGameActivate, text='Main Menu')
        playagain_button = tk.Button(winningGameActivate, text='Play again')
        self.no_button = tk.Button(winningGameActivate, text='Next')

        score_title.place(relx=0.44, rely=0.05)
        pc_title.place(relx=0.755, rely=0.21)
        scoringLabel.place(relx=0.464, rely=0.17)
        playerImageLoaded.place(relx=0.09, rely=0.3)

        resultingScore.place(relx=0.405, rely=0.65)
        computerCurrentImage.place(relx=0.65, rely=0.3)
        pl_title.place(relx=0.18, rely=0.21)

        self.no_button.place(relwidth=0.12, relheight=0.07, relx=0.82, rely=0.81)
        self.paper_button['command'] = lambda: self.callPaper()
        self.mainScissorButton['command'] = lambda: self.game_scissors()
        self.rock_button.place(relwidth=0.080, relheight=0.1, relx=0.1, rely=0.8, height=150, width=150)
        self.paper_button.place(relwidth=0.080, relheight=0.1, relx=0.300, rely=0.8, height=150, width=150)
        self.rock_button['command'] = lambda: self.callRock()

        self.mainScissorButton.place(relwidth=0.080, relheight=0.1, relx=0.500, rely=0.8, height=150, width=150)
        self.no_button['command'] = lambda: self.firstScreen()
        self.no_button.config(state="disabled")
        playagain_button['command'] = lambda: self.playAgain()
        back_button['command'] = lambda: self.gameClosing()

    def gameClosing(self):
        self.deiconify()
        winningGameActivate.destroy()

    def gameClosing2(self):

        # winningGameActivate.destroy()
        # winningGameActivate2.destroy()
        self.destroy()

    def playAgain(self):

        winningGameActivate.destroy()
        self.startingThemenu()

    def isGameRunning(self):

        self.startingThemenu()

    def firstScreen(self):
        global winningGameActivate2
        winningGameActivate2 = tk.Toplevel(self)
        winningGameActivate2.geometry(self.game_size)
        winningGameActivate2.resizable(False, False)
        asking = tk.Label(winningGameActivate2, text="Do you want to continue the game?", font=("italic 22 bold"))
        asking.pack(side=tk.TOP, pady=100)
        no = 'no'
        yes = 'yes'
        mainNoButton = tk.Button(winningGameActivate2, text=no)
        mainYesButton = tk.Button(winningGameActivate2, text=yes)
        mainYesButton.place(relwidth=0.12, relheight=0.07, relx=0.2, rely=0.81)
        mainYesButton['command'] = lambda: self.isGameRunning()
        mainNoButton.place(relwidth=0.12, relheight=0.07, relx=0.82, rely=0.81)
        mainNoButton['command'] = lambda: self.gameClosing2()
        self.gameClosing()

    def getRandomInt(self):
        return random.randint(0, 2)
    def callRock(self):

        # nonlocal pl_score, computerScoreCurrent, pl_pick, computerPicker
        global userScore  , computerScore

        pl_pick = 0
        playerImageLoaded.configure(image=playerRock)
        playerImageLoaded.image = playerRock
        computerPicker = self.getRandomInt()

        if computerPicker == self.return0():

            computerCurrentImage.configure(image=rockImage)
            computerCurrentImage.image = rockImage
            resultingScore['text'] = 'MainGame tied'

        elif computerPicker == self.return1():

            computerCurrentImage.configure(image=computerPaper)
            computerCurrentImage.image = computerPaper
            resultingScore['text'] = 'You lost!'
            # computerScoreCurrent+=1
            computerScore+=1

        else:

            computerCurrentImage.configure(image=computerScissor)
            computerCurrentImage.image = computerScissor
            resultingScore['text'] = 'You won!'
            # pl_score+=1
            userScore+=1

        scoringLabel['text'] = f'{userScore} : {computerScore}'
        self.rockConfig()
        self.paperConfig()
        self.scissorConfig()
        self.no_button.config(state="active")

    def callPaper(self):

        # nonlocal pl_score, computerScoreCurrent, pl_pick, computerPicker, rounds
        global userScore, computerScore
        pl_pick = 0
        playerImageLoaded.configure(image=playerPaper)
        playerImageLoaded.image = playerPaper
        computerPicker = self.getRandomInt()

        if computerPicker == 1:

            computerCurrentImage.configure(image=computerPaper)
            computerCurrentImage.image = computerPaper
            resultingScore['text'] = 'MainGame tied'

        elif computerPicker == 2:

            computerCurrentImage.configure(image=computerScissor)
            computerCurrentImage.image = computerScissor
            resultingScore['text'] = 'You lost!'
            # computerScoreCurrent+=1
            computerScore += 1

        else:

            computerCurrentImage.configure(image=rockImage)
            computerCurrentImage.image = rockImage
            resultingScore['text'] = 'You won!'
            # pl_score+=1
            userScore += 1

        scoringLabel['text'] = f'{userScore} : {computerScore}'
        self.rockConfig()
        self.paperConfig()
        self.scissorConfig()
        self.no_button.config(state="active")

    def scissorConfig(self):
        self.mainScissorButton.config()

    def paperConfig(self):
        self.paper_button.config()

    def rockConfig(self):
        self.rock_button.config()
    def return2(self):
        return 2
    def return1(self):
        return 1
    def return0(self):
        return 0
    def game_scissors(self):

        # nonlocal pl_score, computerScoreCurrent, pl_pick, computerPicker, rounds
        global userScore, computerScore
        pl_pick = 0
        playerImageLoaded.configure(image=playerScissors)
        playerImageLoaded.image = playerScissors
        computerPicker = self.getRandomInt()



        if computerPicker == self.return0():

            computerCurrentImage.configure(image=rockImage)
            computerCurrentImage.image = rockImage
            resultingScore['text'] = 'You lost!'
            # computerScoreCurrent+=1
            computerScore += 1

        if computerPicker == self.return2():

            computerCurrentImage.configure(image=computerScissor)
            computerCurrentImage.image = computerScissor
            resultingScore['text'] = 'MainGame tied'

        else:

            computerCurrentImage.configure(image=computerPaper)
            computerCurrentImage.image = computerPaper
            resultingScore['text'] = 'You won!'
            # pl_score+=1
            userScore+=1

        scoringLabel['text'] = f'{userScore} : {computerScore}'
        self.rockConfig()
        self.paperConfig()
        self.scissorConfig()
        self.no_button.config(state="active")

def main():
    pass

game = MainGame()
game.startMainGame()
game.mainloop()

main()