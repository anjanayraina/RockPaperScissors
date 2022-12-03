from tkinter import *
from PIL import Image, ImageTk
import random

userscore = 0
pcscore = 0


### Functions of the game
def enter(event):
    rock.config(bg='black', fg='white')


def enter1(event):
    paper.config(bg='black', fg='white')


def enter2(event):
    scissor.config(bg='black', fg='white')


def leave(event):
    rock.config(bg='white', fg='black')


def leave1(event):
    paper.config(bg='white', fg='black')


def leave2(event):
    scissor.config(bg='white', fg='black')


def entergame():
    maingame()

def choicemaker(user , pc):
    if user == 'Rock' and pc == 'Paper':
        return 1
    elif user == 'Rock' and pc == 'Scissor':
        return 2

    elif user == 'Paper' and pc == 'Scissor':
        return 3

    elif user == 'Paper' and pc == 'Rock':
        return 4

    elif user == 'Scissor' and pc == 'Rock':
        return 5
    elif user == 'Scissor' and pc == 'Paper':
        return 6

    elif user == pc:
        return -1

def initilizestate():
    root.geometry('650x450')
    userName.destroy()
    frame1.destroy()
    inputtedName.destroy()
    mainFrame.destroy()
def creategame():
    L2 = Label(text=f"{userNameInp.get()} Score: {userscore}", bg='#4834DF', fg='#ffffff', borderwidth=5, relief=RAISED,
               font='Rockwell 13 bold', padx=4, pady=2)
    L2.grid(row=5, column=0, pady=15)
    L3 = Label(text=f"PC Score: {pcscore}", bg='#4834DF', fg='white', borderwidth=5, relief=RAISED,
               font='Rockwell 13 bold', padx=4, pady=2)
    L3.grid(row=6, column=0, pady=15)
def getRandomInt():
    return random.randint(0,2)
def getRandomchoice():
    l1 = ['Rock', 'Paper', 'Scissor']
    return l1[getRandomInt()]


def playGame(val , pc_opt):
    global userscore
    global pcscore
    global label1

    if choicemaker(val, pc_opt) == 1:  # val means what user chose and pc_opt means what pc chose or opted
        label1 = Label(text='PC Won', font='lucida 15 bold', bg='black', fg='gold')
        label1.grid(row=6, column=1, pady=15)
        pcscore += 1

    elif choicemaker(val, pc_opt) == 2:
        label1 = Label(text=f'{userNameInp.get()} Won', font='lucida 15 bold', bg='black', fg='gold')
        label1.grid(row=6, column=1, pady=15)
        userscore += 1

    elif choicemaker(val, pc_opt) == 3:
        label1 = Label(text='PC Won', font='lucida 15 bold', bg='black', fg='gold')
        label1.grid(row=6, column=1, pady=15)
        pcscore += 1

    elif choicemaker(val, pc_opt) == 4:
        label1 = Label(text=f'{userNameInp.get()} Won', font='lucida 15 bold', bg='black', fg='gold')
        label1.grid(row=6, column=1, pady=15)
        userscore += 1

    elif choicemaker(val, pc_opt) == 5:
        label1 = Label(text='PC Won', font='lucida 15 bold', bg='black', fg='gold')
        label1.grid(row=6, column=1, pady=15)
        pcscore += 1

    elif choicemaker(val, pc_opt) == 6:
        label1 = Label(text=f'{userNameInp.get()} Won', font='lucida 15 bold', bg='black', fg='gold')
        label1.grid(row=6, column=1, pady=15)
        userscore += 1

    elif choicemaker(val, pc_opt) == -1:
        label1 = Label(text=f"It's A Tie", font='lucida 15 bold', bg='black', fg='gold')
        label1.grid(row=6, column=1, pady=15)


