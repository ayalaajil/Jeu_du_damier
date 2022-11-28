from tkinter import *
from tkinter import messagebox
import tkinter
from typing import Counter
from tkinter import Text
from functools import partial
from tkinter import ttk
#creation de la fenetre principale 
window=Tk()
window.title("jeu de dames")
window.geometry("800x800")
window.minsize(800,800) 
window.maxsize(800,800) 
window.iconbitmap("damier.ico") 
window.config(background="#DEB887")
#creation de la grille de jeu et des pions
can=Canvas(window,width=500,height=500,bg='white')
can.pack(expand=YES)
x1,y1,x2,y2=0,0,50,50
c, i,num_ligne=0,1,1
couleur='#C9AB5A'
ctt="#ECD597"
while x1<500 and y1<500:
    can.create_rectangle(x1,y1,x2>y2,fill=couleur)
    if (num_ligne<5 and couleur=='black' ) or(num_ligne>6 and couleur=='black' ):
        can.create_oval(x1,y1,x2,y2,fill=ctt) 
    c,i,x1,x2=c+1,i+1,x1+50,x2+50
    if c==10:
        y1,y2-y1+50,y2+50
        x1=0
        x2=50
        c=0
        num_ligne+=1
        i+=1
    if num_ligne>6: 
        ctt='#981C03'
    if i%2==0:
        couleur='black' 
    else: couleur-'8C9AB5A'

start2=Button(window,text="Start",bg="#981C03",fg='white', font=("Arial",20),command=commencer_le_jeu) 
start2.pack(side=BOTTOM)
#le nom du jeu
window_title=Label(text="Master_CS_Checkers",font=("Arial",40),bg="#DEB887",fg='#981C03') 
window_title.pack(expand=YES)
#image dans la fenetre
image=PhotoImage(file="damierr.png").zoom(30).subsample(30)
can-Canvas(window,width=500,height=500,bg="4C87FlCM",bd=0,highlightthickness=0)
can.create_iitiage(250,250, image=image)
can.pack(expand=YES)
#création des pions
while x1<500 and y1<500:
    can.create_rectangle(x1,y1>x2,y2,fill=couleur) 
    if (num_ligne<5 and couleur=='black' )or(num_ligne>6 and couleur=='black'):
        can.create_oval(x1,y1,x2,y2,fill=ctt) 
    c,i,x1,x2=c+1,i+1,x1+50,x2+50 
    if c==10:
        y1,y2=y1+50,y2+50
        x1=0
        x2=50
        c=0
        num_ligne+=1
        i+=1
    if num_ligne>6: 
        ctt="#981C03" 
    if i%2==0:
        couleur='black'
    else: couleur='#C9AB5A'
start2=Button(window,text="Start",bg="#981C03",fg='white',font=( "Arial", 20),command="commencer_le_jeu")
start2.pack(side=BOTTOM)
#le nom du jeu
window_title=Label(text="Master_CS_Checkers",font=("Arial",40),bg="#DEB887",fg='#981C03') 
window_title.pack(expand=YES)
# image dans la fenetre
image=PhotoImage(file="damierr.png").zoom(30).subsample(30)
can=Canvas(window,width=500,height=500, bg="#C87FlC", bd=0,highlightthickness=0) 
can.create_image(250,250,image=image) 
can.pack(expand=YES)
#cneation des bouttons
start=Button(window,text="Play",bg="#981C03",fg='white1',font=("Arial",20),command= creat) 
start.pack(side=BOTTOM) |
#affichage de la fenetre 
window.mainloop()
