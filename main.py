import pygame
from game import SnakeGame


def main():
    game = SnakeGame()
    execute = True
    playing = False
    solved = False

    while execute:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                execute = False
            if event.type != pygame.KEYDOWN:
                continue
            if event.key == pygame.K_RETURN and not playing and not solved:
                playing = True
                game.algorithm.graph_init()
                game.path_init()
                game.score = 0
                game.counter = 0
            if event.key == pygame.K_SPACE and not playing:
                playing = False
                solved = False
                game.score = 0
                game.place_snake()
                game.place_food()
                game.update_display()

        if game.score != game.max_score and playing:
            game.play_step()

        if game.score == game.max_score:
            playing = False
            solved = True

    pygame.quit()


if __name__ == "__main__":
    main()
