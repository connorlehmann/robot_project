import math
import time

from math import find_t, find_u, vector_subtract, cross_product


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


    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (400, 300, 100, 100))
    pygame.draw.rect(screen, (0, 0, 255), (475, 375, 10, 10))


    #Needed for LiDAR calculations
    wall_start1 = (400, 300) #Q
    wall_end1 = (500, 300)
    wall_direction1 = vector_subtract(wall_start1, wall_end1) #S
    robot_position = (robot1.pos_x, robot1.pos_y) #P
    ray_direction = (math.cos(robot1.theta), -math.sin(robot1.theta)) #R

    t = find_t(wall_start1, robot_position, wall_direction1, ray_direction)
    u = find_u(wall_start1, robot_position, wall_direction1, ray_direction)




    pygame.draw.line(surface=screen, color=(255, 255, 255), 
                     start_pos=(robot1.pos_x, robot1.pos_y), 
                     end_pos=(math.cos(robot1.theta) * 50 + robot1.pos_x, 
                            robot1.pos_y - math.sin(robot1.theta) * 50), 
                            width=2)


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

    left_text = font.render(f"Left Speed: {robot1.left_speed}", True, (255, 255, 255))
    right_text = font.render(f"Right Speed: {robot1.right_speed}", True, (255, 255, 255))
    theta_text = font.render(f"Theta: {robot1.theta:.2f}", True, (255, 255, 255))
    closest_wall_text = font.render(f"Closest Wall: {t:.2f}", True, (255, 255, 255))

    screen.blit(left_text, (10, 10))
    screen.blit(right_text, (10, 50))
    screen.blit(theta_text, (10, 90))

    pygame.display.update()