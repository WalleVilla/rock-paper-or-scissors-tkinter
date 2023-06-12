from tkinter import *
from tkinter import messagebox, ttk
import random

#list for the images references
user_images = []
pc_images = []



def moves_selected(event):
    user_move = moves_combo.get()

    #User image
    user_canvas = Canvas(width=120, height=120)
    user_img = PhotoImage(file=f"./images/{user_move}_user.png")
    
    if user_move == "rock":
        user_img = user_img.subsample(5, 5)
    else:
        user_img = user_img.subsample(2, 2)
        
    user_canvas.create_image(60, 60, image=user_img)
    user_canvas.grid(column=0, row=4)
    user_images.append(user_img) 
    
def play():
    user_move = moves_combo.get()
    moves = ["rock", "paper", "scissors"]
    
    if user_move != "Moves":
        pc_move = random.choice(moves)
        
        #Pc image
        pc_canvas = Canvas(width=120, height=120)
        pc_img = PhotoImage(file=f"./images/{pc_move}_pc.png")
    
        if pc_move == "rock":
            pc_img = pc_img.subsample(5, 5)
        else:
            pc_img = pc_img.subsample(2, 2)
            
        pc_canvas.create_image(60, 60, image=pc_img)
        pc_canvas.grid(column=2, row=4)
        pc_images.append(pc_img) 
        
        winner(user_move, pc_move)
    
    #message error if the user didn´t choose    
    else:
        messagebox.showerror(
            title="Error",
            message="You didn't choose a valid move"
        )

def winner(user_move, pc_move):
    if user_move == "rock" and pc_move == "scissors":
        winner_lb.config(text="You win!", fg="green")
    elif user_move == "paper" and pc_move == "rock":
        winner_lb.config(text="You win!", fg="green")
    elif user_move == "scissors" and pc_move == "paper":
        winner_lb.config(text="You win!", fg="green")
    elif user_move == pc_move:
        winner_lb.config(text="Tie!", fg="black")
    else:
        winner_lb.config(text="PC wins!", fg="red")


# ------------------------------------ UI ------------------------------------ #
window = Tk()
window.title("Rock paper or scissors game")
window.config(padx=50, pady=50)

title_lb = Label(text="Rock paper or scissors game", font=("Arial", 18))
title_lb.grid(column=1, row=0, pady=(0, 20))

logo_canvas = Canvas(width=120, height=120)
logo_img = PhotoImage(file="./images/logo.png")
logo_img = logo_img.subsample(5, 5)
logo_canvas.create_image(60, 60, image=logo_img)
logo_canvas.grid(column=1, row=1)

choose_lb = Label(text="Choose your move", font=("Arial", 16))
choose_lb.grid(column=1, row=2, pady=50)

moves_combo = ttk.Combobox(
    window, values=["rock", "paper", "scissors"],
    state="readonly", font=("Arial", 10),
    width=10)
moves_combo.set("Moves")
moves_combo.bind("<<ComboboxSelected>>", moves_selected)
moves_combo.grid(column=0, row=3)

pc_lb = Label(text="PC choice", font=("Arial", 10))
pc_lb.grid(column=2, row=3)


play_btn = Button(text="Play", font=("Arial", 12), command=play ,width=10)
play_btn.grid(column=1, row=5)

winner_lb = Label(font=("Arial", 10))
winner_lb.grid(column=1, row=6, pady=20)

window.mainloop()