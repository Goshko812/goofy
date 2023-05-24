import pygame
import time
import random

pygame.init()

window_width = 800
window_height = 600

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake Game')

fps = pygame.time.Clock()

snake_block_size = 20
snake_block_width = snake_block_size
snake_block_height = snake_block_size

snake_speed = 15

font_size = 36
font = pygame.font.SysFont(None, font_size)


def snake_game():
    game_over = False
    game_exit = False

    snake_x = window_width / 2
    snake_y = window_height / 2

    snake_x_change = 0
    snake_y_change = 0

    snake_body = []
    snake_length = 1

    food_x = round(random.randrange(0, window_width - snake_block_width) / snake_block_size) * snake_block_size
    food_y = round(random.randrange(0, window_height - snake_block_height) / snake_block_size) * snake_block_size

    while not game_exit:
        while game_over:
            game_window.fill(black)
            game_over_text = font.render("Game Over! Press Q-Quit or C-Play Again", True, red)
            game_window.blit(game_over_text, [window_width / 2 - game_over_text.get_width() / 2,
                                               window_height / 2 - game_over_text.get_height() / 2])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    if event.key == pygame.K_c:
                        snake_game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_x_change = -snake_block_size
                    snake_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    snake_x_change = snake_block_size
                    snake_y_change = 0
                elif event.key == pygame.K_UP:
                    snake_y_change = -snake_block_size
                    snake_x_change = 0
                elif event.key == pygame.K_DOWN:
                    snake_y_change = snake_block_size
                    snake_x_change = 0

        if snake_x >= window_width or snake_x < 0 or snake_y >= window_height or snake_y < 0:
            game_over = True

        snake_x += snake_x_change
        snake_y += snake_y_change
        game_window.fill(black)
        pygame.draw.rect(game_window, green, [food_x, food_y, snake_block_width, snake_block_height])
        snake_head = []
        snake_head.append(snake_x)
        snake_head.append(snake_y)
        snake_body.append(snake_head)
        if len(snake_body) > snake_length:
            del snake_body[0]

        for segment in snake_body[:-1]:
            if segment == snake_head:
                game_over = True

        for segment in snake_body:
            pygame.draw.rect(game_window, blue, [segment[0], segment[1], snake_block_width, snake_block_height])

        pygame.display.update()

        if snake_x == food_x and snake_y == food_y:
            food_x = round(random.randrange(0, window_width - snake_block_width) / snake_block_size) * snake_block_size
            food_y = round(random.randrange(0, window_height - snake_block_height) / snake_block_size) * snake_block_size
            snake_length += 1

        fps.tick(snake_speed)

    pygame.quit()
    quit()


snake_game()
