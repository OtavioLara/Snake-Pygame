from keyboard import KeyboardHandler
from fruit import Fruit
import sys
class GameScene:
    
    def __init__(self, color):
        self.color = color
        self.snakes = []
        self.fruit = Fruit()
        self.kb_handler = KeyboardHandler()
        
    def add_snake(self, snake):
        self.snakes.append(snake)
    
    def update_actors(self):
        for snake in self.snakes:
            direction = self.kb_handler.update()
            snake.move(direction)
            self.detect_colision(snake, direction)
            
    def detect_colision(self, snake, direction):
        for piece in snake.body:
            if(piece == self.fruit.pos):
                snake.pontuation += 1
                snake.eat(direction)
                self.fruit.newPos()
                cont = 0
                for other_piece in snake.body:
                    if(piece == other_piece):
                        cont += 1
                if(cont >= 2):
                    sys.exit()
            if(0 > piece[0] < 800 or 0 > piece[1] < 600):
                snake.colide()
                
    
