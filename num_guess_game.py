# numer guessing game

import tkinter as tk
import random
from tkinter import messagebox

# Global variables
num_to_guess = 0
max_num = 100
attempts = 0


def start_game(level):
    global num_to_guess, max_num, attempts
    attempts = 0

    if level == "1":
        max_num = 20
    elif level == "2":
        max_num = 100
    elif level == "3":
        max_num = 200
    else:
        max_num = 100

    num_to_guess = random.randint(1, max_num)
    feedback_label.config(text=f"Guess a number between 1 and {max_num}")
    guess_entry.delete(0, tk.END)


def check_guess():
    global attempts
    try:
        guess = int(guess_entry.get())
        attempts += 1
        if guess < num_to_guess:
            feedback_label.config(text="Too low! Try again.")
        elif guess > num_to_guess:
            feedback_label.config(text="Too high! Try again.")
        else:
            messagebox.showinfo(
                "🎉 Correct!", f"You guessed it in {attempts} attempts!")
            feedback_label.config(text="Start a new game to play again.")
            guess_entry.delete(0, tk.END)
    except ValueError:
        feedback_label.config(text="Please enter a valid number.")


# GUI setup
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x300")

tk.Label(root, text="🎮 Welcome to the Number Guessing Game",
         font=("Arial", 14)).pack(pady=10)

tk.Label(root, text="Choose Difficulty:").pack()
button_frame = tk.Frame(root)
button_frame.pack()

tk.Button(button_frame, text="Easy", command=lambda: start_game(
    "1")).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Medium", command=lambda: start_game(
    "2")).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Hard", command=lambda: start_game(
    "3")).grid(row=0, column=2, padx=5)

tk.Label(root, text="Enter your guess:").pack(pady=10)
guess_entry = tk.Entry(root)
guess_entry.pack()

tk.Button(root, text="Submit", command=check_guess).pack(pady=5)

feedback_label = tk.Label(root, text="", font=("Arial", 11))
feedback_label.pack(pady=10)

# IMPORTANT: Start the GUI loop
root.mainloop()
