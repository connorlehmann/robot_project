import time

import pygame
from robot import Robot

pygame.init()

screen = pygame.display.set_mode((800, 600))
robot1 = Robot("Robo1")

robot_square = pygame.draw.rect(screen, (0, 255, 0), (robot1.pos_x, robot1.pos_y, 10, 10))
pygame.display.update()

clock = pygame.time.Clock()

while True:
    dt = clock.tick(60) / 1000

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (400, 300, 100, 100))
    pygame.draw.rect(screen, (0, 0, 255), (475, 375, 10, 10))

    for event in pygame.event.get():

        if pygame.key.get_pressed()[pygame.K_UP]:
            robot1.speed_forward()
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            robot1.speed_backward()
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            robot1.turn_left()
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            robot1.turn_right()
        
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
    if  475 < robot1.pos_x < 485 and 375 < robot1.pos_y < 385:
        print("Robot has reached the target!")
        pygame.quit()
        exit()
        

    robot1.boundaries_check()
    robot1.pos_update(dt=dt)
    robot_square = pygame.draw.rect(screen, (0, 255, 0), (robot1.pos_x, robot1.pos_y, 10, 10))
    pygame.display.update()