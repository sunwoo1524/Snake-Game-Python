import pygame
import random

pygame.init()

pygame.display.set_caption("Snake Game")

width = 400
height = 400
screen = pygame.display.set_mode((width, height))
row = 18
col = 18
rect_size = int(width / 18)

class Snake:
    def __init__(self):
        self.pos = [[3, 1], [2, 1], [1, 1]]
        self.dir = "right"
        self.apple = [random.randint(0, row - 1), random.randint(0, row - 1)]
        self.score = 0
    
    def move(self):
        head_pos = [self.pos[0][0], self.pos[0][1]]

        if self.dir == "up":
            head_pos[1] -= 1
        elif self.dir == "down":
            head_pos[1] += 1           
        elif self.dir == "left":
            head_pos[0] -= 1
        elif self.dir == "right":
            head_pos[0] += 1
        
        if head_pos[0] < 0:
            head_pos[0] = row - 1
        elif head_pos[0] >= row:
            head_pos[0] = 0
        
        if head_pos[1] < 0:
            head_pos[1] = col - 1
        elif head_pos[1] >= col:
            head_pos[1] = 0
        
        self.pos.insert(0, head_pos)

        if self.pos[0] != self.apple:
            self.pos.pop()
        else:
            self.apple = [random.randint(0, row - 1), random.randint(0, row - 1)]
            self.score += 1
    
    def draw(self):
        for value in self.pos:
            pygame.draw.rect(screen, pygame.Color(0, 255, 0), (value[0] * rect_size, value[1] * rect_size, rect_size, rect_size))
            pygame.draw.rect(screen, pygame.Color(0, 0, 0), (value[0] * rect_size, value[1] * rect_size, rect_size, rect_size), 3)
        
        pygame.draw.rect(screen, pygame.Color(255, 0, 0), (self.apple[0] * rect_size, self.apple[1] * rect_size, rect_size, rect_size))
        pygame.draw.rect(screen, pygame.Color(0, 0, 0), (self.apple[0] * rect_size, self.apple[1] * rect_size, rect_size, rect_size), 3)
    
    def gameover(self):
        for index, value in enumerate(self.pos):
            if index != 0 and self.pos[0][0] == value[0] and self.pos[0][1] == value[1]:
                return True
        
        return False

snake = Snake()
clock = pygame.time.Clock()
keydown = True
gameover = False

if __name__ == "__main__":
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN and keydown and not gameover:
                if event.key == pygame.K_UP and snake.dir != "down":
                    snake.dir = "up"
                elif event.key == pygame.K_DOWN and snake.dir != "up":
                    snake.dir = "down"
                elif event.key == pygame.K_LEFT and snake.dir != "right":
                    snake.dir = "left"
                elif event.key == pygame.K_RIGHT and snake.dir != "left":
                    snake.dir = "right"

                keydown = False
        
        screen.fill(pygame.Color(0, 0, 0))

        if gameover:
            font = pygame.font.SysFont(None, 50)
            text = font.render("Game Over!", True, pygame.Color(255, 255, 255))
            text_rect = text.get_rect()
            text_rect.centerx = round(width / 2)
            text_rect.y = height / 2 - 50
            screen.blit(text, text_rect)
            font = pygame.font.SysFont(None, 30)
            text = font.render(f"Your score is {snake.score}", True, pygame.Color(255, 255, 255))
            text_rect = text.get_rect()
            text_rect.centerx = round(width / 2)
            text_rect.y = height / 2 + 30
            screen.blit(text, text_rect)
        else:
            snake.move()
            snake.draw()
            font = pygame.font.SysFont(None, 40)
            text = font.render(f"{snake.score}", True, pygame.Color(255, 255, 255))
            text_rect = text.get_rect()
            text_rect.centerx = round(width / 2)
            text_rect.y = 10
            screen.blit(text, text_rect)
        
        if snake.gameover():
            gameover = True
        
        keydown = True
        
        pygame.display.update()
        clock.tick(15)
