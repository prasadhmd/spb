from tkinter import *
import pygame
import random

pygame.mixer.init()
def play_word():
    i = idx[j]
    pygame.mixer.music.load("audio/"+str(i)+".mp3")
    pygame.mixer.music.play(0)
    
def evaluate():
    my_word = entry.get()
    if my_word.strip().lower() == words[j].strip().lower():
        label = Label(win, text = "Correct!", font = ("Helvetica", 32))
    else:
        label = Label(win, text = words[j], font = ("Helvetica", 32))
    label.place(x=25, y = 275)

    
words = open("audio/3b.txt", "r").readlines()
idx = range(1, len(words))
words_idx = list(zip(idx, words))
random.shuffle(words_idx)
words = [item[1] for item in words_idx]
idx = [item[0] for item in words_idx]

win = Tk()
win.title("Spelling Bee Practice")
win.geometry("450x350")

j = 0
play_button = Button(win, text = "New Word", font = ("Helvetica", 32),
                     command = play_word)
play_button.place(x=25, y=50)

entry = Entry(width=20, font = ("Helvetica", 32))
entry.place(x=25, y=125)

submit = Button(win, text="Submit", pady=5, font=("Helvetica", 32),
                command = evaluate)
submit.place(x=25, y = 200)

win.mainloop()
