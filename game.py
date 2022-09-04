import random
from collections import namedtuple
import pygame
from algorithm import Direction, HamiltonianPath

pygame.init()

Point = namedtuple("Point", "x, y")


class SnakeGame:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED_GRADIENT = [(123, 0, 0), (255, 0, 0)]
    GREEN_GRADIENT = [(56, 115, 24), (100, 204, 43)]
    YELLOW_GRADIENT = [(201, 141, 2), (252, 215, 3)]
    MENU_COLOR = (40, 10, 70)
    MENU_FONT = pygame.font.SysFont("helvetica", 35, bold=True, italic=False)

    BLOCK_SIZE = 80
    SPEED = 10

    def __init__(self, width=640, height=320):
        self.width = width
        self.height = height

        self.display = pygame.display.set_mode(
            (self.width, self.height+self.BLOCK_SIZE))
        pygame.display.set_caption("Snake")
        self.clock = pygame.time.Clock()

        self.algorithm = HamiltonianPath(
            width//self.BLOCK_SIZE,
            height//self.BLOCK_SIZE)

        self.score = 0
        self.max_score = 29
        self.counter = 0
        self.snake = None
        self.head = None
        self.direction = None

        self.algorithm.graph_init()
        self.place_snake()
        self.place_food()
        self.path_init()
        self.update_display()

    def place_snake(self):
        snake_coordinates = (
            list(range(0, self.width, self.BLOCK_SIZE)),
            list(range(0, self.height, self.BLOCK_SIZE))
        )

        dim1 = random.choice([0, 1])
        dim2 = abs(dim1-1)
        ind1, ind2 = (random.randint(0, len(snake_coordinates[dim1])-3),
                      random.randint(0, len(snake_coordinates[dim2])-1))

        is_reverse = random.choice([-1, 1])
        if dim2:
            coords = (snake_coordinates[dim1][ind1:ind1+3][::is_reverse],
                      [snake_coordinates[dim2][ind2]]*3)
        else:
            coords = ([snake_coordinates[dim2][ind2]]*3,
                      snake_coordinates[dim1][ind1:ind1+3][::is_reverse])

        self.snake = [Point(x, y) for x, y in zip(*coords)]
        self.head = self.snake[0]

    def place_food(self):
        x = random.randint(0, (self.width-self.BLOCK_SIZE) //
                           self.BLOCK_SIZE)*self.BLOCK_SIZE
        y = random.randint(0, (self.height-self.BLOCK_SIZE) //
                           self.BLOCK_SIZE)*self.BLOCK_SIZE
        self.food = Point(x, y)
        if self.food in self.snake:
            self.place_food()

    def path_init(self):
        self.snake_body = [self.get_block_id(pt) for pt in self.snake]

        self.algorithm.change_adjacents(self.snake_body)
        self.algorithm.get_cycle(self.snake_body[0])
        self.algorithm.path.popleft()

    def get_block_id(self, point):
        x_pos = point.x // self.BLOCK_SIZE
        y_pos = point.y // self.BLOCK_SIZE

        return int(y_pos*(self.width//self.BLOCK_SIZE) + x_pos)

    def play_step(self):
        self.direction = self.algorithm.path[self.counter %
                                             self.algorithm.num_vertices]
        self.counter += 1

        self.move(self.direction)
        self.snake.insert(0, self.head)

        if self.is_collision():
            return

        if self.head == self.food:
            self.score += 1
            if self.score != self.max_score:
                self.place_food()
        else:
            self.snake.pop()

        self.update_display()
        self.clock.tick(self.SPEED)

    def is_collision(self):
        if self.head.x > self.width - self.BLOCK_SIZE \
           or self.head.x < 0 or self.head.y > self.height - self.BLOCK_SIZE \
           or self.head.y < 0:
            return True
        if self.head in self.snake[1:]:
            return True
        return False

    def move(self, direction):
        x = self.head.x
        y = self.head.y
        if direction == Direction.RIGHT:
            x += self.BLOCK_SIZE
        elif direction == Direction.LEFT:
            x -= self.BLOCK_SIZE
        elif direction == Direction.DOWN:
            y += self.BLOCK_SIZE
        elif direction == Direction.UP:
            y -= self.BLOCK_SIZE

        self.head = Point(x, y)

    def update_display(self):
        self.display.fill(self.BLACK)
        self.draw_apple()
        self.draw_snake()
        self.display_menu()
        pygame.display.flip()

    def draw_apple(self):
        pygame.draw.circle(self.display, self.RED_GRADIENT[0],
                           (self.food.x+self.BLOCK_SIZE//2,
                           self.food.y+self.BLOCK_SIZE//2),
                           self.BLOCK_SIZE//3)
        pygame.draw.circle(self.display, self.RED_GRADIENT[1],
                           (self.food.x+self.BLOCK_SIZE//2,
                           self.food.y+self.BLOCK_SIZE//2),
                           self.BLOCK_SIZE//4)

    def draw_snake(self):
        snake_color = self.YELLOW_GRADIENT
        for pt in self.snake:
            pygame.draw.rect(self.display, snake_color[0],
                             pygame.Rect(pt.x, pt.y, self.BLOCK_SIZE, self.BLOCK_SIZE))
            pygame.draw.rect(self.display, snake_color[1],
                             pygame.Rect(pt.x+8, pt.y+8, 64, 64))
            snake_color = self.GREEN_GRADIENT

    def display_menu(self):
        pygame.draw.rect(self.display, self.MENU_COLOR,
                         (0, self.height, self.width, self.BLOCK_SIZE))

        text = self.MENU_FONT.render(
            "SCORE: " + str(self.score), True, self.WHITE)
        self.display.blit(
            text, [self.width/2-self.BLOCK_SIZE, self.height+self.BLOCK_SIZE/4])