# Maingame Function will bring a new window of GUI and will provide a platform to play RPS:
def maingame():
    global frame1
    global userscore, pcscore
    global userNameInp
    global rock, paper, scissor
    initilizestate()

    # score:
    creategame()
    # Click Function Main Logic:
    def click(event):
        global userscore, pcscore  # These variable will get or count the scores of user and pc
        global label1  # We are using label1 Label
        global pcchose  # we are using old pcchose label
        label1.grid_forget()  # We are forgetting or removing old label so that new text can come properly
        pcchose.destroy()  # We are deleting or removing old one so that new can come properly

        val = event.widget.cget('text')  # This command will take the text of button

        # PC Logic (Pc will choose something randomly)


        pc_opt = getRandomchoice() # PC Option

        # PC OPT (what PC opted will be shown as a label by this command):
        pcchose = Label(text=f'PC Chose : {pc_opt}', font='lucida 15 bold', bg='black', fg='red')
        pcchose.grid(row=5, column=1, pady=15)

        # Actual Game Logic
        playGame(val , pc_opt)
        maingame()

    # (Layout of RPS Game)

    head = Label(text='Rock Paper Scissor Game', font='arial 45 bold', bg='gold', fg='white')
    head.grid(columnspan=2, row=0, ipadx=70, padx=33, pady=10)
    playerone = Label(text=f'Player 1 : {userNameInp.get()}', font='lucida 16')
    playerone.grid(row=1, column=0)
    playertwo = Label(text=f'Player 2 : Computer', font='lucida 16')
    playertwo.grid(row=1, column=1)

    # Player 1 Buttons

    def player1Buttons():
        global frame1
        rock = Button(text='Rock', font='comicsansms 14 bold', height=1, width=7 )
        rock.grid(row=2, column=0, pady=15)
        rock.bind('<Enter>', enter)
        rock.bind('<Leave>', leave)
        rock.bind('<Button-1>', click)
        paper = Button(text='Paper', font='comicsansms 14 bold', height=1, width=7)
        paper.grid(row=3, column=0)
        paper.bind('<Enter>', enter1)
        paper.bind('<Leave>', leave1)
        paper.bind('<Button-1>', click)
        scissor = Button(text='Scissor', font='comicsansms 14 bold', height=1, width=7)
        scissor.grid(row=4, column=0, pady=15)
        scissor.bind('<Enter>', enter2)
        scissor.bind('<Leave>', leave2)
        scissor.bind('<Button-1>', click)

    player1Buttons()


    # Player 2:Computer Buttons
    def computerButtons():
        rock1 = Button(text='Rock', font='comicsansms 14 bold', height=1, width=7)
        rock1.grid(row=2, column=1, pady=15)
        paper1 = Button(text='Paper', font='comicsansms 14 bold', height=1, width=7)
        paper1.grid(row=3, column=1)
        scissor1 = Button(text='Scissor', font='comicsansms 14 bold', height=1, width=7)
        scissor1.grid(row=4, column=1, pady=15)
    computerButtons()



    # Keep Playing Button
    def keepPlayingButton():
        btnclose = Button(text='Keep Playing', bg='green', font='arial 10 bold')
        btnclose.place(x=350, y=350)
    keepPlayingButton()

    # Close Button
    def closeButton():
        btnclose = Button(text='Stop Playing', command=root.destroy, bg='green', font='arial 10 bold')
        btnclose.place(x=500, y=350)
    closeButton()

    # def menu_start(self):
    #
    #     global pl_image, pl_paper, pl_pick, pl_rock, pl_scissors, pl_paper, pc_rock, pc_pick, pc_scissors, pc_score, pc_paper, pc_image, result_label, score_label
    #     pl_score = 0
    #     pc_score = 0
    #     pc_rock = ImageTk.PhotoImage(Image.open(path1))
    #     pc_paper = ImageTk.PhotoImage(Image.open(path2))
    #     pc_scissors = ImageTk.PhotoImage(Image.open(path3))
    #     pl_rock = ImageTk.PhotoImage(Image.open(path1))
    #     pl_paper = ImageTk.PhotoImage(Image.open(path2))
    #     pl_scissors = ImageTk.PhotoImage(Image.open(path3))
    #     rock_i = ImageTk.PhotoImage(Image.open(path1))
    #     paper_i = ImageTk.PhotoImage(Image.open(path2))
    #     scissors_i = ImageTk.PhotoImage(Image.open(path3))
    #     # tk.withdraw()
    #     pc_pick = 0
    #     pl_pick = 0
    #
    #     global game_win
    #     game_win = root.Toplevel(self)
    #     game_win.geometry(self.game_size)
    #     game_win.resizable(False, False)
    #     score_title = tk.Label(game_win, text='Score:', font=('Tahoma', 32))
    #     score_label = tk.Label(game_win, text=f'{pl_score} : {pc_score}', font=('Tahoma', 24, 'bold'))
    #     result_label = tk.Label(game_win, text=' ', font=('Tahoma', 32))
    #     pc_image = tk.Label(game_win)
    #     pl_image = tk.Label(game_win)
    #     pc_title = tk.Label(game_win, text='PC:', font=('Tahoma', 24, 'bold'))
    #     pl_title = tk.Label(game_win, text=f'{string}:', font=('Tahoma', 24, 'bold'))
    #     self.rock_button = tk.Button(game_win, image=rock_i)
    #     self.rock_button.image = rock_i
    #     self.paper_button = tk.Button(game_win, image=paper_i)
    #     self.paper_button.image = paper_i
    #     self.scissors_button = tk.Button(game_win, image=scissors_i)
    #     self.scissors_button.image = scissors_i
    #     back_button = tk.Button(game_win, text='Menu')
    #     playagain_button = tk.Button(game_win, text='Play again')
    #     self.no_button = tk.Button(game_win, text='NEXT')
    #
    #     score_title.place(relx=0.44, rely=0.05)
    #     score_label.place(relx=0.464, rely=0.17)
    #     result_label.place(relx=0.405, rely=0.65)
    #     pc_image.place(relx=0.65, rely=0.3)
    #     pl_image.place(relx=0.09, rely=0.3)
    #     pc_title.place(relx=0.755, rely=0.21)
    #     pl_title.place(relx=0.18, rely=0.21)
    #     self.rock_button.place(relwidth=0.080, relheight=0.1, relx=0.1, rely=0.8, height=150, width=150)
    #     self.paper_button.place(relwidth=0.080, relheight=0.1, relx=0.300, rely=0.8, height=150, width=150)
    #     self.scissors_button.place(relwidth=0.080, relheight=0.1, relx=0.500, rely=0.8, height=150, width=150)
    #     self.no_button.place(relwidth=0.12, relheight=0.07, relx=0.82, rely=0.81)
    #     self.rock_button['command'] = lambda: self.game_rock()
    #     self.paper_button['command'] = lambda: self.game_paper()
    #     self.scissors_button['command'] = lambda: self.game_scissors()
    #     self.no_button['command'] = lambda: self.askuser()
    #     self.no_button.config(state="disabled")
    #     playagain_button['command'] = lambda: self.play_again()
    #     back_button['command'] = lambda: self.close_game()


