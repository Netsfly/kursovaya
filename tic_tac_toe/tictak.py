import pygame as p

p.init()

class Square(p.sprite.Sprite):
    def __init__(self, x_id, y_id, number):
        super().__init__()
        self.width = 120
        self.height = 120
        self.x = x_id * self.width
        self.y = y_id * self.height
        self.content = ''
        self.number = number
        self.image = blank_image
        self.image = p.transform.scale(self.image,(self.width, self.height))
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.center = (self.x, self.y)
        
    def clicked(self, x_val, y_val):
        global turn
        if self.content == '  ':
            if self.rect.collidepoint(x_val, y_val):
                self.content = turn
                board[self.number] = turn
                
                if turn == 'x':
                    self.image = x_image
                    self.image = p.transform.scale(self.image, (self.width, self.height))
                    turn = 'o'
    
        
def Update():
    win.blit(background, (0, 0))
    square_group.draw(win)
    square_group.update()
    p.display.update()
    
WIDTH = 500
HEIGHT = 500

win = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption('Tic Tac Toe')
clock = p.time.Clock()

blank_image = p.image.load(r"d:\tic tac\tic_tac_toe\Blank.png")
x_image = p.image.load(r"d:\tic tac\tic_tac_toe\x.png")
o_image = p.image.load(r"d:\tic tac\tic_tac_toe\o.png")
background_image = p.image.load(r"d:\tic tac\tic_tac_toe\Background.png")
background = p.transform.scale(background_image, (WIDTH, HEIGHT)) 

square_group = p.sprite.Group()
squares = []
board = [' ' for i in range(10)]


num = 1
for y in range(1 ,4):
    for x in range(1, 4):
        sq = Square(x, y, num)
        square_group.add(sq)
        squares.append(sq)
        
        num += 1


turn = 'x'
run = True
while run:
    clock.tick(60)
    for event in p.event.get():
        if event.type == p.QUIT:
            run = False
    
    Update()