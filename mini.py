import math
from brain import brain

class mini:
    xpos: int
    ypos: int
    mind: brain()
    energy: int
    dir: int
    vision: int

    def mini(self, x, y, mind):
        self.xpos=x
        self.ypos=y
        self.mind=mind
        self.energy=100
        self.dir=90
        self.vision=25

    def eat(self, inp):
        self.energy = min(100, self.energy+inp)
    
    def move(self):
        mv_x=int(math.cos(math.radians(self.dir)))
        mv_y=int(math.sin(math.radians(self.dir)))
        self.xpos+=mv_x
        self.ypos+=mv_y
        self.energy-=2
        return 5*mv_x, 5*mv_y
    
    def turn(self, right_or_left):
        if right_or_left == 0:
            self.dir+=90
        else:
            self.dir-=90

    def getpos(self):
        return self.xpos, self.ypos
    
    def sex(self, other: mini):
        self.energy-=20
        mind=self.mind.brain_merge(other.mind)
        return mini(self.xpos, self.ypos, mind)
    
    def go(self, inputs):
        return self.mind.fire_all(inputs)

class snack:
    energy: int
    xpos: int
    ypos: int

    def snack(self, x, y, energy):
        self.xpos=x
        self.ypos=y
        self.energy=energy

