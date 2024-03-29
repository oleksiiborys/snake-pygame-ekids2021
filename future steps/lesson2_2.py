import pygame
import time

dis_width = 800
dis_height = 600

pygame.init()
dis = pygame.display.set_mode(size = (dis_width, dis_height))

pygame.display.set_caption('Snake game for eKids')

x1 = dis_width / 2
y1 = dis_height / 2

snake_speed = 30

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 50)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 2, dis_height / 2])

black = (0, 0, 0)
blue = (0, 0, 255)
light_blue = (96, 148, 188)
red = (255, 0, 0)

game_over = False
while not game_over:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -10
                x1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = 10
                x1_change = 0

    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        game_over = True

    x1 = x1 + x1_change
    y1 = y1 + y1_change
    dis.fill(light_blue)
    pygame.draw.rect(dis, black, [x1, y1, 10, 10])
    pygame.display.update()
    clock.tick(snake_speed)

message("You lost", red)
pygame.display.update()
time.sleep(2)

pygame.quit()
quit()