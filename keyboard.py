import pygame
import sys
from directions import Direction as dirs

class KeyboardHandler:

    def update(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    return dirs.LEFT
                elif event.key == pygame.K_RIGHT:
                    return dirs.RIGHT
                elif event.key == pygame.K_UP:
                    return dirs.UP
                elif event.key == pygame.K_DOWN:
                    return dirs.DOWN
                if event.key == pygame.K_q:
                    print("Good bye")
                    sys.exit()
        return dirs.CONTINUE
