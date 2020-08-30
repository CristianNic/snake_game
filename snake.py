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
        
    def draw(self, surface):
        pass

def drawGrid():
    pass 

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

def main():
    pygame.init()
    
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill((255, 255, 255))
            
    snake = Snake()
    food = Food()
    
    while (True):
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    
        pygame.display.update()
        
main()
