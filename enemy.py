import pygame as pg
from settings import *
vec = pg.math.Vector2

class Goomba(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.screen = self.game.screen
        self.images()
        self.image = self.walk[0]
        self.rect = self.image.get_rect()
        self.dead = False
        self.vel = vec(-1, 0)
        self.pos = vec(x, y)
        self.current_frame = 0
        self.last_update = 0
        self.num = 0
        self.obstacle = False
        self.falling_obstacle = False

    def images(self):
        self.walk = [pg.image.load('images/goomba1.png').convert_alpha(),
                     pg.image.load('images/goomba2.png').convert_alpha()]
        self.rect = self.walk[0].get_rect()
        self.walk = [pg.transform.scale(self.walk[0], (int(self.rect.width * 3.214), int(self.rect.height * 3.214))),
                      pg.transform.scale(self.walk[1], (int(self.rect.width * 3.214), int(self.rect.height * 3.214)))]
        self.deads = pg.image.load('images/goomba3.png').convert_alpha()
        self.deads = pg.transform.scale(self.deads, (int(self.rect.width * 3.214), int(self.rect.height * 3.214)))

    def update(self):
        self.animate()
        self.vel.y = 10
        self.pos += self.vel
        self.rect.midbottom = self.pos

        if self.dead:
            self.image = self.deads
            self.vel.x = 0
            if self.num > 1:
                self.kill()
                self.num = 0
            self.num += 0.04

    def animate(self):
        now = pg.time.get_ticks()
        if now - self.last_update > 100:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.walk)
            self.image = self.walk[self.current_frame]

class Fire(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.screen = self.game.screen
        self.image = pg.image.load('images/fire.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.image = pg.transform.scale(self.image, (int(self.rect.width * 3.214), int(self.rect.height * 3.214)))
        self.vel = vec(0, 0)
        self.pos = vec(x, y)
        self.obstacle = True
        self.falling_obstacle = False

    def update(self):
        self.pos += self.vel
        self.rect.center = self.pos

class Cloud(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.screen = self.game.screen
        self.image = pg.image.load('images/cloud.png').convert()
        self.rect = self.image.get_rect()
        self.image = pg.transform.scale(self.image, (int(self.rect.width * 3.214), int(self.rect.height * 3.214)))
        self.rect = self.image.get_rect()
        self.vel = vec(0, 0)
        self.pos = vec(x, y)
        self.obstacle = True
        self.falling_obstacle = False
        self.hit = False

    def update(self):
        if self.hit:
            self.image = pg.image.load('images/cloud2.png').convert()
            self.rect = self.image.get_rect()
            self.image = pg.transform.scale(self.image, (int(self.rect.width * 3.214), int(self.rect.height * 3.214)))
            self.rect = self.image.get_rect()
        self.pos += self.vel
        self.rect.center = self.pos
