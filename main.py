import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

robot_x = 400
robot_y = 300
robot = pygame.draw.rect(screen, (0, 255, 0), (robot_x, robot_y, 10, 10))
pygame.display.update()

while True:
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (400, 300, 100, 100))
    pygame.draw.rect(screen, (0, 0, 255), (475, 375, 10, 10))


    for event in pygame.event.get():

        if pygame.key.get_pressed()[pygame.K_UP]:
            robot_y -= 5
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            robot_y += 5
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            robot_x -= 5
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            robot_x += 5
        
        if robot_x < 400:
            robot_x = 400
        elif robot_x > 490:
            robot_x = 490
        if robot_y < 300:
            robot_y = 300
        elif robot_y > 390:
            robot_y = 390
            
        robot = pygame.draw.rect(screen, (0, 255, 0), (robot_x, robot_y, 10, 10))
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if robot_x == 475 and robot_y == 375:
            print("Robot has reached the target!")
            pygame.quit()
            exit()
        
        pygame.display.update()