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
        self.title('Rock, Paper, Scissors')
        self.resizable(False, False)

    def started(self):
        global entry
        global string

        name = tk.Label(self, text="Please tell me your name :", font=("Courier 22 bold"))

        name.pack(side=tk.TOP, pady=100)
        new_game = tk.Button(self, text='Start Game')

        new_game.place(relheight=0.1, relwidth=0.2, rely=0.7, relx=0.4)
        new_game['command'] = lambda: self.menu_start()

        entry = tk.Entry(self, width=60)
        entry.focus_set()
        entry.pack(side=TOP)

    def menu_start(self):
        string = entry.get()
        global pl_image, pl_paper, pl_pick, pl_rock, pl_scissors, pl_paper, pc_rock, pc_pick, pc_scissors, pc_score, pc_paper, pc_image, result_label, score_label
        global userScore , pcScore
        pl_score = 0
        pc_score = 0
        pc_rock = ImageTk.PhotoImage(Image.open('rock.jpeg'))
        pc_paper = ImageTk.PhotoImage(Image.open('paper.jpeg'))
        pc_scissors = ImageTk.PhotoImage(Image.open('scisscors.jpeg'))
        pl_rock = ImageTk.PhotoImage(Image.open('rock.jpeg'))
        pl_paper = ImageTk.PhotoImage(Image.open('paper.jpeg'))
        pl_scissors = ImageTk.PhotoImage(Image.open('scisscors.jpeg'))
        rock_i = ImageTk.PhotoImage(Image.open('rock.jpeg'))
        paper_i = ImageTk.PhotoImage(Image.open('paper.jpeg'))
        scissors_i = ImageTk.PhotoImage(Image.open('scisscors.jpeg'))
        # tk.withdraw()
        pc_pick = 0
        pl_pick = 0

        global game_win
        game_win = tk.Toplevel(self)
        game_win.geometry(self.game_size)
        game_win.resizable(False, False)
        score_title = tk.Label(game_win, text='Score:', font=('Tahoma', 32))
        score_label = tk.Label(game_win, text=f'{userScore} : {computerScore}', font=('Tahoma', 24, 'bold'))
        result_label = tk.Label(game_win, text=' ', font=('Tahoma', 32))
        pc_image = tk.Label(game_win)
        pl_image = tk.Label(game_win)
        pc_title = tk.Label(game_win, text='PC:', font=('Tahoma', 24, 'bold'))
        pl_title = tk.Label(game_win, text=f'{string}:', font=('Tahoma', 24, 'bold'))
        self.rock_button = tk.Button(game_win, image=rock_i)
        self.rock_button.image = rock_i
        self.paper_button = tk.Button(game_win, image=paper_i)
        self.paper_button.image = paper_i
        self.scissors_button = tk.Button(game_win, image=scissors_i)
        self.scissors_button.image = scissors_i
        back_button = tk.Button(game_win, text='Menu')
        playagain_button = tk.Button(game_win, text='Play again')
        self.no_button = tk.Button(game_win, text='NEXT')

        score_title.place(relx=0.44, rely=0.05)
        score_label.place(relx=0.464, rely=0.17)
        result_label.place(relx=0.405, rely=0.65)
        pc_image.place(relx=0.65, rely=0.3)
        pl_image.place(relx=0.09, rely=0.3)
        pc_title.place(relx=0.755, rely=0.21)
        pl_title.place(relx=0.18, rely=0.21)
        self.rock_button.place(relwidth=0.080, relheight=0.1, relx=0.1, rely=0.8, height=150, width=150)
        self.paper_button.place(relwidth=0.080, relheight=0.1, relx=0.300, rely=0.8, height=150, width=150)
        self.scissors_button.place(relwidth=0.080, relheight=0.1, relx=0.500, rely=0.8, height=150, width=150)
        self.no_button.place(relwidth=0.12, relheight=0.07, relx=0.82, rely=0.81)
        self.rock_button['command'] = lambda: self.game_rock()
        self.paper_button['command'] = lambda: self.game_paper()
        self.scissors_button['command'] = lambda: self.game_scissors()
        self.no_button['command'] = lambda: self.askuser()
        self.no_button.config(state="disabled")
        playagain_button['command'] = lambda: self.play_again()
        back_button['command'] = lambda: self.close_game()

    def close_game(self):
        self.deiconify()
        game_win.destroy()

    def close_game2(self):

        # game_win.destroy()
        # game_win2.destroy()
        self.destroy()

    def play_again(self):

        game_win.destroy()
        self.menu_start()

    def active_game(self):

        self.menu_start()

    def askuser(self):
        global game_win2
        game_win2 = tk.Toplevel(self)
        game_win2.geometry(self.game_size)
        game_win2.resizable(False, False)
        asking = tk.Label(game_win2, text="Do you want to continue the game?", font=("Courier 22 bold"))
        asking.pack(side=tk.TOP, pady=100)
        no_button2 = tk.Button(game_win2, text='NO')
        yes_button = tk.Button(game_win2, text='YES')
        yes_button.place(relwidth=0.12, relheight=0.07, relx=0.2, rely=0.81)
        yes_button['command'] = lambda: self.active_game()
        no_button2.place(relwidth=0.12, relheight=0.07, relx=0.82, rely=0.81)
        no_button2['command'] = lambda: self.close_game2()
        self.close_game()

    def getRandomInt(self):
        return random.randint(0, 2)
    def game_rock(self):

        # nonlocal pl_score, pc_score, pl_pick, pc_pick
        global userScore  , computerScore

        pl_pick = 0
        pl_image.configure(image=pl_rock)
        pl_image.image = pl_rock
        pc_pick = self.getRandomInt()

        if pc_pick == 0:

            pc_image.configure(image=pc_rock)
            pc_image.image = pc_rock
            result_label['text'] = 'MainGame tied'

        elif pc_pick == 1:

            pc_image.configure(image=pc_paper)
            pc_image.image = pc_paper
            result_label['text'] = 'You lost!'
            # pc_score+=1
            computerScore+=1

        else:

            pc_image.configure(image=pc_scissors)
            pc_image.image = pc_scissors
            result_label['text'] = 'You won!'
            # pl_score+=1
            userScore+=1

        score_label['text'] = f'{userScore} : {computerScore}'
        self.rock_button.config(state="disabled")
        self.paper_button.config(state="disabled")
        self.scissors_button.config(state="disabled")
        self.no_button.config(state="active")

    def game_paper(self):

        # nonlocal pl_score, pc_score, pl_pick, pc_pick, rounds
        global userScore, computerScore
        pl_pick = 0
        pl_image.configure(image=pl_paper)
        pl_image.image = pl_paper
        pc_pick = random.randint(0, 2)

        if pc_pick == 1:

            pc_image.configure(image=pc_paper)
            pc_image.image = pc_paper
            result_label['text'] = 'MainGame tied'

        elif pc_pick == 2:

            pc_image.configure(image=pc_scissors)
            pc_image.image = pc_scissors
            result_label['text'] = 'You lost!'
            # pc_score+=1
            computerScore += 1

        else:

            pc_image.configure(image=pc_rock)
            pc_image.image = pc_rock
            result_label['text'] = 'You won!'
            # pl_score+=1
            userScore += 1

        score_label['text'] = f'{userScore} : {computerScore}'
        # self.rock_button.config(state="disabled")
        # self.paper_button.config(state="disabled")
        # self.scissors_button.config(state="disabled")
        self.no_button.config(state="active")

    def game_scissors(self):

        # nonlocal pl_score, pc_score, pl_pick, pc_pick, rounds
        global userScore, computerScore
        pl_pick = 0
        pl_image.configure(image=pl_scissors)
        pl_image.image = pl_scissors
        pc_pick = random.randint(0, 2)

        if pc_pick == 2:

            pc_image.configure(image=pc_scissors)
            pc_image.image = pc_scissors
            result_label['text'] = 'MainGame tied'

        elif pc_pick == 0:

            pc_image.configure(image=pc_rock)
            pc_image.image = pc_rock
            result_label['text'] = 'You lost!'
            # pc_score+=1
            computerScore += 1

        else:

            pc_image.configure(image=pc_paper)
            pc_image.image = pc_paper
            result_label['text'] = 'You won!'
            # pl_score+=1
            userScore+=1

        score_label['text'] = f'{userScore} : {computerScore}'
        self.rock_button.config(state="disabled")
        self.paper_button.config(state="disabled")
        self.scissors_button.config(state="disabled")
        self.no_button.config(state="active")


def main():
    game = MainGame()
    game.started()
    game.mainloop()


if __name__ == "__main__":
    main()