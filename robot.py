import math
wheel_base = 20
class Robot:
    def __init__(self, name):
        self.name = name
        self.pos_x = 400
        self.pos_y = 300
        self.velo = 0
        self.theta = 0
        self.angular_velo = 0
        self.left_speed = 0
        self.right_speed = 0

    def left_up(self):
        self.left_speed += 5
    
    def left_down(self):
        self.left_speed -= 5
    
    def right_up(self):
        self.right_speed += 5
    
    def right_down(self):
        self.right_speed -= 5

    def speed_check(self):
        if self.left_speed > 15:
            self.left_speed = 15
        elif self.left_speed < -15:
            self.left_speed = -15
        if self.right_speed > 15:
            self.right_speed = 15
        elif self.right_speed < -15:
            self.right_speed = -15
    
    def total_velocity(self):
        self.velo = (self.left_speed + self.right_speed) / 2
        self.angular_velo = (self.right_speed - self.left_speed) / wheel_base 
    
    def boundaries_check(self):
        if self.pos_x < 400:
            self.pos_x = 400
        elif self.pos_x > 490:
            self.pos_x = 490
        if self.pos_y < 300:
            self.pos_y = 300
        elif self.pos_y > 390:
            self.pos_y = 390

    def pos_update(self, dt):
        self.theta += self.angular_velo * dt
        
        self.pos_x += self.velo * math.cos(self.theta) * dt
        self.pos_y -= self.velo * math.sin(self.theta) * dt