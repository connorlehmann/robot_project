import math
import time
from types import NoneType

from mymathcalc import find_t, find_u, vector_subtract, cross_product


import pygame
from robot import Robot

pygame.init()


screen = pygame.display.set_mode((800, 600))
robot1 = Robot("Robo1")


pygame.display.update()

clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

while True:
    dt = clock.tick(60) / 1000


    screen.fill((0, 0, 0))

    wall_boxes = [
    pygame.Rect(400, 300, 100, 10),
    pygame.Rect(490, 300, 10, 100),
    pygame.Rect(400, 390, 100, 10),
    pygame.Rect(400, 300, 10, 100)
    ]

    for wall in wall_boxes:
        pygame.draw.rect(screen, (255, 0, 0), wall)



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
    ray_direction_front = (math.cos(robot1.theta), -math.sin(robot1.theta))
    ray_direction_left = (math.cos(robot1.theta + math.pi/2), -math.sin(robot1.theta + math.pi/2))
    ray_direction_right = (math.cos(robot1.theta - math.pi/2), -math.sin(robot1.theta - math.pi/2))
    ray_direction_back = (math.cos(robot1.theta + math.pi), -math.sin(robot1.theta + math.pi))

    t1_front = find_t(wall_start1, robot_position, wall_direction1, ray_direction_front)
    u1_front = find_u(wall_start1, robot_position, wall_direction1, ray_direction_front)
    t2_front = find_t(wall_start2, robot_position, wall_direction2, ray_direction_front)
    u2_front = find_u(wall_start2, robot_position, wall_direction2, ray_direction_front)
    t3_front = find_t(wall_start3, robot_position, wall_direction3, ray_direction_front)
    u3_front = find_u(wall_start3, robot_position, wall_direction3, ray_direction_front)
    t4_front = find_t(wall_start4, robot_position, wall_direction4, ray_direction_front)
    u4_front = find_u(wall_start4, robot_position, wall_direction4, ray_direction_front)

    t1_left = find_t(wall_start1, robot_position, wall_direction1, ray_direction_left)
    u1_left = find_u(wall_start1, robot_position, wall_direction1, ray_direction_left)
    t2_left = find_t(wall_start2, robot_position, wall_direction2, ray_direction_left)
    u2_left = find_u(wall_start2, robot_position, wall_direction2, ray_direction_left)
    t3_left = find_t(wall_start3, robot_position, wall_direction3, ray_direction_left)
    u3_left = find_u(wall_start3, robot_position, wall_direction3, ray_direction_left)
    t4_left = find_t(wall_start4, robot_position, wall_direction4, ray_direction_left)
    u4_left = find_u(wall_start4, robot_position, wall_direction4, ray_direction_left) 

    t1_right = find_t(wall_start1, robot_position, wall_direction1, ray_direction_right)
    u1_right = find_u(wall_start1, robot_position, wall_direction1, ray_direction_right)
    t2_right = find_t(wall_start2, robot_position, wall_direction2, ray_direction_right)
    u2_right = find_u(wall_start2, robot_position, wall_direction2, ray_direction_right)
    t3_right = find_t(wall_start3, robot_position, wall_direction3, ray_direction_right)
    u3_right = find_u(wall_start3, robot_position, wall_direction3, ray_direction_right)
    t4_right = find_t(wall_start4, robot_position, wall_direction4, ray_direction_right)
    u4_right = find_u(wall_start4, robot_position, wall_direction4, ray_direction_right)

    t1_back = find_t(wall_start1, robot_position, wall_direction1, ray_direction_back)
    u1_back = find_u(wall_start1, robot_position, wall_direction1, ray_direction_back)
    t2_back = find_t(wall_start2, robot_position, wall_direction2, ray_direction_back)
    u2_back = find_u(wall_start2, robot_position, wall_direction2, ray_direction_back)
    t3_back = find_t(wall_start3, robot_position, wall_direction3, ray_direction_back)
    u3_back = find_u(wall_start3, robot_position, wall_direction3, ray_direction_back)
    t4_back = find_t(wall_start4, robot_position, wall_direction4, ray_direction_back)
    u4_back = find_u(wall_start4, robot_position, wall_direction4, ray_direction_back)




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
        if pygame.key.get_pressed()[pygame.K_o]:
            robot1.left_speed = 0
            robot1.right_speed = 0

    if  475 < robot1.pos_x < 485 and 375 < robot1.pos_y < 385:
        print("Robot has reached the target!")
        pygame.quit()
        exit()
        



    # Robot body
    cx = robot1.pos_x
    cy = robot1.pos_y
    radius = 10

    pygame.draw.circle(
        screen,
        (0, 255, 0),
        (int(cx), int(cy)),
        radius
    )

    # Distance of eyes from center
    eye_distance = 6

    # Eye positions relative to heading
    left_eye_x = cx + math.cos(robot1.theta + math.pi / 4) * eye_distance
    left_eye_y = cy - math.sin(robot1.theta + math.pi / 4) * eye_distance

    right_eye_x = cx + math.cos(robot1.theta - math.pi / 4) * eye_distance
    right_eye_y = cy - math.sin(robot1.theta - math.pi / 4) * eye_distance

    # Draw eyes
    pygame.draw.circle(
        screen,
        (0, 0, 0),
        (int(left_eye_x), int(left_eye_y)),
        2
    )

    pygame.draw.circle(
        screen,
        (0, 0, 0),
        (int(right_eye_x), int(right_eye_y)),
        2
    )




    left_text = font.render(f"Left Speed: {robot1.left_speed}", True, (255, 255, 255))
    right_text = font.render(f"Right Speed: {robot1.right_speed}", True, (255, 255, 255))
    theta_text = font.render(f"Theta: {robot1.theta:.2f}", True, (255, 255, 255))


    valid_t_front = [t for t in [t1_front, t2_front, t3_front, t4_front] if t >= 0]
    valid_t_left = [t for t in [t1_left, t2_left, t3_left, t4_left] if t >= 0]
    valid_t_right = [t for t in [t1_right, t2_right, t3_right, t4_right] if t >= 0]
    valid_t_back = [t for t in [t1_back, t2_back, t3_back, t4_back] if t >= 0]

    closest_t_front = min(valid_t_front) if valid_t_front else None
    closest_t_left = min(valid_t_left) if valid_t_left else None
    closest_t_right = min(valid_t_right) if valid_t_right else None
    closest_t_back = min(valid_t_back) if valid_t_back else None

    closest_t = min(closest_t_front, closest_t_left, closest_t_right, closest_t_back) if any([closest_t_front, closest_t_left, closest_t_right, closest_t_back]) else None

    if closest_t is not None:
        closest_wall_text = font.render(f"Closest Wall: {closest_t:.2f}", True, (255, 255, 255))
    else:
        closest_wall_text = font.render("No wall detected", True, (255, 255, 255))

    closest_t_right_text = font.render(f"Closest Right Wall: {closest_t_right:.2f}" if closest_t_right is not None else "No right wall detected", True, (255, 255, 255))
    closest_t_left_text = font.render(f"Closest Left Wall: {closest_t_left:.2f}" if closest_t_left is not None else "No left wall detected", True, (255, 255, 255))
    closest_t_front_text = font.render(f"Closest Front Wall: {closest_t_front:.2f}" if closest_t_front is not None else "No front wall detected", True, (255, 255, 255))
    closest_t_back_text = font.render(f"Closest Back Wall: {closest_t_back:.2f}" if closest_t_back is not None else "No back wall detected", True, (255, 255, 255))

    closest_u_right_text = font.render(f"Closest Right Wall U: {u3_right:.2f}" if u3_right is not None else "No right wall detected", True, (255, 255, 255))
    closest_u_left_text = font.render(f"Closest Left Wall U: {u3_left:.2f}" if u3_left is not None else "No left wall detected", True, (255, 255, 255))
    closest_u_front_text = font.render(f"Closest Front Wall U: {u3_front:.2f}" if u3_front is not None else "No front wall detected", True, (255, 255, 255))
    closest_u_back_text = font.render(f"Closest Back Wall U: {u3_back:.2f}" if u3_back is not None else "No back wall detected", True, (255, 255, 255))




    screen.blit(closest_t_right_text, (10, 170))
    screen.blit(closest_t_left_text, (10, 210))
    screen.blit(closest_t_front_text, (10, 250))
    screen.blit(closest_t_back_text, (10, 290))
    screen.blit(closest_u_right_text, (10, 330))
    screen.blit(closest_u_left_text, (10, 370))
    screen.blit(closest_u_front_text, (10, 410))
    screen.blit(closest_u_back_text, (10, 450))

    screen.blit(left_text, (10, 10))
    screen.blit(right_text, (10, 50))
    screen.blit(theta_text, (10, 90))
    screen.blit(closest_wall_text, (10, 130))

    robot1.speed_check()
    robot1.total_velocity()

    
    robot1.boundaries_check(right_dist=closest_t_right, left_dist=closest_t_left, top_dist=closest_t_front, bottom_dist=closest_t_back)

    next_distance = robot1.predict_dist_moved(dt=dt)
    if closest_t > next_distance:
        robot1.pos_update(dt=dt)
        
    pygame.display.update()