import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

robot_x = 0
robot_y = 0

while True:
    
    for event in pygame.event.get():
        if pygame.key.get_pressed()[pygame.K_UP]:
            robot_y += 5
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            robot_y -= 5
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            robot_x -= 5
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            robot_x += 5
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()