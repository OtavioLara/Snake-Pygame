from pygame import Surface, draw, Color, display, image
from game_scene import GameScene
from pygame import Color
from pygame import font
import os
class Screen:
    '''Draw actors in the scenes'''
    def __init__(self):
        self.scene = GameScene(Color(255,255,255))
        self.display = display.set_mode((800, 600))
        self.display.fill(self.scene.color)
        self.font = font.Font(font.match_font('bitstreamverasans'), 20)
        
        # ~ if(image.get_extended()):
            # ~ self.background = image.load(os.path.abspath("desert.jpg"))
            # ~ self.background = self.background.convert()
        
    def drawSnakes(self):
        self.scene.update_actors()
        # ~ if(image.get_extended()): self.display.blit(self.background, (0,0))
        for snake in self.scene.snakes:
            self.display.fill(self.scene.color)
            for piece in snake.body:
                draw.rect(self.display, snake.color, [piece[0], piece[1], snake.RECT_SIZE, snake.RECT_SIZE])
            self.display.blit(self.font.render(str(snake.pontuation), True, Color(255,0,0)), (self.display.get_width()/2, 0))
        draw.rect(self.display, self.scene.fruit.color, [self.scene.fruit.pos[0], self.scene.fruit.pos[1], self.scene.fruit.RECT_SIZE, self.scene.fruit.RECT_SIZE])
        
        display.update()
        
