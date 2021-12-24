from tkinter import *
from mini import mini, snack
import numpy as np
import math

root=Tk()
root.title('Simmu Eva!')
root.geometry('1200x1200')

w=1000
h=1000
x=w//2
y=h//2

## create the environment 
my_canvas=Canvas(root, width=w, height=h, bg='grey')
my_canvas.pack(pady=20)

## create some minis
mini1=mini()
mini1.mini(x,y, my_canvas)
snack1=snack()
snack1.snack(x+50, y+10, 20, my_canvas)

current_minis=[mini1] 
current_food=[snack1]      

## helper methods
def in_sight(item, cur):
    if item.xpos in range(cur.xpos-cur.vision, cur.xpos+cur.vision) and item.ypos in range(cur.ypos-cur.vision, cur.ypos+cur.vision):
        return True
    return False

def rel_distance(item, cur):
    direction=math.atan2(cur.xpos-item.xpos, cur.ypos-item.ypos)
    return [math.dist(cur.get_pos(), item.get_pos()), math.degrees(direction)]

def vision_input(iter, r, cur, inputs, current_arr, in_range, i):
    item=current_arr[iter]
    if in_sight(item, cur):
        distance_info=rel_distance(item, cur)  
        if(distance_info[0]<inputs[i]):
            inputs[i]=distance_info[0] ## distance val to the correct input
            inputs[i+1]=distance_info[1]
            if distance_info[0]<5:
                in_range.append(item)
    if iter+1<r:
        root.after(1, vision_input, iter+1, r, cur, inputs, current_arr, in_range, i)

def get_inputs(cur):
    inputs=np.full([8], 50)
    in_range_food,in_range_mate=[],[]     
    vision_input(0, len(current_food), cur, inputs, current_food, in_range_food, 0)
    vision_input(0, len(current_minis), cur, inputs, current_minis, in_range_mate, 2)
    inputs[4],inputs[5]=cur.get_pos()
    inputs[6]=cur.dir
    inputs[7]=cur.energy
    return inputs, in_range_food, in_range_mate

## universal update method
def update(n_mini):  
    ## after through the list and update
    cur_mini=current_minis[n_mini]
    inputs,in_range_food, in_range_mate=get_inputs(cur_mini)
    next=cur_mini.go(inputs)
    if next==0:
        cur_mini.move()  ## sort this out 
        print('move')
    elif next==1:
        cur_mini.turn(1)
        print('turn right')
    elif next==2:
        cur_mini.turn(-1)
        print('turn left')
    elif next==3:
        if in_range_food:
            cur_mini.eat(in_range_food) 
            my_canvas.delete(in_range_food[0])
            current_food.remove(in_range_food[0])
            print('eat')
    elif next==4:
        if in_range_mate:
            cur_mini.sex(in_range_mate[0])
            print('fuck')
    if cur_mini.energy<=0:
        my_canvas.delete(cur_mini.rendered_mini)
        current_minis.remove(cur_mini)
        n_mini-=1
    cur_mini.energy-=2                
    if not stop:
        if n_mini+1==len(current_minis):
            n_mini=-1
        root.after(250, update, n_mini+1)

stop=False
def start():
    global stop
    stop=False
    update(0)


def stopper():
    global stop
    stop=True

## Set up the board
start_btn=Button(root, text='Start', command=start)
start_btn.place(x=100, y=1100)
quit_btn=Button(root, text='Stop', command=stopper)
quit_btn.place(x=500, y=1100)
quit_btn=Button(root, text='Quit', command=root.destroy)
quit_btn.place(x=1000, y=1100)

root.mainloop()