class Robot:
    def __init__(self, name):
        self.name = name
        self.pos_x = 400
        self.pos_y = 300

    def move_right(self):
        self.pos_x += 5
        return self.pos_x
    
    def move_left(self):
        self.pos_x -= 5
        return self.pos_x
    
    def move_up(self):
        self.pos_y -= 5
        return self.pos_y
    
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