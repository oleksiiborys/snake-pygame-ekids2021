import pygame
import time
import random
from assets import fruits


dis_width = 800
dis_height = 600
pygame.init()
dis = pygame.display.set_mode(size = (dis_width, dis_height))
pygame.display.set_caption('Snake game for eKids')
icon = pygame.image.load('assets/img/head.png')
pygame.display.set_icon(icon)

initial_snake_speed = 10
snake_block = 20

clock = pygame.time.Clock()
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
apple_sound = pygame.mixer.Sound('assets/sound/apple.wav')
game_over_sound = pygame.mixer.Sound('assets/sound/gameover.wav')
snake_head_img = pygame.image.load('assets/img/head.png')
snake_body_img = pygame.image.load('assets/img/body.png')


def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [25,25])


def draw_our_snake(snake_block, snake_list):
    for x in snake_list[0:-1]:
        dis.blit(snake_body_img, (x[0], x[1]))
    dis.blit(snake_head_img, (snake_list[-1][0], snake_list[-1][1]))

def message(msg, color):
    rendered_message = font_style.render(msg, True, color)
    dis.blit(rendered_message, [dis_width / 6, dis_height / 3])

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
light_blue = (96, 148, 188)
red = (255, 0, 0)

def gameLoop():  # creating a function
    game_over = False
    game_close = False
    current_fruit = 0
    snake_speed = initial_snake_speed

    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = snake_block
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

        # if x1 >= dis_width:
        #     x1 = 0
        # elif x1 < 0:
        #     x1 = dis_width
        # elif y1 < 0:
        #     y1 = dis_height
        # elif y1 >= dis_height:
        #     y1 = -snake_block

        # region demo mode
        # if y1 >= dis_height:
        #     y1 = -snake_block
        # elif x1 == (dis_width - snake_block) and x1_change == snake_block:
        #     x1_change = 0
        #     y1_change = snake_block
        # elif x1 == (dis_width - snake_block) and x1_change == 0 and y1_change == snake_block:
        #     x1_change = -snake_block
        #     y1_change = 0
        # elif x1 == 0 and x1_change == -snake_block:
        #     x1_change = 0
        #     y1_change = snake_block
        # elif x1 == 0 and x1_change == 0 and y1_change == snake_block:
        #     x1_change = snake_blockqqq
        #     y1_change = 0

        if x1 == food_x:
            x1_change = 0
        elif x1 > food_x:
            x1_change = -snake_block
            y1_change = 0
        elif x1 < food_x:
            x1_change = snake_block
            y1_change = 0

        if y1 == food_y:
            y1_change = 0
        elif y1 > food_y:
            x1_change = 0
            y1_change = -snake_block
        elif y1 < food_y:
            x1_change = 0
            y1_change = snake_block

        # region demo mode - end

        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        dis.blit(fruits.images[current_fruit], (food_x, food_y))
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # for x in snake_list[:-1]:
        #     if x == snake_head:
        #         game_over_sound.play()
        #         game_over = False

        draw_our_snake(snake_block, snake_list)
        your_score(length_of_snake - 1)

        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            print("Yummy!!")
            apple_sound.play()
            current_fruit = random.randrange(0, len(fruits.images))
            food_x = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
            food_y = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block
            length_of_snake += 1
            # snake_speed +=1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
