import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SNAKE_SIZE = 20
ORANGE_SIZE = SNAKE_SIZE
FPS = 15
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE_COLOR = (255, 165, 0)

# Directions
UP = (0, -SNAKE_SIZE)
DOWN = (0, SNAKE_SIZE)
LEFT = (-SNAKE_SIZE, 0)
RIGHT = (SNAKE_SIZE, 0)

# Setup the screen and fonts
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

class Snake:
    def __init__(self):
        self.segments = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.direction = RIGHT
        self.grow = False

    def get_head_position(self):
        return self.segments[0]

    def turn(self, point):
        if (point[0] * -1, point[1] * -1) == self.direction:
            return
        self.direction = point

    def update(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x)) % SCREEN_WIDTH), (cur[1] + (y)) % SCREEN_HEIGHT)
        if self.grow:
            self.segments.insert(0, new)
            self.grow = False
        else:
            self.segments.insert(0, new)
            self.segments.pop()

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(UP)
                elif event.key == pygame.K_DOWN:
                    self.turn(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.turn(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.turn(RIGHT)

    def draw(self, surface):
        for segment in self.segments:
            pygame.draw.rect(surface, GREEN, pygame.Rect(segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))

    def check_collision(self):
        head = self.get_head_position()
        return head in self.segments[1:]

class Orange:
    def __init__(self):
        self.position = (0, 0)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, (SCREEN_WIDTH // ORANGE_SIZE) - 1) * ORANGE_SIZE,
                         random.randint(0, (SCREEN_HEIGHT // ORANGE_SIZE) - 1) * ORANGE_SIZE)

    def draw(self, surface):
        pygame.draw.rect(surface, ORANGE_COLOR, pygame.Rect(self.position[0], self.position[1], ORANGE_SIZE, ORANGE_SIZE))

def main():
    snake = Snake()
    orange = Orange()
    score = 0

    while True:
        snake.handle_keys()
        snake.update()

        if snake.get_head_position() == orange.position:
            snake.grow = True
            orange.randomize_position()
            score += 10

        if snake.check_collision():
            break

        screen.fill(BLACK)
        snake.draw(screen)
        orange.draw(screen)
        draw_text(f'Score: {score}', font, WHITE, screen, SCREEN_WIDTH // 2, 20)

        pygame.display.flip()
        clock.tick(FPS)

    game_over_screen()

def game_over_screen():
    screen.fill(BLACK)
    draw_text('Game Over', font, RED, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20)
    draw_text('Press Q to Quit or C to Play Again', font, WHITE, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_c:
                    main()

if __name__ == "__main__":
    main()

