import pygame as pg
from settings import *
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.screen = self.game.screen
        self.right = True
        self.walking = False
        self.jumping = False
        self.dead = False
        self.finish = False
        self.current_frame = 0
        self.last_update = 0
        self.images()
        self.image = self.stand_img
        self.rect = self.image.get_rect()
        self.pos = vec(120, 643)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.fvel = vec(0, 0)
        self.facc = vec(0, 0)
        self.score = 0
        self.timer = 0
        self.near_finish = False
    
    def images(self):
        if self.game.doge:
            self.stand_img = pg.image.load('images/dstand.png').convert_alpha()
            self.rect = self.stand_img.get_rect()
            self.stand_img = pg.transform.scale(self.stand_img, (int(self.rect.width * 2.5), int(self.rect.height * 2.5)))
            self.walk_img = [pg.image.load('images/dwalk1.png').convert_alpha(),
                             pg.image.load('images/dwalk2.png').convert_alpha()]
            self.rect = self.walk_img[0].get_rect()
            self.rect1 = self.walk_img[1].get_rect()
            self.walk_img = [
                pg.transform.scale(self.walk_img[0], (int(self.rect.width * 2.5), int(self.rect.height * 2.5))),
                pg.transform.scale(self.walk_img[1], (int(self.rect1.width * 2.5), int(self.rect1.height * 2.5)))]
            self.jump_img = pg.image.load('images/djump.png').convert_alpha()
            self.rect = self.jump_img.get_rect()
            self.jump_img = pg.transform.scale(self.jump_img,(int(self.rect.width * 2.5), int(self.rect.height * 2.5)))
            self.dead_img = pg.image.load('images/ddead.png').convert_alpha()
            self.rect = self.dead_img.get_rect()
            self.dead_img = pg.transform.scale(self.dead_img,(int(self.rect.width * 2.5), int(self.rect.height * 2.5)))
        else:
            self.stand_img = pg.image.load('images/mario.png').convert_alpha()
            self.rect = self.stand_img.get_rect()
            self.stand_img = pg.transform.scale(self.stand_img, (int(self.rect.width * 3.214), int(self.rect.height * 3.214)))
            self.walk_img = [pg.image.load('images/walk1.png').convert_alpha(),
                          pg.image.load('images/walk2.png').convert_alpha(),
                          pg.image.load('images/walk3.png').convert_alpha()]
            self.walk_img = [pg.transform.scale(self.walk_img[0], (int(self.rect.width * 3.214), int(self.rect.height * 3.214))),
                          pg.transform.scale(self.walk_img[1], (int(self.rect.width * 3.214), int(self.rect.height * 3.214))),
                          pg.transform.scale(self.walk_img[2], (int(self.rect.width * 3.214), int(self.rect.height * 3.214)))]
            self.jump_img = pg.image.load('images/jump.png').convert_alpha()
            self.jump_img = pg.transform.scale(self.jump_img , (int(self.rect.width * 3.214), int(self.rect.height * 3.214)))
            self.dead_img = pg.image.load('images/dead.png').convert_alpha()
            self.dead_img = pg.transform.scale(self.dead_img, (int(self.rect.width * 3.214), int(self.rect.height * 3.214)))

    def jump(self):
        if not self.jumping:
            if self.game.doge:
                self.game.bark.play()
            else:
                self.game.jump_fx.play()
            self.vel.y = -jump

    def jump_cut(self):
        if self.jumping:
            if self.vel.y < -10:
                self.vel.y = -10

    def update(self):
        self.anime()
        if not self.dead and not self.finish:
            self.acc = vec(0, gravity)
            self.facc = vec(0, gravity)
            keys = pg.key.get_pressed()
            if keys[pg.K_LEFT] and keys[pg.K_RIGHT] or keys[pg.K_a] and keys[pg.K_d]:
                self.acc.x = 0
            elif keys[pg.K_LEFT] or keys[pg.K_a]:
                if self.game.doge:
                    self.acc.x = -7.5
                else:
                    self.acc.x = -acceleration
                self.facc.x = -7.5
            elif keys[pg.K_RIGHT] or keys[pg.K_d]:
                if self.game.doge:
                    self.acc.x = 7.5
                else:
                    self.acc.x = acceleration
                self.facc.x = 7.5

        # apply friction
        if self.game.doge:
            self.acc.x += self.vel.x * -1
        else:
            self.acc.x += self.vel.x * friction
        # equations of motion
        self.vel += self.acc
        if abs(self.vel.x) < 0.1:
            self.vel.x = 0
        self.pos += self.vel + 0.5 * self.acc

        # apply friction
        self.facc.x += self.fvel.x * -1
        # equations of motion
        self.fvel += self.facc
        if abs(self.fvel.x) < 0.1:
            self.fvel.x = 0

        # Block the edge of the screen.
        if self.pos.x < 15:
            self.pos.x = 15
        if not self.finish:
            if self.near_finish:
                if self.pos.x > screen_width - 15:
                    self.pos.x = screen_width - 15

        #  Die if player fell off the screen.
        if self.pos.y > screen_height + 51:
            if not self.dead:
                self.dead = True
                self.game.death.play()

        if self.dead:
            pg.mixer.music.stop()
            self.game.timer = 0
            self.timer += 1
            for sprite in self.game.enemies:
                sprite.vel.x = 0
                sprite.vel.y = 0
            for sprite in self.game.items:
                sprite.vel.x = 0
                sprite.vel.y = 0
            if self.timer < 25:
                self.acc = vec(0, 0)
                self.vel.x = 0
                self.vel.y = 0
            if self.timer >= 25:
                if not self.pos.y > screen_height + 51:
                    self.acc = vec(0, gravity)
                    self.pos.y -= 15
            if self.timer >= 150:
                self.game.lives -= 1
                self.game.play = False
                self.game.music = False

        if self.finish:
            if not self.dead:
                self.acc = vec(0, gravity)
                if self.game.timer >= 50:
                    self.pos.x += 1.2
                    self.vel.x = 1
                if self.game.timer >= 260:
                    self.pos.x -= 1.2
                    self.vel.x = 0
                    self.kill()

        self.rect.midbottom = self.pos

    def anime(self):
        now = pg.time.get_ticks()
        if self.fvel.x != 0:
            self.walking = True
        else:
            self.walking = False
        if self.vel.y != 0:
            self.jumping = True
        else:
            self.jumping = False
        #  Show walk animation.
        if self.walking:
            if now - self.last_update > 30:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.walk_img)
                if self.vel.x > 0:
                    self.right = True
                    self.image = self.walk_img[self.current_frame]
                else:
                    self.right = False
                    self.image = pg.transform.flip(self.walk_img[self.current_frame], True, False)

        if not self.walking:
            if self.right == True:
                self.image = self.stand_img
            else:
                self.image = pg.transform.flip(self.stand_img, True, False)

        if self.jumping:
            if self.right == True:
                self.image = self.jump_img
            elif self.vel.x > 0:
                self.image = self.jump_img
            else:
                self.image = pg.transform.flip(self.jump_img, True, False)

        if self.dead:
            self.image = self.dead_img
