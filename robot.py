robot_x = 400
robot_y = 300

class Robot:
    def __init__(self, name):
        self.name = name
        self.robot_x = robot_x
        self.robot_y = robot_y

    def move_right(self):
        self.robot_x += 5
        return self.robot_x
    
    def move_left(self):
        self.robot_x -= 5
        return self.robot_x
    
    def move_up(self):
        self.robot_y -= 5
        return self.robot_y
    
    def move_down(self):
        self.robot_y += 5
        return self.robot_y