''' GUI Program Starting '''

# if __name__=='__main__':
root = Tk()
root.title('Rock Paper Scissor')
# root.wm_iconbitmap("game.ico")
# Geometry or dimensions of game window
root.geometry('1000x450')
root.maxsize(1000, 450)
root.minsize(1000, 450)

# Defining some widgets to use them in diff functions
rock = Button()
paper = Button()
scissor = Button()

# Defining Label to use it later in the program
label1 = Label()  # This Label will show the who won pc or user
pcchose = Label()  # This Label will show what pc opted or chose

# Frame for first window of game

def enteringframe():
    pass
def newEnterGame(e):
    maingame()

frame1 = Frame(root)

mainFrameImage = Image.open('main.webp')
mainFrameImage = mainFrameImage.resize((900, 400))
picture = ImageTk.PhotoImage(mainFrameImage)
mainLabel = Label(frame1, image=picture)
mainLabel.pack()
frame1.pack()
rockImage = Image.open('rockImage.png')


# Create some widgets and placed them above the image that's why used place geometry method
userName = Label(root, text='What do you want to be called in this game', font='arial 15 bold')
userName.place(x=300, y=20)
userNameInp = StringVar()  # This variable will store the userName of user
inputtedName = Entry(root, textvar=userNameInp, font='arial 10')
inputtedName.bind('<Return>',
             entergame)  # We binded Return event with inputtedName entry widget i.e. if enter key is pressed then entergame function will be called
inputtedName.place(x=435, y=60)

mainFrame = Button(root, text="Let's Play", font='lucida 10 bold', bg='black', fg='white', command=maingame)
mainFrame.place(x=475, y=88)
root.bind('<Return>', newEnterGame)
root.mainloop()