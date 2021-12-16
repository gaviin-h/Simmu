from tkinter import *
from mini import mini, snack
from brain import brain
import numpy as np

root=Tk()
root.title('Simmu Eva!')
root.geometry('800x600')

w=600
h=400
x=w//2
y=h//2

my_canvas=Canvas(root, width=w, height=h, bg='grey')
my_canvas.pack(pady=20)

meme=mini()
mind=brain()
meme.mini(x,y,mind.brain())
pellet=snack()
pellet.snack(x+50, y+10, 20)

my_circle=my_canvas.create_oval(pellet.xpos, pellet.ypos, pellet.xpos+10, pellet.ypos+10)
points=[x,y,x-10, y+7, x-7, y+10, x+7, y+10, x+10, y+7]
my_mini=my_canvas.create_polygon(points, outline='#f11', width=2)
def update():  
    mv=meme.move()
    my_canvas.move(my_mini, mv[0], mv[1])
    if not stop:
        root.after(500, update)

stop=False
def start():
    global stop
    stop=False
    update()


def stopper():
    global stop
    stop=True

start_btn=Button(root, text='Start', command=start)
start_btn.place(x=50, y=500)
quit_btn=Button(root, text='Stop', command=stopper)
quit_btn.place(x=400, y=500)
quit_btn=Button(root, text='Quit', command=root.destroy)
quit_btn.place(x=650, y=500)

root.mainloop()