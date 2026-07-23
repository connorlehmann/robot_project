import time

import pygame
from robot import Robot

pygame.init()


screen = pygame.display.set_mode((800, 600))
robot1 = Robot("Robo1")

robot_square = pygame.draw.rect(screen, (0, 255, 0), (robot1.pos_x, robot1.pos_y, 10, 10))
pygame.display.update()

clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

while True:
    dt = clock.tick(60) / 1000
    
    left_text = font.render(f"Left Speed: {robot1.left_speed}", True, (255, 255, 255))
    right_text = font.render(f"Right Speed: {robot1.right_speed}", True, (255, 255, 255))


    screen.blit(left_text, (10, 10))
    screen.blit(right_text, (10, 50))


    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (400, 300, 100, 100))
    pygame.draw.rect(screen, (0, 0, 255), (475, 375, 10, 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        if pygame.key.get_pressed()[pygame.K_q]:
            robot1.left_up()
        if pygame.key.get_pressed()[pygame.K_a]:
            robot1.left_down()
        if pygame.key.get_pressed()[pygame.K_e]:
            robot1.right_up()
        if pygame.key.get_pressed()[pygame.K_d]:
            robot1.right_down()

    if  475 < robot1.pos_x < 485 and 375 < robot1.pos_y < 385:
        print("Robot has reached the target!")
        pygame.quit()
        exit()
        
    robot1.speed_check()
    robot1.total_velocity()
    robot1.boundaries_check()
    robot1.pos_update(dt=dt)
    robot_square = pygame.draw.rect(screen, (0, 255, 0), (robot1.pos_x, robot1.pos_y, 10, 10))
    pygame.display.update()