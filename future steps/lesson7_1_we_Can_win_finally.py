import pygame
import time
import random
from assets import fruits


dis_width = 800
dis_height = 600

pygame.init()
dis = pygame.display.set_mode(size = (dis_width, dis_height))
pygame.display.set_caption('Snake game for eKids')

initial_snake_speed = 10
snake_block = 20
clock = pygame.time.Clock()
level_speed_add = 3
fruits_per_level = 3
levels = 5
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
background_img = pygame.image.load("assets/img/sand1.jpg")
apple_sound = pygame.mixer.Sound('assets/sound/apple.wav')
explosion_sound = pygame.mixer.Sound('assets/sound/explosion.wav')
game_over_sound = pygame.mixer.Sound('assets/sound/gameover.wav')
level_up_sound = pygame.mixer.Sound('assets/sound/level_up.mp3')
snake_head_img = pygame.image.load('assets/img/head.png')
snake_body_img = pygame.image.load('assets/img/body.png')


def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [25,25])

def draw_our_snake(snake_block, snake_list):
    for cell in snake_list[0:-1]:
        dis.blit(snake_body_img, (cell[0], cell[1]))
    dis.blit(snake_head_img, (snake_list[-1][0], snake_list[-1][1]))

def message(msg, color, pos_x=dis_width/7, pos_y=dis_height / 3):
    rendered_message = font_style.render(msg, True, color)
    dis.blit(rendered_message, [pos_x, pos_y])

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
light_blue = (96, 148, 188)
red = (255, 0, 0)
orange = (255, 165, 48)
violet = (117, 48, 255)

def starting_screen():
    while True:
        for i in range(-10, 1):
            dis.fill(orange)
            message("Game will start in: " + str(i*(-1)) + " or press r to run the game", violet)
            message("Select speed on Snake: * 1 - slow mode * 2 - medium mode * 3 - fast mode", violet, pos_y=dis_height/2)
            pygame.display.update()
            time.sleep(1)
            if i == 0:
                gameLoop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        gameLoop()
                    elif event.key == pygame.K_1:
                        gameLoop(snake_speed=7)
                    elif event.key == pygame.K_2:
                        gameLoop(snake_speed=20)
                    elif event.key == pygame.K_3:
                        gameLoop(snake_speed=30)

def your_level(value):
    value = score_font.render("Ваш рівень: " + str(value), True, yellow)
    dis.blit(value, [25, 100])

def gameLoop(snake_speed=initial_snake_speed):  # creating a function
    game_over = False
    game_win = False
    game_close = False
    # snake_speed = initial_snake_speed
    fruit_eaten = False
    current_fruit = 0
    bad_fruit = -1
    relieve_ratio = 2

    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1
    level = 1
    foodx = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
    foody = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block

    bad_food_x = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
    bad_food_y = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block

    while not game_close:

        while game_over == True or game_win == True:

            if game_over:
                dis.fill(white)
                message("Ви програли! Q-Вихід або C-Грати знову", red, dis_width/7, dis_height/7)
            else:
                dis.fill(orange)
                message("You Win! Press C-Play Again or Q-Quit", black)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    exit()
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

        x1 = x1 + x1_change
        y1 = y1 + y1_change
        dis.blit(background_img, [0, 0])
        dis.blit(fruits.good[current_fruit], (foodx, foody))
        if bad_fruit > 0:
            dis.blit(fruits.bad[bad_fruit], (bad_food_x, bad_food_y))
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for cell in snake_list[:-1]:
            if cell == snake_head:
                game_over = True
                game_over_sound.play()

        draw_our_snake(snake_block, snake_list)
        your_score(length_of_snake - 1)
        your_level(level)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            print("Yummy!!")
            apple_sound.play()
            length_of_snake += 1
            fruit_eaten = True

        if x1 == bad_food_x and y1 == bad_food_y:
            print("Fooo!!")
            explosion_sound.play()
            length_of_snake -= 1
            snake_list.pop(0)
            fruit_eaten = True

        if fruit_eaten:
            fruit_eaten = False
            current_fruit = random.randrange(0, len(fruits.good))
            foodx = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
            foody = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block

            if length_of_snake == 0:
                game_over = True

            if length_of_snake % relieve_ratio == 0:
                bad_fruit = random.randrange(0, len(fruits.bad))
                bad_food_x = snake_list[0][0]
                bad_food_y = snake_list[0][1]
            elif length_of_snake % fruits_per_level == 0 and not game_over:
                level += 1
                if level == levels:  # якщо новий рівень рівний максимальному - перемогу
                    game_win = True
                else:
                    snake_speed += level_speed_add
                    dis.fill(light_blue)
                    message("Level passed!", violet)
                    pygame.display.update()
                    level_up_sound.play()
                    time.sleep(2)

        clock.tick(snake_speed)

    pygame.quit()
    quit()


starting_screen()
