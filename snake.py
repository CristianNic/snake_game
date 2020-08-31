import pygame
import random
import sys

light_gray = (40, 44, 52) #ligther gray (91, 98, 111)
dark_gray = (33, 37, 43)
red = (255,0,0)
green = (80,200,80)

screen_width = 520
screen_height = 520

gridsize = 20

class Snake():
    def __init__(self):
        pass
        
    def draw(self, surface):
        pass    

class Food():
    def __init__(self):
        self.position = (0,0)
        self.color = red
        self.random_position()
        
    def random_position(self):
        pass
        
    def draw(self, surface):
        pass

def drawGrid(surface):
    x, y = 0, 0
    for l in range(0, screen_width):
        x = x + gridsize
        y = y + gridsize
        pygame.draw.line(surface, light_gray, (x, 0), (x, screen_height))
        pygame.draw.line(surface, light_gray, (0, y), (screen_width, y)) 

def exit_keys():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
                
def main():
    pygame.init()
    pygame.display.set_caption("Snake Game")
    
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((screen_width, screen_height))
    
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    
    snake = Snake()
    food = Food()
    
    myfont = pygame.font.SysFont("None", 26)
    
    while (True):
        clock.tick(10)
        exit_keys()
        
        surface.fill(dark_gray)            
        drawGrid(surface)
        food.draw(surface)
        snake.draw(surface)
        screen.blit(surface, (0,0))
        
        text = myfont.render("Score ", 1, green)
        screen.blit(text, (10,10))
                        
        pygame.display.update()

if __name__ == '__main__':
    main()                

