import pygame
import random
import sys

light_gray = (40, 44, 52)   # ligther gray (91, 98, 111)
dark_gray = (33, 37, 43)
red = (255,0,0)
green = (80,200,80)

screen_width = 520
screen_height = 520

gridsize = 20

up = (0,-1)
down = (0,1)
left = (-1,0)
right = (1,0)
    
class Snake():
    def __init__(self):
        self.length = 1
        self.color = green
        self.score = 0         
        self.position = [((screen_width/2), (screen_height/2))]
        self.direction = random.choice([up, down, left, right])
        
    def get_head_position(self):
        return self.position[0]

    def turn(self, point):
        if self.length > 1 and (point[0]*-1, point[1]*-1) == self.direction:
            return
        else:
            self.direction = point
                  
    def move(self):
        current_head = self.get_head_position()
        x,y = self.direction 
        new = (((current_head[0]+(x*gridsize))%screen_width), (current_head[1]+(y*gridsize))%screen_height)
        if len(self.position) > 2 and new in self.position[2:]:
            self.reset()
        else:
            self.position.insert(0,new)
            if len(self.position) > self.length:
                self.position.pop()

    def draw(self, surface):
        for p in self.position:
            rect = pygame.Rect((p[0], p[1]), (gridsize,gridsize))
            pygame.draw.rect(surface, self.color, rect)
                    
    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()                
                elif event.key == pygame.K_UP:
                    self.turn(up)
                elif event.key == pygame.K_DOWN:
                    self.turn(down)
                elif event.key == pygame.K_LEFT:
                    self.turn(left)
                elif event.key == pygame.K_RIGHT:
                    self.turn(right)    
    
    def reset(self):
        self.length = 1
        self.position = [((screen_width/2), (screen_height/2))]
        self.direction = random.choice([up, down, left, right])
        self.score = 0
            
class Food():
    def __init__(self):
        self.position = (0,0)
        self.color = red
        self.random_position()

    def random_position(self):
        # Random number between 0 and 520 divisible by 20
        x = random.randrange(0, (screen_width-1), 20)
        y = random.randrange(0, (screen_height-1), 20)
        self.position = (x, y)

    def draw(self, surface):
        # rect = (top left corner(x, y), rectangle size(width, height))
        rect = ((self.position[0], self.position[1]), (gridsize, gridsize))
        pygame.draw.rect(surface, self.color, rect)

def drawGrid(surface):
    x, y = 0, 0
    for l in range(0, screen_width):
        x = x + gridsize
        y = y + gridsize
        pygame.draw.line(surface, light_gray, (x, 0), (x, screen_height))
        pygame.draw.line(surface, light_gray, (0, y), (screen_width, y))
                                                            
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
        surface.fill(dark_gray)
        drawGrid(surface)
        
        if snake.get_head_position() == food.position:
            snake.length += 1
            snake.score += 1
            food.random_position()        
      
        food.draw(surface)
        snake.handle_keys()
        snake.move()
        snake.draw(surface)
        
        screen.blit(surface, (0,0))

        text = myfont.render("Score  " + str(snake.score), 1, green)
        screen.blit(text, (10,10))

        pygame.display.update()
        
        # Game over score if it hits the sides of the screen (next add if it crosses it's own tail)
        if snake.position[0][0] in [0,screen_width] or snake.position[0][1] in [0,screen_height]:
            game_over_font = pygame.font.SysFont("None", 42)
            gameover = game_over_font.render("Score  " + str(snake.score), 1, green)
            rect = gameover.get_rect()
            rect.center = screen.get_rect().center
            screen.blit(gameover, rect)
            pygame.display.update()            
            pygame.time.wait(500)    
            snake.reset()
            food.random_position()
 
    pygame.display.update()

if __name__ == '__main__':
    main()
