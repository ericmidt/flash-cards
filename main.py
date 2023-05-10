from tkinter import *
from tkinter import messagebox
import pandas
import random

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#b1ddc6"
YELLOW = "#f7f5dd"
FONT_NAME = "Ariel"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# Tries to read words_to_learn.csv
try:
    words_df = pandas.read_csv("words_to_learn.csv")
# If there's no words_to_learn csv file, it creates one. If it's empty, it loads from french_words.csv
except (FileNotFoundError, pandas.errors.EmptyDataError):
    words_df = pandas.read_csv("data/french_words.csv")

words_dict = words_df.to_dict(orient="records")
random_word = {}


# ---------------------------- REMOVE WORD ------------------------------- #
def remove_word():
    global random_word
    try:
        words_dict.remove(random_word)
        words_to_learn_df = pandas.DataFrame(words_dict)
        words_to_learn_df.to_csv("words_to_learn.csv", index=False)
    except IndexError:
        messagebox.showinfo(title="Error", message="You have ran out of words.")
    new_card()


# ---------------------------- SHOW ANSWER ------------------------------- #
def show_answer(chosen_word):
    canvas.itemconfig(card, image=card_back)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=chosen_word['English'], fill="white")


# ---------------------------- LOAD NEW CARD ---------------------------- #
def new_card():
    global words_dict
    global timer
    global random_word
    try:
        window.after_cancel(timer)
    except ValueError:
        pass
    random_word = random.choice(words_dict)
    canvas.itemconfig(card, image=card_front)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word, text=random_word['French'], fill="black")
    timer = window.after(3000, show_answer, random_word)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=GREEN)

# Loads images
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")

# Creates background and card_front image
canvas = Canvas(width=800, height=526, bg=GREEN, highlightthickness=0)
card = canvas.create_image(0, 0, image=card_front, anchor='nw')
canvas.grid(row=0, column=0, columnspan=2)
language = canvas.create_text(400, 150, text="", font=(FONT_NAME, 40, "italic"))
word = canvas.create_text(400, 263, text="", font=(FONT_NAME, 60, "bold"))

# Creates buttons
right_button = Button(image=right_image, highlightthickness=0, command=remove_word)
right_button.grid(row=1, column=0)
wrong_button = Button(image=wrong_image, highlightthickness=0, command=new_card)
wrong_button.grid(row=1, column=1)

# Load new card info
new_card()

window.mainloop()
