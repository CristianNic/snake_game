import pygame
import random
import sys

class Snake():
    def __init__(self):
        pass

class Food():
    def __init__(self):
        self.position = (0,0)
        self.color = (255,0,0)
        self.random_position()
        
    def random_position(self):
        pass
        
    def draw(self, surface):
        pass

def drawGrid(surface):
    x, y = 0, 0
    for l in range(0, screen_width):
        x = x + 20
        y = y + 20
        pygame.draw.line(surface, (40, 44, 52), (x, 0), (x, screen_height))
        pygame.draw.line(surface, (40, 44, 52), (0, y), (screen_width, y))   # light gray (40, 44, 52),  ligther gray (91, 98, 111)

screen_width = 520
screen_height = 520

gridsize = 20
grid_width = screen_width/gridsize
grid_height = screen_height/gridsize


def main():
    pygame.init()
    pygame.display.set_caption("Snake Game")
    
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((screen_width, screen_height))
    x = screen.fill((33, 37, 43))
    
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
      
    snake = Snake()
    food = Food()
    
    while (True):
        clock.tick(10)
        drawGrid(surface)
        screen.blit(surface, (0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        
        food.draw(surface)
                    
        pygame.display.update()

        
main()
