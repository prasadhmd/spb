from tkinter import *
from time import sleep
import pygame
import random
import re
import unicodedata

out = pygame.mixer.init()

class Question:
    def __init__(self, word, iidx):
        self.word = word
        self.iidx = iidx
 
    def check(self, answer, view):
        global right
        if(answer.strip().lower() == self.word):
            label = Label(view, text="Correct!", font = ("Helvetica", 25),
                          fg = "green")
            right += 1
        else:
            label = Label(view, text=self.word, font = ("Helvetica", 25),
                          fg = "red")
        label.place(x = 25, y = 275)
        b3 = Button(view, text = "Next", font = ("Helvetica", 25),
                     command = lambda *args: self.unpackView(view))
        b3.place(x = 350, y = 275)

    def play_word(self):
        pygame.mixer.music.load("2b/"+str(self.iidx)+".mp3")
        pygame.mixer.music.play(0)

    def getView(self, window):
        view = Frame(window, width=900, height=700)
        b1 = Button(view, text = "New Word", font = ("Helvetica", 25),
                     command = self.play_word)
        b1.place(x=25, y=50)
        entry = Entry(view, width=20, font = ("Helvetica", 25))
        entry.place(x = 25, y = 128)
        b2 = Button(view, text="Submit", pady=5, font=("Helvetica", 25),
                command = lambda *args: self.check(entry.get(), view))
        b2.place(x = 25, y = 200)
        
        if self.word in defn[self.iidx-1]:
            defn[self.iidx-1] = defn[self.iidx-1].replace(self.word, '****')
            
        l1 = Message(view, text = defn[self.iidx-1], width = 700,
                     font=("Helvetica", 15), fg = 'blue')
        l1.place(x = 25, y = 340)
        return view

    def unpackView(self, view):
        view.pack_forget()
        askQuestion()

def askQuestion():
    global words_sel, window, index, button, right, number_of_questions, defn
    if(index == number_of_questions):
        Label(window, text="Score: " +
              str(right) + "/" + str(number_of_questions),
              font = ("Helvetica", 25)).pack()
        return
    button.pack_forget()
    words_sel[index].getView(window).pack()
    index += 1

def strip_accents(text):
    return ''.join(char for char in
                   unicodedata.normalize('NFKD', text)
                   if unicodedata.category(char) != 'Mn')

wordset = '2b'

index = 0
right = 0
number_of_questions = 10
window = Tk()
window.title("Spelling Bee Practice")
window.geometry("900x700")

wdefs = open("2b_def.txt", "r").readlines()
defn = []
pattern = re.compile('sx\|?.*')
#pattern = re.compile('.\|.*')

for w in wdefs:
    if w.replace('\n','').isnumeric():
        l = int(w.replace('\n',''))
        defn.append('')
    else:
        w = w.strip()
        if 'a_link|' in w:
          w = w.replace('a_link|', '')
        if 'd_link|' in w:
          w = w.replace('d_link|', '')
        if '{bc}' in w:
          w = w.replace('{bc}','')
        if '{' in w:
          w = w.replace('{', '')
        if '}' in w:
          w = w.replace('}', '')
        w = pattern.sub('', w)
        w = strip_accents(w)
        defn[l-1] = defn[l-1] + w.lower() + '.\n'

#words = open("3b.txt", "r").readlines()
words = open("2b.txt", "r").readlines()
idx = range(1, len(words))
words_idx = list(zip(idx, words))
random.shuffle(words_idx)
words = [item[1] for item in words_idx]
idx = [item[0] for item in words_idx]
words_sel = []
for i in range(number_of_questions):
    w = words[i].strip().lower()
    words_sel.append(Question(w, idx[i]))
button = Button(window, text="Start", font=("Helvetica", 25), fg = 'blue',
                command=askQuestion)
button.pack()
window.mainloop()
