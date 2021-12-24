'''
A place to play :)
'''


from tkinter import *

root=Tk()
root.title('Simmu Eva!')
root.geometry('800x600')

w=600
h=400

my_canvas=Canvas(root, width=w, height=h, bg='grey')
my_canvas.pack(pady=20)

obj=my_canvas.create_rectangle(200,200,210,210)

def update(my_canvas, obj, i):
    my_canvas.move(obj, i, i)
    root.after(500, update, my_canvas, obj, i)
def start():
    update(my_canvas, obj, 10)
start_btn=Button(root, text='Start', command=start)
start_btn.place(x=50, y=500)

root.mainloop()
