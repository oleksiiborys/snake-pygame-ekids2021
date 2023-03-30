import pygame
import time
import random

dis_width = 1000
dis_height = 800
pygame.init()
dis = pygame.display.set_mode(size = (dis_width, dis_height))

pygame.display.set_caption('Eyes exercises for eKids')

radius = 40
delay = 3
center_positions = [(50, 70), (720, 490), (170, 260), (340, 200), (110, 700), (690, 300),
                    (random.randint(radius, dis_width-radius), random.randint(radius, dis_height-radius)),
                    (random.randint(radius, dis_width-radius), random.randint(radius, dis_height-radius)),
                    (random.randint(radius, dis_width-radius), random.randint(radius, dis_height-radius))]

for x, y in center_positions:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                exit()

    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    pygame.draw.circle(dis, color, center=[x, y], radius=radius)
    pygame.display.update()
    time.sleep(delay)

pygame.quit()
quit()
