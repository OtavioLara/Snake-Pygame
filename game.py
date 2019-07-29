from screen import Screen
from snake import Snake
from time import sleep
import pygame
from pygame import Color
class Game:
    def __init__(self):
        pygame.init()
        self.screen = Screen()
        self.snake1 = Snake()
        self.screen.scene.add_snake(self.snake1)
        
        
    def run(self):
        while True:
            self.screen.drawSnakes()
            sleep(0.1)
            
def main(args):
    Game().run()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
