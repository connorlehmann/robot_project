import math
import time

from mymathcalc import ray_segment_intersect, vector_subtract, cross_product


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
    pygame.Rect(500, 300, 10, 100),
    pygame.Rect(400, 400, 100, 10),
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

    #S  (segment direction MUST go start -> end for u to range over [0, 1])
    wall_direction1 = vector_subtract(wall_end1, wall_start1)
    wall_direction2 = vector_subtract(wall_end2, wall_start2)
    wall_direction3 = vector_subtract(wall_end3, wall_start3)
    wall_direction4 = vector_subtract(wall_end4, wall_start4)

    walls = [
        (wall_start1, wall_direction1),
        (wall_start2, wall_direction2),
        (wall_start3, wall_direction3),
        (wall_start4, wall_direction4),
    ]

    #P
    robot_position = (robot1.pos_x, robot1.pos_y)

    #R
    ray_direction_front = (math.cos(robot1.theta), -math.sin(robot1.theta))
    ray_direction_left = (math.cos(robot1.theta + math.pi/2), -math.sin(robot1.theta + math.pi/2))
    ray_direction_right = (math.cos(robot1.theta - math.pi/2), -math.sin(robot1.theta - math.pi/2))
    ray_direction_back = (math.cos(robot1.theta + math.pi), -math.sin(robot1.theta + math.pi))

    def closest_hit(ray_direction):
        """Cast ray_direction from the robot and return the distance to the
        nearest wall it actually hits, or None if it hits nothing."""
        hits = [
            ray_segment_intersect(robot_position, ray_direction, wall_q, wall_s)
            for wall_q, wall_s in walls
        ]
        valid_hits = [h for h in hits if h is not None]
        return min(valid_hits) if valid_hits else None

    front_dist = closest_hit(ray_direction_front)
    left_dist = closest_hit(ray_direction_left)
    right_dist = closest_hit(ray_direction_right)
    back_dist = closest_hit(ray_direction_back)




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

    pygame.draw.rect(screen, (255, 255, 0), (475, 375, 10, 10))
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

    closest_front = front_dist
    closest_left = left_dist
    closest_right = right_dist
    closest_back = back_dist

    closest_t = min(
        [d for d in [closest_front, closest_left, closest_right, closest_back] if d is not None],
        default=None,
    )

    if closest_t is not None:
        closest_wall_text = font.render(f"Closest Wall: {closest_t:.2f}", True, (255, 255, 255))
    else:
        closest_wall_text = font.render("No wall detected", True, (255, 255, 255))



    #Display values
    closest_t_right_text = font.render(f"Closest Right Wall: {closest_right:.2f}" if closest_right is not None else "No right wall detected", True, (255, 255, 255))
    closest_t_left_text = font.render(f"Closest Left Wall: {closest_left:.2f}" if closest_left is not None else "No left wall detected", True, (255, 255, 255))
    closest_t_front_text = font.render(f"Closest Front Wall: {closest_front:.2f}" if closest_front is not None else "No front wall detected", True, (255, 255, 255))
    closest_t_back_text = font.render(f"Closest Back Wall: {closest_back:.2f}" if closest_back is not None else "No back wall detected", True, (255, 255, 255))

    screen.blit(closest_t_right_text, (10, 170))
    screen.blit(closest_t_left_text, (10, 210))
    screen.blit(closest_t_front_text, (10, 250))
    screen.blit(closest_t_back_text, (10, 290))

    screen.blit(left_text, (10, 10))
    screen.blit(right_text, (10, 50))
    screen.blit(theta_text, (10, 90))
    screen.blit(closest_wall_text, (10, 130))

    robot1.speed_check()
    robot1.total_velocity()

    
    robot1.boundaries_check(right_dist=closest_right, left_dist=closest_left, top_dist=closest_front, bottom_dist=closest_back)

    next_distance = robot1.predict_dist_moved(dt=dt)
    
    if robot1.velo > 0:
        # moving forward
        if closest_front is None or closest_front > next_distance:
            robot1.pos_update(dt)

    elif robot1.velo < 0:
        # moving backward
        if closest_back is None or closest_back > next_distance:
            robot1.pos_update(dt)
    

    pygame.display.update()