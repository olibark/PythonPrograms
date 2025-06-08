import  pygame as pg

class Enemy(pg.sprite.Sprite):
    def __init__(self, pos, image):
        pg.sprite.Sprite.__init__(self)
        self.image = image 
        self.react = self.image.get_rect()
        self.rect.center = pos 

