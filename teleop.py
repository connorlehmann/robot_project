import math
import pygame
from environment import RobotEnv

env = RobotEnv()

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

wall_boxes = [
pygame.Rect(400, 290, 100, 10),   # top    
pygame.Rect(500, 300, 10, 100),   # right  
pygame.Rect(400, 400, 100, 10),   # bottom 
pygame.Rect(390, 300, 10, 100),   # left   
]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if pygame.key.get_pressed()[pygame.K_o]:
        action = 0
    elif pygame.key.get_pressed()[pygame.K_w]:
        action = 1
    elif pygame.key.get_pressed()[pygame.K_s]:
        action = 2
    elif pygame.key.get_pressed()[pygame.K_d]:
        action = 3
    elif pygame.key.get_pressed()[pygame.K_a]:
        action = 4
    else:
        action = 0

    obs, reward, terminated, truncated, info = env.step(action)
    if terminated == True or truncated == True:
        obs, info = env.reset()




    dt = clock.tick(60) / 1000
    screen.fill((0, 0, 0))
        
    for wall in wall_boxes:
        pygame.draw.rect(screen, (255, 0, 0), wall)

    pygame.draw.rect(screen, (255, 255, 0), (470, 370, 15, 15))

    cx = env.robot1.pos_x
    cy = env.robot1.pos_y
    radius = 10

    # Distance of eyes from center
    eye_distance = 6

    # Eye positions relative to heading
    left_eye_x = cx + math.cos(env.robot1.theta + math.pi / 4) * eye_distance
    left_eye_y = cy - math.sin(env.robot1.theta + math.pi / 4) * eye_distance

    right_eye_x = cx + math.cos(env.robot1.theta - math.pi / 4) * eye_distance
    right_eye_y = cy - math.sin(env.robot1.theta - math.pi / 4) * eye_distance

    pygame.draw.circle(
        screen,
        (0, 255, 0),
        (int(cx), int(cy)),
        radius
    )


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

    left_text = font.render(f"Left Speed: {env.robot1.left_speed}", True, (255, 255, 255))
    right_text = font.render(f"Right Speed: {env.robot1.right_speed}", True, (255, 255, 255))
    theta_text = font.render(f"Theta: {env.robot1.theta:.2f}", True, (255, 255, 255))



    closest_t = min(
        [d for d in [env.front_dist, env.left_dist, env.right_dist, env.back_dist] if d is not None],
        default=None,
    )

    if closest_t is not None:
        closest_wall_text = font.render(f"Closest Wall: {closest_t:.2f}", True, (255, 255, 255))
    else:
        closest_wall_text = font.render("No wall detected", True, (255, 255, 255))



    #Display values
    closest_t_right_text = font.render(f"Closest Right Wall: {env.right_dist:.2f}" if env.right_dist is not None else "No right wall detected", True, (255, 255, 255))
    closest_t_left_text = font.render(f"Closest Left Wall: {env.left_dist:.2f}" if env.left_dist is not None else "No left wall detected", True, (255, 255, 255))
    closest_t_front_text = font.render(f"Closest Front Wall: {env.front_dist:.2f}" if env.front_dist is not None else "No front wall detected", True, (255, 255, 255))
    closest_t_back_text = font.render(f"Closest Back Wall: {env.back_dist:.2f}" if env.back_dist is not None else "No back wall detected", True, (255, 255, 255))

    screen.blit(closest_t_right_text, (10, 170))
    screen.blit(closest_t_left_text, (10, 210))
    screen.blit(closest_t_front_text, (10, 250))
    screen.blit(closest_t_back_text, (10, 290))

    screen.blit(left_text, (10, 10))
    screen.blit(right_text, (10, 50))
    screen.blit(theta_text, (10, 90))
    screen.blit(closest_wall_text, (10, 130))


    pygame.display.update()




