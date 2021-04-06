import pygame
import time
import random

dis_width = 1000
dis_height = 800
pygame.init()
dis = pygame.display.set_mode(size=(dis_width, dis_height))

pygame.display.set_caption('Eyes exercises for eKids')

radius = 40
delay = 1

for i in range(0, 100):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                exit()

    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    pygame.draw.circle(dis, color, center=[random.randint(0, dis_width-radius*2), random.randint(0, dis_height-radius*2)],
                           radius=radius)
    pygame.display.update()
    time.sleep(delay)

pygame.quit()
quit()
