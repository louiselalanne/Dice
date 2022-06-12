#OS APPLICATION
from tkinter import *
from PIL import ImageTk, Image
import random

root = Tk()
root.title("Jogo de Dados")
root.geometry("500x400")
root.configure(background="tan1")
img = ImageTk.PhotoImage(Image.open("dice.png"))
player1 = Label(root, text="Player 1", bg="bisque", fg="saddle brown")
player2 = Label(root, text="Player 2", bg="bisque", fg="saddle brown")
scoreP1 = Label(root, bg="bisque", fg="saddle brown")
scoreP2 = Label(root, bg="bisque", fg="saddle brown")
Random_label = Label(root, text="Num Sorteado: ",bg="bisque", fg="saddle brown")


player1.place(relx = 0.1, rely = 0.3, anchor=CENTER)
player2.place(relx = 0.9, rely = 0.3, anchor=CENTER)
scoreP1.place(relx=0.1, rely=0.4, anchor=CENTER)
scoreP2.place(relx=0.9, rely=0.4, anchor=CENTER)
Random_label.place(relx =0.5, rely=0.5, anchor=CENTER)

p1score = 0
def jogadap1():
    global p1score
    num_ale = random.randint(1,6)
    Random_label["text"] = "Resultado do Player 1: " + str(num_ale)
    p1score = p1score + num_ale
    scoreP1["text"]=str(p1score)

p1_btn = Button(root, image=img, command=jogadap1)
p1_btn.place(relx=0.1, rely=0.7, anchor=CENTER)

p2score = 0
def jogadap2():
    global p2score
    num = random.randint(1,6)
    Random_label["text"] = "Resultado do Player 2: " + str(num)
    p2score = p2score + num
    scoreP2["text"]=str(p2score)

p2_btn = Button(root, image=img, command=jogadap2)
p2_btn.place(relx=0.9, rely=0.7, anchor=CENTER)

root.mainloop()