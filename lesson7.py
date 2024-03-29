import pygame
import time
import random

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
light_blue = (96, 148, 188)
red = (255, 0, 0)
orange = (255, 165, 48)
violet = (117, 48, 255)

dis_width = 800
dis_height = 600
pygame.init()
dis = pygame.display.set_mode(size = (dis_width, dis_height))
pygame.display.set_caption('Snake game for eKids')

snake_block = 10
snake_speed = 15
clock = pygame.time.Clock()
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
background_img = pygame.image.load('assets/img/sand1.jpg')


def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [25,25])


def draw_our_snake(snake_block, snake_list):
    for x in snake_list[0: -1]:
        pygame.draw.rect(dis, black, [cell[0], cell[1], snake_block, snake_block])
    pygame.draw.rect(dis, red, [snake_list[-1][0], snake_list[-1][1], snake_block, snake_block])


def message(msg, color):
    rendered_message = font_style.render(msg, True, color)
    dis.blit(rendered_message, [dis_width / 6, dis_height / 3])


def starting_screen():
    while True:
        for i in range(-10, 1):
            dis.fill(orange)
            message('Game will start in: ' + str(i*(-1)) + ' or press r to run the game', violet)
            pygame.display.update()
            time.sleep(1)
            if i == 0:
                gameLoop()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        gameLoop()


def gameLoop():  # creating a function
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1
    food_x = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
    food_y = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block

    while not game_close:

        while game_over == True:
            dis.fill(white)
            message("Ви програли! Q-Вихід або C-Грати знову", red)
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
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width:
            x1 = 0
        if x1 < 0:
            x1 = dis_width
        if y1 >= dis_height:
            y1 = 0
        if y1 < 0:
            y1 = dis_height

        x1 += x1_change
        y1 += y1_change
        dis.blit(background_img, [0, 0])
        pygame.draw.rect(dis, green, [food_x, food_y, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_over = True

        draw_our_snake(snake_block, snake_list)
        your_score(length_of_snake - 1)

        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            print("Yummy!!")
            food_x = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
            food_y = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


starting_screen()
