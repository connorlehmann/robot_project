import math
import pygame
from stable_baselines3 import PPO
from environment import RobotEnv

env = RobotEnv()
model = PPO.load("robot_policy")

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

wall_boxes = [
    pygame.Rect(400, 290, 100, 10),
    pygame.Rect(500, 300, 10, 100),
    pygame.Rect(400, 400, 100, 10),
    pygame.Rect(390, 300, 10, 100),
]

obs, info = env.reset()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    action, _states = model.predict(obs, deterministic=True)
    obs, reward, terminated, truncated, info = env.step(int(action))

    if terminated or truncated:
        obs, info = env.reset()

    screen.fill((0, 0, 0))

    for wall in wall_boxes:
        pygame.draw.rect(screen, (255, 0, 0), wall)
    pygame.draw.rect(screen, (255, 255, 0), (470, 370, 15, 15))

    cx = env.robot1.pos_x
    cy = env.robot1.pos_y
    radius = 10
    pygame.draw.circle(screen, (0, 255, 0), (int(cx), int(cy)), radius)

    theta_text = font.render(f"Theta: {env.robot1.theta}", True, (255, 255, 255))
    left_text = font.render(f"Left Speed: {env.robot1.left_speed}", True, (255, 255, 255))
    right_text = font.render(f"Right Speed: {env.robot1.right_speed}", True, (255, 255, 255))
    reward_text = font.render(f"Reward: {reward:.2f}", True, (255, 255, 255))
    screen.blit(left_text, (10, 10))
    screen.blit(right_text, (10, 50))
    screen.blit(reward_text, (10, 90))

    pygame.display.update()
    clock.tick(60)