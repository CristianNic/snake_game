import pygame
import random
import sys

class Snake():
    def __init__(self):
        pass

class Food():
    def __init__(self):
        pass
    
    def random_position(self):
        pass
        
    def draw():
        pass

def drawGrid():
    pass 

def main():
    pygame.init()
            
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode([500, 500])
    screen.fill((255, 255, 255))
    snake = Snake()
    food = Food()
    
    while (True):
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()
        
main()
