import random
from tkinter import *

def next_turn(row, column):
    global player

    # Check if the button is empty and no winner yet
    if buttons[row][column]['text'] == "" and check_winner() is False:
        buttons[row][column]['text'] = player

        # Check for winner or tie after the move
        result = check_winner()
        
        if result is False:
            # Switch player
            player = players[1] if player == players[0] else players[0]
            label.config(text=(player + " turn"))

        elif result is True:
            label.config(text=(player + " wins"))
            if player == players[0]:
                x_wins[0] += 1
            else:
                o_wins[0] += 1
            update_scoreboard()
            # Disable all buttons so no more moves can be made
            disable_buttons()
            window.after(2000, new_game)

        elif result == "Tie":
            label.config(text=("Tie!"))
            disable_buttons()
            window.after(2000, new_game)


def check_winner():
    # Check rows
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            highlight_win(buttons[row][0], buttons[row][1], buttons[row][2])
            return True

    # Check columns
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            highlight_win(buttons[0][column], buttons[1][column], buttons[2][column])
            return True

    # Check diagonals
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        highlight_win(buttons[0][0], buttons[1][1], buttons[2][2])
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        highlight_win(buttons[0][2], buttons[1][1], buttons[2][0])
        return True

    # Check for Tie
    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="red")
        return "Tie"

    else:
        return False


def highlight_win(btn1, btn2, btn3):
    btn1.config(bg="green")
    btn2.config(bg="green")
    btn3.config(bg="green")


def empty_spaces():
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] == "":
                return True
    return False


def disable_buttons():
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(state=DISABLED)


def new_game():
    global player
    player = random.choice(players)
    label.config(text=player + " turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", state=NORMAL, bg="SystemButtonFace")


def update_scoreboard():
    score_label.config(text=f"X Wins: {x_wins[0]}   O Wins: {o_wins[0]}")


# --- Main Setup ---
window = Tk()
window.title('Tic-Tac-Toe')
window.resizable(False, False)  # Prevent resizing

players = ["x", "o"]
player = random.choice(players)

x_wins = [0]
o_wins = [0]

buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

label = Label(text=player + " turn", font=('consolas', 40))
label.pack(side="top")

score_label = Label(text="X Wins: 0   O Wins: 0", font=('consolas', 20))
score_label.pack(side="top")

restart_button = Button(text="Restart", bg="lightblue", bd=3, relief=RAISED, font=('consolas', 15), command=new_game)
restart_button.pack(side="top", pady=10)

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('consolas', 40), width=5, height=2,
                                      command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

window.mainloop()