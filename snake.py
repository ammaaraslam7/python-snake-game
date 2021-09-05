# importing libraries
import pygame
import time
import random

snake_speed = 15
window_x = 720
window_y = 480

# Colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)


pygame.init()


pygame.display.set_caption('Simple Snake')
game_window = pygame.display.set_mode((window_x, window_y))

fps = pygame.time.Clock()

# Snake's default position
snake_position = [100, 50]

snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]
# food posiiton
food_position = [random.randrange(1, (window_x//10)) * 10,
                 random.randrange(1, (window_y//10)) * 10]

food_spawn = True

# Default snake's direction
direction = 'RIGHT'
change_to = direction

# initial score
score = 0


def show_score(choice, color, font, size):

    score_font = pygame.font.SysFont(font, size)

    score_surface = score_font.render('Score : ' + str(score), True, color)

    score_rect = score_surface.get_rect()

    game_window.blit(score_surface, score_rect)

# game over function


def game_over():

    my_font = pygame.font.SysFont('times new roman', 50)
    if score <= 10:
        game_over_surface = my_font.render(
            'Your Score is : ' + str(score), True, red)
    elif score > 10:
        game_over_surface = my_font.render(
            'Your Score is : ' + str(score), True, green)

    game_over_rect = game_over_surface.get_rect()

    game_over_rect.midtop = (window_x/2, window_y/4)

    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    time.sleep(2)

    pygame.quit()
    quit()


# Main Function
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Ignore if two keys pressed simultaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Moving the snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Growing snake's body when it eats food
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        score += 10
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_position = [random.randrange(1, (window_x//10)) * 10,
                         random.randrange(1, (window_y//10)) * 10]

    food_spawn = True
    game_window.fill(white)

    for pos in snake_body:
        pygame.draw.rect(game_window, blue,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, green, pygame.Rect(
        food_position[0], food_position[1], 10, 10))

    # Conditions for the game to stop
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()

    # Touching the snake's body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    show_score(1, black, 'times new roman', 20)

    # Refresh game screen
    pygame.display.update()
    fps.tick(snake_speed)
