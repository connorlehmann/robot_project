import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

robot_x = 400
robot_y = 300
robot = pygame.draw.rect(screen, (0, 255, 0), (robot_x, robot_y, 10, 10))
pygame.draw.rect(screen, (255, 0, 0), (400, 300, 50, 50))
pygame.display.update()

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
            
            robot = pygame.draw.rect(screen, (0, 255, 0), (robot_x, robot_y, 10, 10))
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        pygame.display.update()