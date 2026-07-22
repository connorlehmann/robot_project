import math

class Robot:
    def __init__(self, name):
        self.name = name
        self.pos_x = 400
        self.pos_y = 300
        self.velo = 0
        self.theta = 0

    def speed_forward(self):
        self.velo = 5

    def speed_backward(self):
        self.velo = -5

    def turn_right(self):
        self.theta -= (math.pi / 2)
    
    def turn_left(self):
        self.theta += (math.pi / 2)

    def move_down(self):
        self.pos_y += 5
        return self.pos_y
    
    def boundaries_check(self):
        if self.pos_x < 400:
            self.pos_x = 400
        elif self.pos_x > 490:
            self.pos_x = 490
        if self.pos_y < 300:
            self.pos_y = 300
        elif self.pos_y > 390:
            self.pos_y = 390

    def pos_update(self):
        self.pos_x += self.velo * math.cos(self.theta)
        self.pos_y -= self.velo * math.sin(self.theta)