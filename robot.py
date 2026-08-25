import math
wheel_base = 20
class Robot:
    def __init__(self, name):
        self.name = name
        self.pos_x = 445
        self.pos_y = 350
        self.velo = 0
        self.theta = math.pi
        self.angular_velo = 0
        self.left_speed = 0
        self.right_speed = 0
        self.next_distance = 0

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
    
    def boundaries_check(self, right_dist, left_dist, top_dist, bottom_dist):
        if right_dist < 10:
            print("Warning: Robot's right side is too close to the boundary!")
        
        elif left_dist < 10:
            print("Warning: Robot's left side is too close to the boundary!")
        
        elif top_dist < 10:
            print("Warning: Robot's top side is too close to the boundary!")
        
        elif bottom_dist < 10:
            print("Warning: Robot's bottom side is too close to the boundary!")


        if right_dist < 1:
            self.right_speed = 0
            self.left_speed = 0

        if left_dist < 1:
            self.right_speed = 0
            self.left_speed = 0

        if top_dist < 1:
            self.right_speed = 0
            self.left_speed = 0

        if bottom_dist < 1:
            self.right_speed = 0
            self.left_speed = 0


    def pos_update(self, dt):
        self.theta += self.angular_velo * dt
        
        self.pos_x += self.velo * math.cos(self.theta) * dt
        self.pos_y -= self.velo * math.sin(self.theta) * dt

    def predict_dist_moved(self, dt):
        self.next_distance = self.velo * dt

