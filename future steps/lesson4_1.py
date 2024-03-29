import pygame
import time
import random


dis_width = 800
dis_height = 600

pygame.init()
dis = pygame.display.set_mode(size = (dis_width, dis_height))

pygame.display.set_caption('Snake game for eKids')

snake_speed = 20
snake_block = 10
clock = pygame.time.Clock()
font_style = pygame.font.SysFont(None, 50)

def message(msg, color):
    rendered_message = font_style.render(msg, True, color)
    dis.blit(rendered_message, [dis_width / 7, dis_height / 2])

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
light_blue = (96, 148, 188)
red = (255, 0, 0)

def gameLoop():  # creating a function
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_close:

        while game_over == True:
            dis.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_close = True
                        game_over = False
                        exit()
                    if event.key == pygame.K_c:
                        gameLoop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_over = True

        x1 = x1 + x1_change
        y1 = y1 + y1_change
        dis.fill(light_blue)
        pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
        pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            print("Yummy!!")
        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
