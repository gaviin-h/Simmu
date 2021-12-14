import math
from brain import brain

class mini:
    xpos: int
    ypos: int
    brain=brain()
    energy: int
    dir: int

    def mini(self, x, y, brain):
        self.xpos=x
        self.ypos=y
        self.brain=brain
        self.energy=100

    def eat(self, inp):
        self.energy = min(100, self.energy+inp)
    
    def move(self):
        self.xpos+=self.dir*math.cos(dir)
        self.ypos+=self.dir*math.sin(dir)
        self.energy-=2 
    
    def turn(self, right_or_left):
        if right_or_left == 0:
            self.dir+=90
        else:
            self.dir-=90

    def getpos(self):
        return self.xpos, self.ypos
    
    def sex(self, other: mini):
        self.energy-=20
        brain=self.brain.brain_merge(other.brain)
        return mini(self.xpos, self.ypos, brain)

class snack:
    energy: int
    xpos: int
    ypos: int

    def snack(self, x, y, energy):
        self.xpos=x
        self.ypos=y
        self.energy=energy
