#!/usr/bin/env python
# -*- coding: utf-8 -*-

from directions import Direction as dirs
from actor import Actor
from pygame import Color
class Snake(Actor):
    
    def __init__(self, headPos = (100,0), size = 3, color = Color(0,0,0)):
        '''Define a snake'''
        super().__init__(color, headPos)
        self.body = []
        self.create_snake_body(headPos, size)
        self.current = dirs.RIGHT
        self.pontuation = 0
        
    def create_snake_body(self, headPos, size):
        for i in range(size, 0, -1):
            self.body.append((headPos[0]-(i*self.RECT_SIZE),headPos[1]))
            
    def move(self, direction, eating = False):
        if(direction == dirs.CONTINUE):
            direction = self.current
            
        if(direction == dirs.UP):
            if self.current != dirs.DOWN: 
                self.body.append((self.body[-1][0], self.body[-1][1] - self.RECT_SIZE)) 
            else:
                self.move(dirs.DOWN)
                return
        elif(direction == dirs.DOWN):
            if self.current != dirs.UP: 
                self.body.append((self.body[-1][0], self.body[-1][1] + self.RECT_SIZE)) 
            else:
                self.move(dirs.UP)
                return
        elif(direction == dirs.LEFT):
            if self.current != dirs.RIGHT: 
                self.body.append((self.body[-1][0] - self.RECT_SIZE, self.body[-1][1])) 
            else: 
                self.move(dirs.RIGHT)
                return
        elif(direction == dirs.RIGHT):
            if self.current != dirs.LEFT: 
                self.body.append((self.body[-1][0] + self.RECT_SIZE, self.body[-1][1])) 
            else:
                self.move(dirs.LEFT)
                return
   
        if(not eating):
            self.body.pop(0)
        self.current = direction
    
    def eat(self, direction):
        self.move(direction, True)
    
    def colide(self):
        self.body.pop(0)
    
    def snake_size(self):
        return len(self.body)
