# Muhammad Erizky S
# 2201797052
# Final Project - Not Your Ordinary Platform Game

import pygame as pg
# from random import choice
# import as least as possible <- My principle
from settings import *
from player import *
from level import *
from enemy import *

class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        for setting in open('setting.txt', 'r'):
            self.window_mode = eval(setting)
        if self.window_mode == 0:
            self.window = 'WINDOWED'
        else:
            self.window = 'FULLSCREEN'
            pg.mouse.set_visible(False)
        self.fps = 'OFF'
        self.mute = 'OFF'
        self.screen = pg.display.set_mode((screen_width, screen_height), self.window_mode | pg.DOUBLEBUF)
        pg.display.set_caption("NYOPG")
        self.clock = pg.time.Clock()
        pg.display.set_icon(pg.image.load("images/mario.png").convert_alpha())
        self.highscore = {}
        for row in open('highscore.txt','r'):
            file = row.split()
            self.highscore[file[0]] = file[1]
        self.menu_arrow_pos_y = 437
        self.setting_arrow_pos_y = 277
        self.text_pos_x = 840
        self.up_counter = 0
        self.secret_unlocked = False
        self.run = True
        self.doge = False
        self.speedrun = False
        self.howtoplay = False
        self.setting = False
        self.restart = False
        self.next_time = False
        self.start = False
        self.play = False
        self.music = False
        self.lives = 3
        self.timer = 0
        self.checkpoint = False
        self.minute = 0
        self.second = 0
        self.milisecond = 0
        self.true_finish = False

    def load(self):
        if self.doge:
            pg.mixer.music.load('sound/dog.mp3')
        else:
            pg.mixer.music.load('sound/music.ogg')
        self.jump_fx = pg.mixer.Sound('sound/small_jump.ogg')
        self.death = pg.mixer.Sound('sound/dead.ogg')
        self.stomp = pg.mixer.Sound('sound/stomp.ogg')
        self.coin_fx = pg.mixer.Sound('sound/coin.ogg')
        self.get_item = pg.mixer.Sound('sound/powerup_appears.ogg')
        self.powerup = pg.mixer.Sound('sound/powerup.ogg')
        self.select_fx = pg.mixer.Sound('sound/select.ogg')
        self.move_fx = pg.mixer.Sound('sound/move.ogg')
        self.secret = pg.mixer.Sound('sound/secret.ogg')
        self.wow = pg.mixer.Sound('sound/wow.ogg')
        self.bark = pg.mixer.Sound('sound/bark.ogg')
        if self.mute == 'OFF':
            pg.mixer.music.set_volume(0.2)
            self.jump_fx.set_volume(0.2)
            self.death.set_volume(0.2)
            self.stomp.set_volume(0.2)
            self.coin_fx.set_volume(0.2)
            self.get_item.set_volume(0.2)
            self.powerup.set_volume(0.2)
            self.select_fx.set_volume(0.2)
            self.move_fx.set_volume(0.2)
            self.secret.set_volume(0.2)
            self.wow.set_volume(0.2)
            self.bark.set_volume(0.2)
        else:
            pg.mixer.music.set_volume(0.0)
            self.jump_fx.set_volume(0.0)
            self.death.set_volume(0.0)
            self.stomp.set_volume(0.0)
            self.coin_fx.set_volume(0.0)
            self.get_item.set_volume(0.0)
            self.powerup.set_volume(0.0)
            self.select_fx.set_volume(0.0)
            self.move_fx.set_volume(0.0)
            self.secret.set_volume(0.0)
            self.wow.set_volume(0.0)
            self.bark.set_volume(0.0)

    def new_game(self):
        self.load()
        self.all_sprites = pg.sprite.Group()
        self.bricks = pg.sprite.Group()
        self.mysteries = pg.sprite.Group()
        self.annoyings = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.pipes = pg.sprite.Group()
        self.items = pg.sprite.Group()
        self.bambozled = pg.sprite.Group()
        self.bambozled2 = pg.sprite.Group()
        self.bambozled3 = pg.sprite.Group()
        self.bambozled4 = pg.sprite.Group()
        self.bambozled5 = pg.sprite.Group()
        self.bambozled6 = pg.sprite.Group()
        self.bambozled7 = pg.sprite.Group()
        self.bambozled8 = pg.sprite.Group()
        self.bambozled9 = pg.sprite.Group()
        self.bambozled10 = pg.sprite.Group()
        self.bambozled11 = pg.sprite.Group()
        self.bambozled12 = pg.sprite.Group()
        self.bambozled13 = pg.sprite.Group()
        self.flagpole = pg.sprite.Group()
        self.checkpointpole = pg.sprite.Group()
        self.ed = pg.sprite.Group()

        self.player = Player(self)
        self.level = Level(self)
        self.all_sprites.add(self.level)
        for foo in floor:
            f = Floor(self,*foo)
            self.all_sprites.add(f)
            self.bricks.add(f)
        for brick in brick_list:
            b = Brick(self,*brick)
            self.all_sprites.add(b)
            self.bricks.add(b)
        for mystery in mystery_list:
            m = Brick(self,*mystery)
            self.all_sprites.add(m)
            self.bricks.add(m)
            self.mysteries.add(m)
        for annoying in annoying_list:
            a = Annoying(self,*annoying)
            self.all_sprites.add(a)
            self.annoyings.add(a)
        for enemy in enemy_list:
            e = Goomba(self,*enemy)
            self.all_sprites.add(e)
            self.enemies.add(e)
        for pipe in pipe_list:
            p = Pipe(*pipe)
            self.all_sprites.add(p)
            self.pipes.add(p)

        self.sensor1 = InvisibleNightmare(3600,1)
        self.all_sprites.add(self.sensor1)
        self.sensor1 = pg.sprite.Group(self.sensor1)

        self.sensor2 = InvisibleNightmare(4400,1)
        self.all_sprites.add(self.sensor2)
        self.sensor2 = pg.sprite.Group(self.sensor2)

        self.bambozle = Brick(self,2,849,463)
        self.all_sprites.add(self.bambozle)
        self.bricks.add(self.bambozle)
        self.bambozled.add(self.bambozle)

        self.bambozle2 = Brick(self,2,1157,257)
        self.all_sprites.add(self.bambozle2)
        self.bricks.add(self.bambozle2)
        self.bambozled2.add(self.bambozle2)

        self.bambozle3 = InvisibleNightmare(1422,1)
        self.all_sprites.add(self.bambozle3)
        self.bambozled3.add(self.bambozle3)

        self.bambozle4 = Goomba(self,2600,626)
        self.all_sprites.add(self.bambozle4)
        self.bambozled4.add(self.bambozle4)

        self.bambozle5 = Brick(self,2,4036,463)
        self.all_sprites.add(self.bambozle5)
        self.bricks.add(self.bambozle5)
        self.bambozled5.add(self.bambozle5)

        self.bambozle6 = InvisibleNightmare(4150,1)
        self.all_sprites.add(self.bambozle6)
        self.bambozled6.add(self.bambozle6)
        self.bambozlebrick = Brick(self,4,4216,257)
        self.all_sprites.add(self.bambozlebrick)
        self.enemies.add(self.bambozlebrick)

        self.bambozle7 = InvisibleNightmare(4535,1)
        self.all_sprites.add(self.bambozle7)
        self.bambozled7.add(self.bambozle7)

        self.bambozle8 = Brick(self,2,5219,463)
        self.all_sprites.add(self.bambozle8)
        self.bricks.add(self.bambozle8)
        self.bambozled8.add(self.bambozle8)

        self.bambozle9 = Floor(self,7,5502,643)
        self.all_sprites.add(self.bambozle9)
        self.bricks.add(self.bambozle9)
        self.bambozled9.add(self.bambozle9)

        self.bambozle10  = Cloud(self,7340,330)
        self.all_sprites.add(self.bambozle10)
        self.enemies.add(self.bambozle10)
        self.bambozled10.add(self.bambozle10)

        self.bambozle11 = InvisibleNightmare(7780,1)
        self.all_sprites.add(self.bambozle11)
        self.bambozled11.add(self.bambozle11)

        self.bambozle12 = InvisibleNightmare(8040,5)
        self.all_sprites.add(self.bambozle12)
        self.bambozled12.add(self.bambozle12)

        self.bambozle13 = InvisibleNightmare(8475,1)
        self.all_sprites.add(self.bambozle13)
        self.bambozled13.add(self.bambozle13)

        self.flag = Flag(self,1,8325,375)
        self.all_sprites.add(self.flag)
        self.flagpole.add(self.flag)

        self.end = InvisibleNightmare(8600,1)
        self.all_sprites.add(self.end)
        self.ed.add(self.end)

        self.all_sprites.add(self.player)
        if self.checkpoint:
            for sprite in self.all_sprites:
                sprite.rect.x -= 5000
            for e in self.enemies:
                e.pos.x -= 5000
            for b in self.bambozled4:
                b.pos.x -= 5000
        else:
            self.checkpoint_flag = Flag(self,2,5190,390)
            self.all_sprites.add(self.checkpoint_flag)
            self.checkpointpole.add(self.checkpoint_flag)
            for sprite in self.all_sprites:
                sprite.rect.x -= 500
            for e in self.enemies:
                e.pos.x -= 500
            for b in self.bambozled4:
                b.pos.x -= 500

    def run_the_game(self):
        self.splash()
        while self.run:
            self.menu()
            while self.start:
                self.new_game()
                self.game_over()
                self.play = True
                while self.play:
                    self.clock.tick(FPS)
                    self.events()
                    self.update()
                    self.draw()
                    if self.true_finish:
                        if not self.speedrun:
                            self.win()
                        else:
                            self.prize()
                        self.play = False
                        self.start = False

    def events(self):
        global run, start
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.play = False
                self.start = False
                self.run = False
                run = False
                start = False
            if not self.player.dead and not self.player.finish:
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.play = False
                        self.start = False
                        self.lives = 3
                        self.checkpoint = False
                        self.music = False
                        self.speedrun = False
                        if self.doge:
                            self.player.score = 0
                        self.doge = False
                        self.minute = 0
                        self.second = 0
                        self.milisecond = 0
                    if event.key == pg.K_SPACE:
                        self.player.jump()
                    if event.key == pg.K_UP:
                        self.player.jump()
                if event.type == pg.KEYUP:
                    if event.key == pg.K_ESCAPE:
                        None
                    if event.key == pg.K_SPACE:
                        self.player.jump_cut()
                    if event.key == pg.K_UP:
                        self.player.jump_cut()

    def update(self):
        if not self.music and self.play:
            pg.mixer.music.play(-1)
            self.music = True
        if not self.music and not self.play:
            pg.mixer.music.stop()
        self.all_sprites.update()

        #  Move camera to the right if player on center of screen.
        if not self.player.finish:
            if not self.player.near_finish:
                if self.player.rect.x > screen_width / 2:
                    self.player.rect.x = screen_width / 2
                    for sprite in self.all_sprites:
                        if self.doge:
                            if self.player.vel.x > 0:
                                sprite.rect.x -= abs(self.player.vel.x - 5) + 7.5
                        else:
                            if self.player.fvel.x > 0:
                                sprite.rect.x -= abs(self.player.fvel.x) + 2.5
                    for e in self.enemies:
                        if self.doge:
                            if self.player.vel.x > 0:
                                e.pos.x -= abs(self.player.vel.x - 5) + 7.5
                        else:
                            if self.player.fvel.x > 0:
                                e.pos.x -= abs(self.player.fvel.x) + 2.5
                    for i in self.items:
                        if self.doge:
                            if self.player.vel.x > 0:
                                i.pos.x -= abs(self.player.vel.x - 5) + 7.5
                        else:
                            if self.player.fvel.x > 0:
                                i.pos.x -= abs(self.player.fvel.x) + 2.5
                    for b in self.bambozled4:
                        if self.doge:
                            if self.player.vel.x > 0:
                                b.pos.x -= abs(self.player.vel.x - 5) + 7.5
                        else:
                            if self.player.fvel.x > 0:
                                b.pos.x -= abs(self.player.fvel.x) + 2.5
                    if self.doge:
                        self.player.pos.x = screen_width / 2 + 75
                    else:
                        self.player.pos.x = screen_width / 2 + 25
        else:
            None

        #  Item collisions.
        item = pg.sprite.groupcollide(self.items, self.bricks, False, False)
        if item:
            for a in item:
                for b in item[a]:
                    if not a.star:
                        a.pos.y = b.rect.top
                        a.vel.y = 0
                    if a.star:
                        if a.vel.y > 9:
                            a.pos.y = b.rect.top
                            a.vel.y -= 25
                        elif a.vel.y < 10:
                            if a.vel.x > 0:
                                a.pos.x = b.rect.left - 25
                                a.vel.x = -5
                            elif a.vel.x < 0:
                                a.pos.x = b.rect.right + 25
                                a.vel.x = 5

        item2 = pg.sprite.groupcollide(self.items, self.pipes, False, False)
        if item2:
            for e in item2:
                if e.vel.x > 0:
                    e.vel.x = -1
                else:
                    e.vel.x = 1

        #  Enemy collisions.
        monster = pg.sprite.groupcollide(self.enemies, self.bricks, False, False)
        if monster:
            for a in monster:
                for b in monster[a]:
                    if not a.obstacle and not a.falling_obstacle:
                        a.pos.y = b.rect.top
                        a.vel.y = 0
                    if a.obstacle:
                        None
                    if a.falling_obstacle:
                        None

        monster2 = pg.sprite.groupcollide(self.enemies, self.pipes, False, False)
        if monster2:
            for e in monster2:
                if e.vel.x > 0:
                    e.vel.x = -1
                else:
                    e.vel.x = 1

        monster3 = pg.sprite.groupcollide(self.enemies, self.enemies, False, False)
        if monster3:
            for a in monster3:
                for b in monster3[a]:
                    if not a.obstacle and not a.falling_obstacle:
                        if b.falling_obstacle:
                            a.pos.y = b.rect.top
                            a.vel.y = 0

        #  Spawn enemies when player reach certain distance.
        sensor1 = pg.sprite.spritecollide(self.player, self.sensor1, True)
        if sensor1:
            for enemy in [(900,350),(1000,50)]:
                e = Goomba(self, *enemy)
                self.all_sprites.add(e)
                self.enemies.add(e)

        sensor2 = pg.sprite.spritecollide(self.player, self.sensor2, True)
        if sensor2:
            for enemy in [(950, 640), (1050, 640), (1250, 640)]:
                e = Goomba(self, *enemy)
                self.all_sprites.add(e)
                self.enemies.add(e)

        #  All bamboozles

        # 1.  Moving mystery block
        bambozled = pg.sprite.spritecollide(self.player, self.bambozled, False)
        if bambozled:
            if self.player.vel.y < 0:
                if self.player.rect.top > bambozled[0].rect.centery:
                    bambozled[0].rect.y += self.player.vel.y
                elif self.player.vel.x > 0:
                    self.player.pos.x = bambozled[0].rect.left - 25
                elif self.player.vel.x < 0:
                    self.player.pos.x = bambozled[0].rect.right + 25

        # 2.  Hit mystery block give enemy
        bambozled2 = pg.sprite.spritecollide(self.player, self.bambozled2, False)
        if bambozled2:
            if not bambozled2[0].hit:
                if self.player.vel.y < 0:
                    if self.player.rect.top > bambozled2[0].rect.centery:
                        bambozled2[0].hit = True
                        self.get_item.play()
                        enemy = Goomba(self,bambozled2[0].rect.centerx, bambozled2[0].rect.centery - 51)
                        self.all_sprites.add(enemy)
                        self.enemies.add(enemy)
                        enemy.vel.x = 1
                        self.player.pos.y = bambozled2[0].rect.bottom + 50
                        self.player.vel.y = 0
                    elif self.player.vel.x > 0:
                        self.player.pos.x = bambozled2[0].rect.left - 25
                    elif self.player.vel.x < 0:
                        self.player.pos.x = bambozled2[0].rect.right + 25

        # 3.  Shoot obstacle from pipe
        bambozled3 = pg.sprite.spritecollide(self.player, self.bambozled3, True)
        if bambozled3:
            fire = Fire(self,452,650)
            self.all_sprites.add(fire)
            self.enemies.add(fire)
            fire.vel.y = -50

        # 4.  Abnormal enemy
        bambozled4 = pg.sprite.spritecollide(self.player, self.bambozled4, False)
        if bambozled4:
            if not self.player.dead:
                if self.player.vel.y > gravity:
                    self.stomp.play()
                    self.player.vel.y -= 35
                if self.player.vel.y == 0.8:
                    if self.player.vel.x >= 0:
                        self.player.dead = True
                        self.death.play()
                    elif self.player.vel.x < 0:
                        self.player.dead = True
                        self.death.play()
            else:
                None

        bambozled41 = pg.sprite.groupcollide(self.bambozled4, self.bricks, False, False)
        if bambozled41:
            for aa in bambozled41:
                for bb in self.bricks:
                    if aa.rect.bottom < bb.rect.bottom:
                        aa.pos.y = bb.rect.top
                        aa.vel.y = 0

        bambozled42 = pg.sprite.groupcollide(self.bambozled4, self.pipes, False, False)
        if bambozled42:
            for cc in bambozled42:
                if cc.vel.x > 0:
                    cc.vel.x = -1
                else:
                    cc.vel.x = 1

        # 5.  Hit mystery block give mushroom
        bambozled5 = pg.sprite.spritecollide(self.player, self.bambozled5, False)
        if bambozled5:
            if not bambozled5[0].hit:
                if self.player.vel.y < 0:
                    bambozled5[0].hit = True
                    self.get_item.play()
                    item = Mushroom(self,bambozled5[0].rect.centerx, bambozled5[0].rect.centery - 51)
                    self.all_sprites.add(item)
                    self.items.add(item)
                    item.vel.x = 1
                    self.player.pos.y = bambozled5[0].rect.bottom + 50
                    self.player.vel.y = 0

        # 6.  Brick falling
        bambozled6 = pg.sprite.spritecollide(self.player, self.bambozled6, True)
        if bambozled6:
            self.bambozlebrick.vel.y = 25

        # 7.  Enemy falling
        bambozled7 = pg.sprite.spritecollide(self.player, self.bambozled7, True)
        if bambozled7:
            enemynem = Fire(self,462,0)
            enemynem.image = pg.transform.rotate(enemynem.image,180)
            self.all_sprites.add(enemynem)
            self.enemies.add(enemynem)
            enemynem.vel.y = 50
            enemynem.obstacle = True

        # 8.  Shooting Star
        bambozled8 = pg.sprite.spritecollide(self.player, self.bambozled8, False)
        if bambozled8:
            if not bambozled8[0].hit:
                if self.player.vel.y < 0:
                    bambozled8[0].hit = True
                    self.get_item.play()
                    item = Star(self,bambozled8[0].rect.centerx, bambozled8[0].rect.centery - 51)
                    self.all_sprites.add(item)
                    self.items.add(item)
                    item.vel.x = 5
                    # item.vel.y = 10
                    self.player.pos.y = bambozled8[0].rect.bottom + 50
                    self.player.vel.y = 0

        # 9.  Floor falling
        bambozled9 = pg.sprite.spritecollide(self.player, self.bambozled9, False)
        if bambozled9:
            if self.player.rect.left > bambozled9[0].rect.left:
                bambozled9[0].rect.y += 20

        # 10.  Cloud
        bambozled10 = pg.sprite.spritecollide(self.player, self.bambozled10, False)
        if bambozled10:
            bambozled10[0].hit = True

        # 11.  Throw 4 enemies from above
        bambozled11 = pg.sprite.spritecollide(self.player, self.bambozled11, True)
        if bambozled11:
            for enemy in [(490,100),(541,100),(592,100),(643,100)]:
                e = Goomba(self,*enemy)
                self.all_sprites.add(e)
                self.enemies.add(e)

        # 12.  Shoot
        bambozled12 = pg.sprite.spritecollide(self.player, self.bambozled12, False)
        if bambozled12:
            keys = pg.key.get_pressed()
            if keys[pg.K_SPACE]:
                if keys[pg.K_d]:
                    pass
                if keys[pg.K_RIGHT]:
                    pass
                boom = Fire(self,768,120)
                boom.image = pg.transform.rotate(boom.image,270)
                self.all_sprites.add(boom)
                self.enemies.add(boom)
                boom.vel.x -= 50

        # 13.  Final Attack
        bambozled13 = pg.sprite.spritecollide(self.player, self.bambozled13, True)
        if bambozled13:
            final = Goomba(self,700,100)
            final.vel.y = 100
            final.vel.x = 0
            self.all_sprites.add(final)
            self.enemies.add(final)

        finish = pg.sprite.spritecollide(self.player, self.flagpole, False)
        if finish:
            self.player.vel.x = 0
            self.player.finish = True

        checkpoint = pg.sprite.spritecollide(self.player, self.checkpointpole, True)
        if checkpoint:
            self.checkpoint = True
            self.all_sprites.remove(self.checkpoint_flag)

        near_finish = pg.sprite.spritecollide(self.player, self.ed, True)
        if near_finish:
            self.player.near_finish = True

        #  Player collision

        #  Check for mystery box collision.
        hits2 = pg.sprite.spritecollide(self.player, self.mysteries, False)
        if hits2:
            if not hits2[0].hit:
                if self.player.vel.y < 0:
                    if self.player.rect.top > hits2[0].rect.centery:
                        hits2[0].hit = True
                        self.coin_fx.play()
                        coin = Coin(self,1, hits2[0].rect.centerx - 5, hits2[0].rect.centery - 60)
                        self.all_sprites.add(coin)
                        self.player.pos.y = hits2[0].rect.bottom + 50
                        self.player.vel.y = 0
                    elif self.player.vel.x > 0 and not self.player.rect.top > hits2[0].rect.centery:
                        self.player.pos.x = hits2[0].rect.left - 25
                    elif self.player.vel.x < 0 and not self.player.rect.top > hits2[0].rect.centery:
                        self.player.pos.x = hits2[0].rect.right + 25

        #  Check for all bricks collision.
        hits = pg.sprite.spritecollide(self.player, self.bricks, False)
        if hits:
            if not self.player.dead:
                if self.player.vel.y > gravity:
                    if self.player.rect.bottom < hits[0].rect.centery:
                        self.player.pos.y = hits[0].rect.top
                        self.player.vel.y = 0
                    elif self.player.vel.x > 0:
                        self.player.pos.x = hits[0].rect.left - 25
                    elif self.player.vel.x < 0:
                        self.player.pos.x = hits[0].rect.right + 25
                elif self.player.vel.y < gravity:
                    if self.player.rect.top > hits[0].rect.centery:
                        if self.player.vel.x > 0:
                            self.player.pos.y = hits[0].rect.bottom + 50
                            self.player.vel.y = 0
                        elif self.player.vel.x < 0:
                            self.player.pos.y = hits[0].rect.bottom + 50
                            self.player.vel.y = 0
                        else:
                            self.player.pos.y = hits[0].rect.bottom + 50
                            self.player.vel.y = 0
                    if self.player.vel.x > 0 and not self.player.rect.top > hits[0].rect.centery:
                        self.player.pos.x = hits[0].rect.left - 25
                    elif self.player.vel.x < 0 and not self.player.rect.top > hits[0].rect.centery:
                        self.player.pos.x = hits[0].rect.right + 25
                elif self.player.vel.y == gravity:
                    if self.player.rect.bottom < hits[0].rect.centery:
                        self.player.pos.y = hits[0].rect.top
                        self.player.vel.y = 0
                        if len(hits) > 1:
                            if self.player.rect.bottom < hits[1].rect.centery:
                                self.player.pos.y = hits[1].rect.top
                                self.player.vel.y = 0
                            else:
                                if self.player.vel.x > 0:
                                    self.player.pos.x = hits[1].rect.left - 25
                                elif self.player.vel.x < 0:
                                    self.player.pos.x = hits[1].rect.right + 25

        #  Check for hidden block collision.
        hits3 = pg.sprite.spritecollide(self.player, self.annoyings, False)
        if hits3:
            if hits3[0].hit:
                if not self.player.dead:
                    if self.player.vel.y > 0:
                        if self.player.rect.bottom < hits3[0].rect.centery:
                            self.player.pos.y = hits3[0].rect.top
                            self.player.vel.y = 0
                        elif self.player.vel.x > 0:
                            self.player.pos.x = hits3[0].rect.left - 25
                        elif self.player.vel.x < 0:
                            self.player.pos.x = hits3[0].rect.right + 25
                    elif self.player.vel.y < 0:
                        if self.player.rect.top > hits3[0].rect.centery:
                            if self.player.vel.x > 0:
                                self.player.pos.y = hits3[0].rect.bottom + 50
                                self.player.vel.y = 0
                            elif self.player.vel.x < 0:
                                self.player.pos.y = hits3[0].rect.bottom + 50
                                self.player.vel.y = 0
                            else:
                                self.player.pos.y = hits3[0].rect.bottom + 50
                                self.player.vel.y = 0
                        elif self.player.vel.x > 0 and not self.player.rect.top > hits3[0].rect.centery:
                            self.player.pos.x = hits3[0].rect.left - 25
                        elif self.player.vel.x < 0 and not self.player.rect.top > hits3[0].rect.centery:
                            self.player.pos.x = hits3[0].rect.right + 25
                    elif self.player.vel.x > 0:
                        self.player.pos.x = hits3[0].rect.left - 25
                    elif self.player.vel.x < 0:
                        self.player.pos.x = hits3[0].rect.right + 25
            if not hits3[0].hit:
                if self.player.vel.y < 0:
                    if self.player.rect.top > hits3[0].rect.centery:
                        hits3[0].hit = True
                        self.coin_fx.play()
                        coin = Coin(self,1, hits3[0].rect.centerx - 5, hits3[0].rect.centery - 60)
                        self.all_sprites.add(coin)
                        self.player.pos.y = hits3[0].rect.bottom + 50
                        self.player.vel.y = 0
                    elif self.player.vel.x > 0:
                        None
                    elif self.player.vel.x < 0:
                        None

        #  Check for enemy collision.
        enemy_hits = pg.sprite.spritecollide(self.player, self.enemies, False)
        if enemy_hits:
            if not self.player.dead:
                if not enemy_hits[0].obstacle and not enemy_hits[0].falling_obstacle:
                    if not enemy_hits[0].dead:
                        if self.player.vel.y > 0:
                            self.stomp.play()
                            if self.doge:
                                # self.player.score = choice(['WOW','MUCH JUMPING','VERY PLATFORM','SO FUN','VERY WOW'])
                                self.player.score = 'WOW'
                            else:
                                # self.player.score += choice([-250,250])
                                self.player.score += -250
                            self.player.pos.y = enemy_hits[0].rect.top - 25
                            enemy_hits[0].dead = True
                            self.player.vel.y = 3
                        else:
                            self.player.dead = True
                            self.death.play()
                if enemy_hits[0].obstacle:
                    self.player.dead = True
                    self.death.play()
                if enemy_hits[0].falling_obstacle:
                    if enemy_hits[0].vel.y == 0:
                        if not self.player.dead:
                            if self.player.vel.y > 0:
                                if self.player.rect.bottom < enemy_hits[0].rect.centery:
                                    self.player.pos.y = enemy_hits[0].rect.top
                                    self.player.vel.y = 0
                                elif self.player.vel.x > 0:
                                    self.player.pos.x = enemy_hits[0].rect.left - 25
                                elif self.player.vel.x < 0:
                                    self.player.pos.x = enemy_hits[0].rect.right + 25
                            elif self.player.vel.y < 0:
                                if self.player.rect.top > enemy_hits[0].rect.centery:
                                    if self.player.vel.x > 0:
                                        self.player.pos.y = enemy_hits[0].rect.bottom + 50
                                        self.player.vel.y = 0
                                    elif self.player.vel.x < 0:
                                        self.player.pos.y = enemy_hits[0].rect.bottom + 50
                                        self.player.vel.y = 0
                                    else:
                                        self.player.pos.y = enemy_hits[0].rect.bottom + 50
                                        self.player.vel.y = 0
                                if self.player.vel.x > 0 and not self.player.rect.top > enemy_hits[0].rect.centery:
                                    self.player.pos.x = enemy_hits[0].rect.left - 25
                                elif self.player.vel.x < 0 and not self.player.rect.top > enemy_hits[0].rect.centery:
                                    self.player.pos.x = enemy_hits[0].rect.right + 25
                            elif self.player.vel.x > 0:
                                self.player.pos.x = enemy_hits[0].rect.left - 25
                            elif self.player.vel.x < 0:
                                self.player.pos.x = enemy_hits[0].rect.right + 25
                    else:
                        if not self.player.dead:
                            if self.player.vel.y > 0:
                                    if self.player.rect.bottom < enemy_hits[0].rect.centery:
                                        self.player.pos.y = enemy_hits[0].rect.top
                                        self.player.vel.y = 0
                            else:
                                self.player.dead = True
                                self.death.play()

        #  Check for pipe collision.
        hits4 = pg.sprite.spritecollide(self.player, self.pipes, False)
        if hits4:
            if not self.player.dead:
                if self.player.vel.y > 0 and self.player.pos.y < hits4[0].rect.centery:
                    self.player.pos.y = hits4[0].rect.top
                    self.player.vel.y = 0
                elif self.player.vel.x > 0:
                    self.player.pos.x = hits4[0].rect.left - 25
                elif self.player.vel.x < 0:
                    self.player.pos.x = hits4[0].rect.right + 25

        #  Check for item collisiom.
        item_hits = pg.sprite.spritecollide(self.player, self.items, True)
        if item_hits:
            if not self.player.dead:
                if not item_hits[0].star:
                    self.powerup.play()
                if item_hits[0].star:
                    self.player.dead = True
                    self.death.play()

        #  Kill enemy if they leave the screen
        for enemies in self.enemies:
            if enemies.rect.x < -51:
                if enemies.obstacle:
                    None
                else:
                    enemies.kill()
            if enemies.rect.y > screen_height + 51 or enemies.rect.y < -51:
                enemies.kill()

        for brick in self.bricks:
            if brick.rect.y > screen_height:
                brick.kill()

        if self.player.finish:
            self.timer += 1
            if self.timer >= 300:
                self.true_finish = True
                self.timer = 0

        if not self.player.finish and self.speedrun:
            self.milisecond += 1.5
        if self.milisecond > 99:
            self.milisecond = 0
            self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1

    def draw(self):
        self.all_sprites.draw(self.screen)
        if self.doge:
            self.draw_text('DOGE', 20, (255, 255, 255), 70, 40)
            self.draw_text('WOW POINT: {}'.format(self.player.score), 20, (255, 255, 255), 70, 70)
        else:
            self.draw_text('PLAYER 1', 20, (255,255,255), 70, 40)
            self.draw_text('%06d' % self.player.score, 22, (255,255,255), 80, 65)
            self.draw_text('WORLD', 20, (255, 255, 255), 415, 40)
            self.draw_text('1-1', 22, (255, 255, 255), 430, 65)
        if self.speedrun:
            self.draw_text('TIME', 20, (255,255,255), 620, 40)
            self.draw_text('%02d:%02d:%02d' % (self.minute,self.second,self.milisecond), 22, (255,255,255), 570, 65)
        if self.fps == 'ON':
            self.draw_text('%.f' % (g.clock.get_fps()), 20, (255,255,0), 10, 10)
        pg.display.flip()

    def splash(self):
        self.screen.fill((255,255,255))
        # self.screen.blit()  # Fade out
        fade = pg.Surface((screen_width, screen_height))
        fade.fill((255,255,255))
        for alpha in range(0, 300, 3):
            fade.set_alpha(alpha)
            self.screen.blit(pg.image.load('images/logo.png').convert_alpha(), (230, 250))  # Fade in
            self.screen.blit(fade, (0,0))
            pg.display.flip()
            self.wait(1)

    def menu(self):
        global run,start
        self.load()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.run = False
                run = False
                start = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    if self.howtoplay:
                        self.howtoplay = False
                    if self.setting and not self.restart:
                        self.setting = False
                if event.key == pg.K_UP:
                    if self.setting:
                        if self.setting_arrow_pos_y == 277:
                            self.setting_arrow_pos_y = 277
                        else:
                            self.move_fx.play()
                            self.setting_arrow_pos_y -= 40
                    elif self.howtoplay:
                        None
                    elif self.restart:
                        None
                    else:
                        if self.up_counter < 5:
                            if self.menu_arrow_pos_y == 437:
                                self.menu_arrow_pos_y = 437
                                self.up_counter += 1
                            else:
                                self.move_fx.play()
                                self.menu_arrow_pos_y -= 40
                        elif self.up_counter > 4 and self.up_counter < 10:
                            if self.menu_arrow_pos_y == 397:
                                self.menu_arrow_pos_y = 397
                                self.up_counter += 1
                            else:
                                self.move_fx.play()
                                self.menu_arrow_pos_y -= 40
                        elif self.up_counter > 9:
                            if self.menu_arrow_pos_y == 357:
                                self.menu_arrow_pos_y = 357
                                # self.up_counter += 1
                            else:
                                self.move_fx.play()
                                self.menu_arrow_pos_y -= 40
                if event.key == pg.K_DOWN:
                    if self.setting:
                        if self.setting_arrow_pos_y == 357:
                            self.setting_arrow_pos_y = 357
                        else:
                            self.move_fx.play()
                            self.setting_arrow_pos_y += 40
                    elif self.howtoplay:
                        None
                    elif self.restart:
                        None
                    else:
                        if self.menu_arrow_pos_y == 557:
                            self.menu_arrow_pos_y = 557
                        else:
                            self.move_fx.play()
                            self.menu_arrow_pos_y += 40
                if event.key == pg.K_LEFT:
                    if self.restart:
                        self.move_fx.play()
                        self.restart_arrow_pos_x = 202
                if event.key == pg.K_RIGHT:
                    if self.restart:
                        self.move_fx.play()
                        self.restart_arrow_pos_x = 400
                if event.key == pg.K_RETURN:
                    self.select_fx.play()
                    if self.setting and not self.restart:
                        if self.setting_arrow_pos_y == 277:
                            if self.window == 'WINDOWED':
                                self.window_mode = pg.FULLSCREEN
                                self.window = 'FULLSCREEN'
                                setting = open('setting.txt','w')
                                setting.write(str(self.window_mode))
                            elif self.window == 'FULLSCREEN':
                                self.window_mode = 0
                                self.window = 'WINDOWED'
                                setting = open('setting.txt', 'w')
                                setting.write(str(self.window_mode))
                            self.restart_arrow_pos_x = 202
                            self.restart = True
                        if self.setting_arrow_pos_y == 317:
                            if self.fps == 'ON':
                                self.fps = 'OFF'
                            elif self.fps == 'OFF':
                                self.fps = 'ON'
                        if self.setting_arrow_pos_y == 357:
                            if self.mute == 'ON':
                                self.mute = 'OFF'
                            elif self.mute == 'OFF':
                                self.mute = 'ON'
                    elif self.restart:
                        if self.restart_arrow_pos_x == 202:
                            self.run = False
                            run = False
                            self.restart = False
                        if self.restart_arrow_pos_x == 400:
                            self.restart = False
                            self.next_time = True
                    else:
                        if self.menu_arrow_pos_y == 357:
                            self.start = True
                            self.doge = True
                        if self.menu_arrow_pos_y == 397:
                            self.start = True
                            self.speedrun = True
                        if self.menu_arrow_pos_y == 437:
                            self.start = True
                        if self.menu_arrow_pos_y == 477:
                            self.howtoplay = True
                        if self.menu_arrow_pos_y == 517:
                            self.setting = True
                        if self.menu_arrow_pos_y == 557:
                            self.run = False
                            run = False
                            start = False
            if event.type == pg.KEYUP:
                if event.key == pg.K_UP:
                    None
                if event.key == pg.K_DOWN:
                    None
        if self.up_counter == 5 and not self.secret_unlocked:
            self.secret.play()
            self.secret_unlocked = True
        if self.up_counter > 5 and self.up_counter < 10:
            self.secret_unlocked = False
        if self.up_counter == 10 and not self.secret_unlocked:
            self.wow.play()
            self.secret_unlocked = True
        self.image = pg.image.load('images/bg2.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.screen.blit(pg.transform.scale(self.image, (int(self.rect.width * 3.214), int(self.rect.height * 3.214))), (0, 0))
        if self.menu_arrow_pos_y == 357:
            self.image = pg.image.load('images/dstand.png').convert_alpha()
            self.rect = self.image.get_rect()
            self.screen.blit(pg.transform.scale(self.image, (int(self.rect.width * 2.5), int(self.rect.height * 2.5))),(120, 600))
        else:
            self.image = pg.image.load('images/mario.png').convert_alpha()
            self.rect = self.image.get_rect()
            self.screen.blit(pg.transform.scale(self.image, (int(self.rect.width * 3.214), int(self.rect.height * 3.214))), (120, 594))
        self.image = pg.image.load('images/game-name.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.screen.blit(pg.transform.scale(self.image, (int(self.rect.width * 1.26), int(self.rect.height * 1.26))), (-35, 190))
        if self.up_counter < 5:
            self.draw_text('PLAY GAME', 20, (255,255,255), 300, 460)
        else:
            if self.menu_arrow_pos_y == 397:
                dim = pg.Surface((280,645))
                dim.fill((0,0,0))
                dim.set_alpha(200)
                self.screen.blit(dim,(0,0))
                self.draw_text('SPEEDRUN HIGHSCORE:', 14, (255,255,255), 10, 20)
                i = 0
                rank = 1
                sort = [(a, self.highscore[a]) for a in sorted(self.highscore, key=self.highscore.get)]
                for name,time in sort:
                    self.draw_text('{}.{} {}'.format(rank, name, time), 12, (255,255,255), 20, 60+i)
                    i += 20
                    rank += 1
            self.draw_text('SPEEDRUN MODE', 20, (255,255,255), 300, 420)
            self.draw_text('NORMAL MODE', 20, (255,255,255), 300, 460)
            if self.up_counter > 9:
                self.draw_text('WOW MODE', 20, (255, 255, 255), 300, 380)
        self.draw_text('HOW TO PLAY', 20, (255,255,255), 300, 500)
        self.draw_text('OPTIONS', 20, (255,255,255), 300, 540)
        self.draw_text('QUIT', 20, (255,255,255), 300, 580)
        self.image = pg.image.load('images/arrow.gif').convert_alpha()
        self.rect = self.image.get_rect()
        self.screen.blit(pg.transform.scale(self.image, (int(self.rect.width * 1), int(self.rect.height * 1))), (240, self.menu_arrow_pos_y))
        if self.howtoplay:
            dim = pg.Surface((screen_width,screen_height))
            dim.fill((0,0,0))
            dim.set_alpha(225)
            self.screen.blit(dim,(0,0))
            self.image = pg.image.load('images/mario.png').convert_alpha()
            self.rect = self.image.get_rect()
            self.screen.blit(pg.transform.scale(self.image, (int(self.rect.width * 3.214), int(self.rect.height * 3.214))), (120, 594))
            for text in texts:
                self.draw_text(*text)
            self.image = pg.image.load('images/a.png').convert_alpha()
            self.rect = self.image.get_rect()
            self.screen.blit(pg.transform.scale(self.image, (int(self.rect.width * 1.5), int(self.rect.height * 1.5))), (375, 300))
            self.image = pg.image.load('images/d.png').convert_alpha()
            self.rect = self.image.get_rect()
            self.screen.blit(pg.transform.scale(self.image, (int(self.rect.width * 1.5), int(self.rect.height * 1.5))), (425, 300))
            self.image = pg.image.load('images/left.png').convert_alpha()
            self.rect = self.image.get_rect()
            self.screen.blit(pg.transform.scale(self.image, (int(self.rect.width * 1.5), int(self.rect.height * 1.5))), (250, 300))
            self.image = pg.image.load('images/right.png').convert_alpha()
            self.rect = self.image.get_rect()
            self.screen.blit(pg.transform.scale(self.image, (int(self.rect.width * 1.5), int(self.rect.height * 1.5))), (300, 300))
            self.image = pg.image.load('images/up.png').convert_alpha()
            self.rect = self.image.get_rect()
            self.screen.blit(pg.transform.scale(self.image, (int(self.rect.width * 1.5), int(self.rect.height * 1.5))), (175, 380))
            self.image = pg.image.load('images/space.png').convert_alpha()
            self.rect = self.image.get_rect()
            self.screen.blit(pg.transform.scale(self.image, (int(self.rect.width * 1.5), int(self.rect.height * 1.5))), (250, 380))
            self.image = pg.image.load('images/bubble.png').convert_alpha()
            self.rect = self.image.get_rect()
            self.screen.blit(pg.transform.scale(self.image, (int(self.rect.width * 0.5), int(self.rect.height * 0.5))), (65, 525))
            self.box = pg.Rect((50, 185), (140, 30))
            if self.box.collidepoint(pg.mouse.get_pos()):
                if pg.event.get([pg.MOUSEBUTTONDOWN]):
                    self.howtoplay = False
        if self.setting:
            dim = pg.Surface((screen_width,screen_height))
            dim.fill((0,0,0))
            dim.set_alpha(225)
            self.screen.blit(dim,(0,0))
            for text in [('< BACK',20,(255,255,255),40,200),
                         ('OPTIONS',20,(255,255,255),320,250),
                         ('WINDOW MODE: {}'.format(self.window),20,(255,255,255),180,300),
                         ('SHOW FPS: {}'.format(self.fps),20,(255,255,255),180,340),
                         ('MUTE SOUND: {}'.format(self.mute),20,(255,255,255),180,380)]:
                self.draw_text(*text)
            if self.next_time:
                self.draw_text('SETTING WILL TAKE EFFECT THE NEXT TIME YOU OPEN THE GAME.',20,(255,255,255),self.text_pos_x,480)
                if self.text_pos_x > -1140:
                    self.text_pos_x -= 15
                else:
                    self.text_pos_x = 840
            self.image = pg.image.load('images/arrow.gif').convert_alpha()
            self.rect = self.image.get_rect()
            self.screen.blit(pg.transform.scale(self.image, (int(self.rect.width * 1), int(self.rect.height * 1))), (120, self.setting_arrow_pos_y))
            self.box = pg.Rect((50, 185), (140, 30))
            if self.box.collidepoint(pg.mouse.get_pos()):
                    if pg.event.get([pg.MOUSEBUTTONDOWN]):
                        self.setting = False
            if self.restart:
                self.screen.blit(dim, (0, 0))
                for text in [('RESTART THE GAME NOW?', 20, (255, 255, 255), 185, 320),
                             ('YES', 20, (255, 255, 255), 260, 380),
                             ('NO', 20, (255, 255, 255), 460, 380)]:
                    self.draw_text(*text)
                self.image = pg.image.load('images/arrow.gif').convert_alpha()
                self.rect = self.image.get_rect()
                self.screen.blit(pg.transform.scale(self.image, (int(self.rect.width * 1), int(self.rect.height * 1))),(self.restart_arrow_pos_x, 357))
        pg.display.flip()

    def game_over(self):
        self.screen.fill((0,0,0))
        self.draw_text('x {}'.format(str(self.lives)), 22, (255,255,255), 380, 370)
        if self.doge:
            self.image = pg.image.load('images/dstand.png').convert_alpha()
            self.rect = self.image.get_rect()
            self.screen.blit(pg.transform.scale(self.image, (int(self.rect.width * 2.5), int(self.rect.height * 2.5))),(305, 355))
        else:
            self.image = pg.image.load('images/mario.png').convert_alpha()
            self.rect = self.image.get_rect()
            self.screen.blit(pg.transform.scale(self.image, (int(self.rect.width * 3.214), int(self.rect.height * 3.214))), (310, 350))
        pg.display.flip()
        self.wait(1600)

    def win(self):
        self.screen.fill((0,0,0))
        if self.doge:
            self.draw_text('wow, you beat the game...', 20, (255, 255, 255), 140, screen_height / 2)
            pg.display.flip()
            self.wait(3000)
        else:
            self.draw_text('Congratulation, you beat level 1...', 20, (255,255,255), 40, screen_height/2)
            pg.display.flip()
            self.wait(3000)
            self.screen.fill((0,0,0))
            if 3-self.lives == 0:
                self.draw_text('You didn\'t even die!'.format(3 - self.lives), 20, (255, 255, 255), 190, screen_height / 2)
            else:
                self.draw_text('You died: {} times'.format(3-self.lives), 20, (255, 255, 255), 220, screen_height / 2)
            pg.display.flip()
            self.wait(3000)
            self.screen.fill((0, 0, 0))
            self.draw_text('(Now, try to press up 5 times in menu)', 19, (255,255,255), 26, screen_height/2)
            pg.display.flip()
            self.wait(5000)
        self.lives = 3
        self.checkpoint = False
        self.music = False
        self.doge = False
        self.true_finish = False

    def prize(self):
        self.lives = 3
        self.checkpoint = False
        self.music = False
        self.speedrun = False
        wait = True
        name = ''
        dim = pg.Surface((screen_width,screen_height))
        dim.fill((0,0,0))
        dim.set_alpha(10)
        while wait:
            self.screen.blit(dim,(0,0))
            self.draw_text('Your time:', 28, (255,255,255), 245, 220)
            self.draw_text('%02d:%02d:%02d' % (self.minute,self.second,self.milisecond), 42, (255,255,255), 215, 270)
            self.draw_text('Your name:', 18, (255,255,255), 75, 400)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    wait = False
                    self.run = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.draw_text('Try enter.', 24, (255,255,255), 280, 550)
                    if event.key == pg.K_BACKSPACE:
                        if len(name) > 0:
                            name = name[:-1]
                    if event.key == pg.K_SPACE:
                        if len(name) < 8:
                            name += '_'
                        else:
                            self.draw_text('8 characters max.', 24, (255,255,255), 200, 550)
                    if event.key == pg.K_RETURN:
                        if len(name) == 0:
                            self.draw_text('Enter your name first', 24, (255, 255, 255), 140, 550)
                        else:
                            self.highscore[name] = '%02d:%02d:%02d' % (self.minute,self.second,self.milisecond)
                            file = open('highscore.txt','w')
                            for nama, time in self.highscore.items():
                                data = nama+' '+time+'\n'
                                file.write(data)
                            wait = False
                    if not event.key == pg.K_ESCAPE and not event.key == pg.K_BACKSPACE and not event.key == pg.K_SPACE and not event.key == pg.K_RETURN:
                        if len(name) < 8:
                            name += event.unicode
                        else:
                            self.draw_text('8 characters max.', 24, (255,255,255), 200, 550)
                    self.draw_text(pg.key.name(event.key), 18, (255,255,255), 75, 360)
            self.draw_text(name, 18, (255,255,255), 75, 440)
            pg.display.update()
        self.true_finish = False
        self.minute = 0
        self.second = 0
        self.milisecond = 0

    def wait(self, time):
        self.waits = True
        while self.waits:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.waits = False
                    self.run = False
                if event.type == pg.KEYUP:
                    self.waits = False
            pg.time.wait(time)
            self.waits = False

    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font('font.ttf', size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.x,text_rect.y = x, y
        self.screen.blit(text_surface, text_rect)

start = True
run = True
while start:
    run = True
    while run:
        g = Game()
        g.run_the_game()

pg.quit()
