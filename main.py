import math
import time

from mymathcalc import find_t, find_u, vector_subtract, cross_product


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
    #Q
    wall_start1 = (400, 300)
    wall_end1 = (500, 300)
    wall_start2 = (500, 300)
    wall_end2 = (500, 400)
    wall_start3 = (500, 400)
    wall_end3 = (400, 400)
    wall_start4 = (400, 400)
    wall_end4 = (400, 300)

    #S
    wall_direction1 = vector_subtract(wall_start1, wall_end1)
    wall_direction2 = vector_subtract(wall_start2, wall_end2)
    wall_direction3 = vector_subtract(wall_start3, wall_end3)
    wall_direction4 = vector_subtract(wall_start4, wall_end4)

    #P
    robot_position = (robot1.pos_x, robot1.pos_y)

    #R
    ray_direction = (math.cos(robot1.theta), -math.sin(robot1.theta))

    t1 = find_t(wall_start1, robot_position, wall_direction1, ray_direction)
    u1 = find_u(wall_start1, robot_position, wall_direction1, ray_direction)
    t2 = find_t(wall_start2, robot_position, wall_direction2, ray_direction)
    u2 = find_u(wall_start2, robot_position, wall_direction2, ray_direction)
    t3 = find_t(wall_start3, robot_position, wall_direction3, ray_direction)
    u3 = find_u(wall_start3, robot_position, wall_direction3, ray_direction)
    t4 = find_t(wall_start4, robot_position, wall_direction4, ray_direction)
    u4 = find_u(wall_start4, robot_position, wall_direction4, ray_direction)




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


    valid_t = [t for t in [t1, t2, t3, t4] if t >= 0]

    if valid_t:
        closest_wall_text = font.render(f"Closest Wall: {min(valid_t):.2f}", True, (255, 255, 255))
    else:
        closest_wall_text = font.render(f"Closest Wall: No intersection", True, (255, 255, 255))



    screen.blit(left_text, (10, 10))
    screen.blit(right_text, (10, 50))
    screen.blit(theta_text, (10, 90))
    screen.blit(closest_wall_text, (10, 130))

    pygame.display.update()