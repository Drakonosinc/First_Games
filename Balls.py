from pygame import *
class Ball:
    def __init__(self, x, y, width, height):
        self.rect = Rect(x, y, width, height)
        self.move_x = 0
        self.move_y = 0
        self.touch_ball:list=[True,True]
        
    def move_ball(self,):
        pass
    def check_collision(self, other_rect):
        return self.rect.colliderect(other_rect)
    def reset(self, x, y):
        self.rect.x, self.rect.y = x, y
    def check_collision(self, other_rect):
        return self.rect.colliderect(other_rect)