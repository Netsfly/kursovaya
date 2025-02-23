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
        self.image = blank_image
        self.image = p.transform.scale(self.image,(self.width, self.heght))
        
blank_image = p.image.load('Blanc.png')
x_image = p.image.load('x.png')
y_image = p.image.load('o.png')
background_image = p.image.load('Background.png')