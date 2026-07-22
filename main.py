import pygame
from robot import Robot, pos_x, pos_y

pygame.init()

screen = pygame.display.set_mode((800, 600))
robot1 = Robot("Robo1")

robot_square = pygame.draw.rect(screen, (0, 255, 0), (robot1.pos_x, robot1.pos_y, 10, 10))
pygame.display.update()


while True:
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (400, 300, 100, 100))
    pygame.draw.rect(screen, (0, 0, 255), (475, 375, 10, 10))


    for event in pygame.event.get():

        if pygame.key.get_pressed()[pygame.K_UP]:
            robot1.move_up()
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            robot1.move_down()
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            robot1.move_left()
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            robot1.move_right()
        
        if robot1.pos_x < 400:
            robot1.pos_x = 400
        elif robot1.pos_x > 490:
            robot1.pos_x = 490
        if robot1.pos_y < 300:
            robot1.pos_y = 300
        elif robot1.pos_y > 390:
            robot1.pos_y = 390
            
        robot = pygame.draw.rect(screen, (0, 255, 0), (robot1.pos_x, robot1.pos_y, 10, 10))
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if robot1.pos_x == 475 and robot1.pos_y == 375:
            print("Robot has reached the target!")
            pygame.quit()
            exit()
        
        pygame.display.update()