import pygame
import time
import random


dis_width = 800
dis_height = 600

pygame.init()
dis = pygame.display.set_mode(size = (dis_width, dis_height))

pygame.display.set_caption('Snake game for eKids')

snake_speed = 10
snake_block = 25
clock = pygame.time.Clock()
font_style = pygame.font.SysFont(None, 50)

def draw_our_snake(snake_block, snake_list):
    for indx, cell in enumerate(snake_list):
        pygame.draw.rect(dis, black, [cell[0], cell[1], snake_block, snake_block ])
        pygame.draw.circle(dis, red, [cell[0]+snake_block/2, cell[1] + snake_block/2], snake_block/2-(len(snake_list) - indx)*0.2)

def message(msg, color, pos_x, pos_y):
    rendered_message = font_style.render(msg, True, color)
    dis.blit(rendered_message, [pos_x, pos_y])

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

    snake_list = []
    length_of_snake = 1
    food_x = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
    food_y = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block

    while not game_close:

        while game_over == True:
            dis.fill(white)
            message("Ви програли! Q-Вихід або C-Грати знову", red, dis_width/7, dis_height/7)
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
                print(event.key)
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
                elif event.key == pygame.K_KP7:
                    x1_change = -snake_block
                    y1_change = -snake_block
                elif event.key == pygame.K_KP1:
                    x1_change = -snake_block
                    y1_change = snake_block
                elif event.key == pygame.K_KP9:
                    x1_change = snake_block
                    y1_change = -snake_block
                elif event.key == pygame.K_KP3:
                    x1_change = snake_block
                    y1_change = snake_block

        # if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        #     game_close = True

        if x1 >= dis_width:
            x1 = 0
        if x1 < 0:
            x1 = dis_width
        if y1 >= dis_height:
            y1 = 0
        if y1 < 0:
            y1 = dis_height

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

        x1 = x1 + x1_change
        y1 = y1 + y1_change
        dis.fill(light_blue)
        pygame.draw.rect(dis, blue, [food_x, food_y, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # for cell in snake_list[:-1]:
        #     if cell == snake_head:
        #         game_over = True

        draw_our_snake(snake_block, snake_list)

        message("Your score : " + length_of_snake.__str__(), white, 20, 20)
        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            print("Yummy!!")
            food_x = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
            food_y = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
