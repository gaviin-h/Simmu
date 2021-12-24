import math
from brain import brain
from tkinter import Canvas
class mini:
    xpos: int
    ypos: int
    mind=brain()
    energy: int
    dir: int
    vision: int
    points: list
    parent_canvas: Canvas()
    rendered_mini: Canvas.create_polygon
    directions={0:90,90:180,180:270}
    reverse_directions={0:270,270:180,180:90,90:0}

    def mini(self, x, y, canvas):
        self.xpos=x
        self.ypos=y
        self.energy=100
        self.dir=90
        self.vision=25
        self.points=[self.xpos,self.ypos-7,self.xpos-5, self.ypos+7, self.xpos+5, self.ypos+7]
        self.parent_canvas=canvas
        self.rendered_mini=self.parent_canvas.create_polygon(self.points, outline='#f11', width=2)


    def eat(self, inp):
        self.energy = min(100, self.energy+inp.energy)
        self.parent_canvas.delete(inp)
    
    def move(self):
        mv_x=int(math.cos(math.radians(self.dir)))
        mv_y=int(math.sin(math.radians(self.dir)))
        self.xpos+=mv_x
        self.ypos+=mv_y
        self.energy-=2
        self.parent_canvas.move(self.rendered_mini, 5*mv_x, 5*mv_y)

    def turn(self, right_or_left):
        self.dir=max(right_or_left*self.directions[self.dir], -right_or_left*self.reverse_directions[self.dir])
        p1=self.xpos+7*int(math.cos(math.radians(self.dir))), self.ypos-7*int(math.sin(math.radians(self.dir)))
        p2=self.xpos-(5*int(math.sin(math.radians(self.dir))) + 7*int(math.sin(math.radians(self.dir)))), self.ypos+(-5*int(math.sin(math.radians(self.dir))) + 7*int(math.sin(math.radians(self.dir))))
        p3=self.xpos+(-7*int(math.cos(math.radians(self.dir))) + 5*int(math.sin(math.radians(self.dir)))), self.ypos+(5*int(math.cos(math.radians(self.dir))) + 7*int(math.sin(math.radians(self.dir))))
        self.points=[p1[0], p1[1], p2[0], p2[1], p3[0], p3[1]]
        self.parent_canvas.delete(self.rendered_mini)
        self.parent_canvas.create_polygon(self.points, outline='#f11', width=2)
        
    def get_pos(self):
        return self.xpos, self.ypos
    
    def sex(self, other: mini):
        self.energy-=20
        mind=self.mind.brain_merge(other.mind)
        kid=mini(self.xpos, self.ypos, mind, self.parent_canvas)
        return kid
    
    def go(self, inputs):
        output=self.mind.fire_all(inputs)
        return output.argmax()      
        

    def die(self):
        self.parent_canvas.delete(self.rendered_mini)


class snack:
    energy: int
    xpos: int
    ypos: int
    parent_canvas: Canvas()
    rendered_snack: Canvas.create_polygon

    def snack(self, x, y, energy, canvas):
        self.xpos=x
        self.ypos=y
        self.energy=energy
        self.parent_canvas=canvas
        self.parent_canvas.create_oval(self.xpos, self.ypos, self.xpos+10, self.ypos+10)
    
    def get_pos(self):
        return self.xpos, self.ypos
