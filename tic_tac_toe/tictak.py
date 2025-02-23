import pygame as p

p.init()

class Square(p.sprite.Sprite):
    def __init__(self, x_id, y_id, number):
        super().__init__()
        self.width = 120
        self.heght = 120
        self.x = x_id * self.width
        self.y = y_id * self.heght
        self.content = ''
        self.number = number