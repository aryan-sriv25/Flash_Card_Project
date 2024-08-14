from tkinter import *
import pandas  #as to read from the csv file
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {} #since current_card was in next_card() so to tap in it in flip_card() we have to declare it as empty dictionary
to_learn = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")

except FileNotFoundError:
    orignal_data = pandas.read_csv("data/french_words.csv")
    to_learn = orignal_data.to_dict(orient="records")

else:
    to_learn = data.to_dict(orient="records") #to convert the dictionary to list of dictionaries.
def next_card():
    global current_card #now we can access the dict. and modify it in french or english as needed
    global flip_timer
    window.after_cancel(flip_timer) #this will invalidate the flip_timer until you wait on a word for 3 secs.
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black") #displays all the french words after clicking one of those buttons.
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)  # this func. is used to flip the cards using flip_card() after 3 sec.

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white") #it makes the text "English" white filled.
    canvas.itemconfig(card_word, text=current_card["English"], fill="white") #it makes the text on card_back_img white filled.
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False) #this index argument will stop adding those indexes.

    next_card()

window = Tk()
window.title("Flashyyy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card) #this func. is used to flip the cards using flip_card() after 3 sec.

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")#the images are in different folder hence name of the folder is must
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0) #here we will change the bg color of card_front_img and also remove the borders
canvas.grid(row=0, column=0,columnspan=2) #here we make the columnspan as 2 so to make the buttons and the card_front.img even

cross_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_img, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_img = PhotoImage(file="images/right.png")
known_button = Button(image=check_img, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()






window.mainloop()