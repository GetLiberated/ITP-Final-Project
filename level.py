import pygame as pg
from settings import *
vec = pg.math.Vector2

class Level(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.screen = self.game.screen
        self.image = pg.image.load('images/bg.png').convert()
        self.rect = self.image.get_rect()
        self.image = pg.transform.scale(self.image, (int(self.rect.width * 3.214), int(self.rect.height * 3.214)))

class Brick(pg.sprite.Sprite):
    def __init__(self, game, name, x, y):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.screen = self.game.screen
        self.name = name
        if self.name == 1:
            self.image = pg.image.load('images/brick.png').convert_alpha()
            self.rect = self.image.get_rect()
            self.image = pg.transform.scale(self.image, (int(self.rect.width * 3.214), int(self.rect.height * 3.214)))
        if self.name == 2:
            self.image = pg.image.load('images/tile1.png').convert_alpha()
            self.rect = self.image.get_rect()
            self.image = pg.transform.scale(self.image, (int(self.rect.width * 3.214), int(self.rect.height * 3.214)))
        if self.name == 3:
            self.image = pg.image.load('images/brick_fall.png').convert_alpha()
            # self.image.fill((255,255,255))
            self.rect = self.image.get_rect()
            self.image = pg.transform.scale(self.image, (int(self.rect.width * 3.214), int(self.rect.height * 3.214)))
        if self.name == 4:
            self.image = pg.image.load('images/brick_fall.png').convert_alpha()
            # self.image.fill((255,0,0))
            self.rect = self.image.get_rect()
            self.image = pg.transform.scale(self.image, (int(self.rect.width * 3.214), int(self.rect.height * 3.214)))
            self.vel = vec(0,0)
            self.pos = vec(x, y)
        if self.name == 5:
            self.image = pg.Surface((51,51), pg.SRCALPHA, 32)
            # self.image.fill((255,255,255))
            # self.image = pg.image.load('images/tile.png').convert_alpha()
            # self.rect = self.image.get_rect()
            # self.image = pg.transform.scale(self.image, (int(self.rect.width * 3.214), int(self.rect.height * 3.214)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.hit = False

    def update(self):
        if self.hit:
            self.image = pg.image.load('images/tile4.png').convert_alpha()
            self.rect2 = self.image.get_rect()
            self.image = pg.transform.scale(self.image, (int(self.rect2.width * 3.214), int(self.rect2.height * 3.214)))
        if self.name == 4:
            self.pos += self.vel
            self.rect.center = self.pos
            self.obstacle = False
            self.falling_obstacle = True

class Annoying(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.screen = self.game.screen
        self.image = pg.Surface((51,51), pg.SRCALPHA, 32)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.hit = False

    def update(self):
        if self.hit:
            self.image = pg.image.load('images/tile4.png').convert_alpha()
            self.rect2 = self.image.get_rect()
            self.image = pg.transform.scale(self.image, (int(self.rect2.width * 3.214), int(self.rect2.height * 3.214)))

class Pipe(pg.sprite.Sprite):
    def __init__(self, height, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((102,height), pg.SRCALPHA, 32)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

class Floor(pg.sprite.Sprite):
    def __init__(self, game, name, x, y):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.screen = self.game.screen
        self.name = name
        if self.name == 1:
            self.image = pg.image.load('images/f1.png').convert()
            # self.image.fill((255,255,0))
            self.rect = self.image.get_rect()
            self.image = pg.transform.scale(self.image, (int(self.rect.width * 3.214), int(self.rect.height * 3.214)))
            self.rect = self.image.get_rect()
        if self.name == 2:
            self.image = pg.image.load('images/f2.png').convert()
            # self.image.fill((255,0,255))
            self.rect = self.image.get_rect()
            self.image = pg.transform.scale(self.image, (int(self.rect.width * 3.214), int(self.rect.height * 3.214)))
            self.rect = self.image.get_rect()
        if self.name == 3:
            self.image = pg.image.load('images/f3.png').convert()
            # self.image.fill((0,255,255))
            self.rect = self.image.get_rect()
            self.image = pg.transform.scale(self.image, (int(self.rect.width * 3.214), int(self.rect.height * 3.214)))
            self.rect = self.image.get_rect()
        if self.name == 4:
            self.image = pg.image.load('images/f4.png').convert()
            # self.image.fill((0,0,255))
            self.rect = self.image.get_rect()
            self.image = pg.transform.scale(self.image, (int(self.rect.width * 3.214), int(self.rect.height * 3.214)))
            self.rect = self.image.get_rect()
        if self.name == 5:
            self.image = pg.image.load('images/f5.png').convert()
            # self.image.fill((255,0,0))
            self.rect = self.image.get_rect()
            self.image = pg.transform.scale(self.image, (int(self.rect.width * 3.214), int(self.rect.height * 3.214)))
            self.rect = self.image.get_rect()
        if self.name == 6:
            self.image = pg.image.load('images/f6.png').convert()
            # self.image.fill((255,255,255))
            self.rect = self.image.get_rect()
            self.image = pg.transform.scale(self.image, (int(self.rect.width * 3.214), int(self.rect.height * 3.214)))
            self.rect = self.image.get_rect()
        if self.name == 7:
            self.image = pg.image.load('images/f7.png').convert()
            # self.image.fill((255,255,255))
            self.rect = self.image.get_rect()
            self.image = pg.transform.scale(self.image, (int(self.rect.width * 3.214), int(self.rect.height * 3.214)))
            self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Flag(pg.sprite.Sprite):
    def __init__(self, game, num, x, y):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.screen = self.game.screen
        if num == 1:
            self.image = pg.image.load('images/flag.png').convert_alpha()
        if num == 2:
            self.image = pg.image.load('images/cflag.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.image = pg.transform.scale(self.image, (int(self.rect.width * 3.214), int(self.rect.height * 3.214)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

class InvisibleNightmare(pg.sprite.Sprite):
    def __init__(self, x, width):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((width,800), pg.SRCALPHA, 32)
        # self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 0

class Coin(pg.sprite.Sprite):
    def __init__(self, game, name, x, y):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.screen = self.game.screen
        if name == 1:
            self.image = pg.image.load('images/coin1.png').convert_alpha()
            self.rect = self.image.get_rect()
            self.image = pg.transform.scale(self.image, (int(self.rect.width * 1.607), int(self.rect.height * 2.7335)))  # 14x16
            self.vel = vec(0,-5)
            self.pos = vec(x, y)
        self.rect.center = (x, y)
        self.num = 0

    def update(self, *args):
        self.pos += self.vel
        self.rect.center = self.pos
        if self.num > 1:
            self.kill()
            self.num = 0
        self.num += 0.08

class Mushroom(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.screen = self.game.screen
        self.image = pg.image.load('images/mushroom.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.image = pg.transform.scale(self.image, (int(self.rect.width * 3.214), int(self.rect.height * 3.214)))
        self.rect = self.image.get_rect()
        self.vel = vec(0,0)
        self.pos = vec(x,y)
        self.star = False

    def update(self, *args):
        self.vel.y = 10
        self.pos += self.vel
        self.rect.midbottom = self.pos

class Star(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.screen = self.game.screen
        self.image = pg.image.load('images/star.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.image = pg.transform.scale(self.image, (int(self.rect.width * 3.214), int(self.rect.height * 3.214)))
        self.rect = self.image.get_rect()
        self.vel = vec(0,0)
        self.pos = vec(x,y)
        self.star = True

    def update(self, *args):
        self.vel.y = 10
        self.pos += self.vel
        self.rect.midbottom = self.pos

