from pygame import Color
from actor import Actor
import random
class Fruit(Actor):
    def __init__(self, pos = (400,300)):
        super().__init__(Color(255,0,0), pos)
        self.eaten = False
        
    def newPos(self):
        self.pos = (random.randrange(0, 800-self.RECT_SIZE, self.RECT_SIZE), random.randrange(0, 600-self.RECT_SIZE, self.RECT_SIZE))
        
        
        
