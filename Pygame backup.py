import pygame
from pygame import *
import os
# from Player import Mario

# player = Mario

current_path = os.path.dirname(__file__)
image = os.path.join(current_path, 'images')
sound = os.path.join(current_path, 'sound')
pygame.init()  # initialize pygame, always do this first.
clock = pygame.time.Clock()
FPS = 60

screen_width = 768
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_icon(pygame.image.load(os.path.join(image, "mario.png")).convert_alpha())


class Mario:

    mario = pygame.image.load(os.path.join(image, 'mario.png')).convert_alpha()
    rect = mario.get_rect()
    mario = pygame.transform.scale(mario, (int(rect.width * 3.214), int(rect.height * 3.214)))
    # mario_width, mario_height = mario.get_rect().size
    mario_walk = [pygame.image.load(os.path.join(image, 'walk1.png')).convert_alpha(),
                  pygame.image.load(os.path.join(image, 'walk2.png')).convert_alpha(),
                  pygame.image.load(os.path.join(image, 'walk3.png')).convert_alpha()]
    mario_walk = [pygame.transform.scale(mario_walk[0], (int(rect.width * 3.214), int(rect.height * 3.214))),
                  pygame.transform.scale(mario_walk[1], (int(rect.width * 3.214), int(rect.height * 3.214))),
                  pygame.transform.scale(mario_walk[2], (int(rect.width * 3.214), int(rect.height * 3.214)))]
    mario_jump = pygame.image.load(os.path.join(image, 'jump.png')).convert_alpha()
    mario_jump = pygame.transform.scale(mario_jump, (int(rect.width * 3.214), int(rect.height * 3.214)))
    mario_dead = pygame.image.load(os.path.join(image, 'dead.png')).convert_alpha()
    mario_dead = pygame.transform.scale(mario_dead, (int(rect.width * 3.214), int(rect.height * 3.214)))

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.accelerate = 0
        self.speed = 0
        self.max_speed = 12.8
        self.jump_state = False
        self.jump_count = 10
        self.fell = False
        self.left = False
        self.was_left = False
        self.right = False
        self.was_right = False
        self.walk_count = 0

    def draw(self, pos):
        self.pos = pos
        self.rect = Rect(self.pos, self.y, self.width, self.height)
        if self.accelerate == -self.max_speed or self.accelerate == self.max_speed:
            if self.walk_count >= 3:
                self.walk_count = 0

            if not self.jump_state:
                if self.left:
                    screen.blit(pygame.transform.flip(self.mario_walk[self.walk_count // 1], True, False),
                                (self.pos, self.y, self.width, self.height))
                    self.walk_count += 1

                elif self.right:
                    screen.blit(self.mario_walk[self.walk_count // 1], (self.pos, self.y, self.width, self.height))
                    self.walk_count += 1

                else:
                    if self.was_left:
                        screen.blit(pygame.transform.flip(self.mario, True, False),
                                    (self.pos, self.y, self.width, self.height))
                    elif self.was_right:
                        screen.blit(self.mario, (self.pos, self.y, self.width, self.height))
                    else:
                        screen.blit(self.mario, (self.pos, self.y, self.width, self.height))

            else:
                if self.was_left:
                    screen.blit(pygame.transform.flip(self.mario_jump, True, False),
                                (self.pos, self.y, self.width, self.height))
                elif self.was_right:
                    screen.blit(self.mario_jump, (self.pos, self.y, self.width, self.height))
                if self.left:
                    screen.blit(pygame.transform.flip(self.mario_jump, True, False),
                                (self.pos, self.y, self.width, self.height))
                elif self.right:
                    screen.blit(self.mario_jump, (self.pos, self.y, self.width, self.height))

        elif player.rect.colliderect(goomba.rect):
            screen.blit(player.mario_dead, player.rect)

        else:
            if self.walk_count >= 9:
                self.walk_count = 0

            if not self.jump_state:
                if self.left:
                    screen.blit(pygame.transform.flip(self.mario_walk[self.walk_count // 3], True, False),
                                (self.pos, self.y, self.width, self.height))
                    self.walk_count += 1

                elif self.right:
                    screen.blit(self.mario_walk[self.walk_count // 3], (self.pos, self.y, self.width, self.height))
                    self.walk_count += 1

                else:
                    if self.was_left:
                        screen.blit(pygame.transform.flip(self.mario, True, False),
                                    (self.pos, self.y, self.width, self.height))
                    elif self.was_right:
                        screen.blit(self.mario, (self.pos, self.y, self.width, self.height))
                    else:
                        screen.blit(self.mario, (self.pos, self.y, self.width, self.height))

            else:
                if self.left:
                    screen.blit(pygame.transform.flip(self.mario_jump, True, False),
                                (self.pos, self.y, self.width, self.height))
                elif self.right:
                    screen.blit(self.mario_jump, (self.pos, self.y, self.width, self.height))
                else:
                    if self.was_left:
                        screen.blit(pygame.transform.flip(self.mario_jump, True, False),
                                    (self.pos, self.y, self.width, self.height))
                    elif self.was_right:
                        screen.blit(self.mario_jump, (self.pos, self.y, self.width, self.height))
                    else:
                        screen.blit(self.mario_jump, (self.pos, self.y, self.width, self.height))

    def jump(self):
        if not self.jump_state:
            fx.small_jump()
            # self.jump_state = True
            # self.left = False
            # self.right = False
            # if self.jump_count >= -10:
            #     neg = 1
            #     if self.jump_count < 0:
            #         neg = -1
            #     self.y -= (self.jump_count ** 2) * 0.5 * neg
            #     self.jump_count -= 1
            # else:
            #     self.jump_state = False
            #     self.jump_count = 10

    def jump_cut(self):
        if self.jump_state:
            if self.y < level.ground:
                self.jump_count = -1
                self.y -= (self.jump_count ** 2) * 0.5 * -1
                self.jump_count -= 1
            elif self.y > level.ground:
                self.y = level.ground
            else:
                self.jump_state = False
                self.jump_count = 10

    def collide(self, coin, coin_list):
        if self.rect.colliderect(coin.rect):
            coin_list.remove(coin)
            fx.coin()


class Enemy:

    goomba_walk = [pygame.image.load(os.path.join(image, 'goomba1.png')).convert_alpha(),
                   pygame.image.load(os.path.join(image, 'goomba2.png')).convert_alpha()]
    rect = goomba_walk[0].get_rect()
    goomba_walk = [pygame.transform.scale(goomba_walk[0], (int(rect.width * 3.214), int(rect.height * 3.214))).convert_alpha(),
                   pygame.transform.scale(goomba_walk[1], (int(rect.width * 3.214), int(rect.height * 3.214))).convert_alpha()]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 1
        self.walk_count = 0

    def draw(self, pos):
        self.rect = Rect(self.x + pos, self.y, self.width, self.height)
        if self.walk_count >= 16:
            self.walk_count = 0

        screen.blit(self.goomba_walk[self.walk_count // 8], self.rect)
        self.walk_count += 1


class Sound:
    def small_jump(self):
        pygame.mixer.music.load(os.path.join(sound, 'small_jump.ogg'))
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(0)

    def coin(self):
        pygame.mixer.music.load(os.path.join(sound, 'coin.ogg'))
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(0)


class Level:
    def __init__(self):
        self.bg = pygame.image.load(os.path.join(image, 'bg2.png')).convert()
        self.rect = self.bg.get_rect()
        self.bg = pygame.transform.scale(self.bg, (int(self.rect.width * 3.214), int(self.rect.height * 3.214)))
        self.rect = self.bg.get_rect()
        self.bg_width, self.bg_height = self.rect.size
        self.ground = screen_height - 128


class Object:
    brick = pygame.image.load(os.path.join(image, 'brick.png')).convert_alpha()
    rect = brick.get_rect()
    brick = pygame.transform.scale(brick, (int(rect.width * 3.214), int(rect.height * 3.214)))
    coin = pygame.image.load(os.path.join(image, 'coin.png')).convert_alpha()
    coin = pygame.transform.scale(coin, (int(rect.width * 3.214), int(rect.height * 3.214)))

    def __init__(self, name, x, y, width, height):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, pos):
        self.rect = Rect(self.x + pos, self.y, self.width, self.height)
        if self.name == 'brick':
            screen.blit(self.brick, self.rect)

        if self.name == 'coin':
            screen.blit(self.coin, self.rect)


level = Level()
player = Mario(100, level.ground, 51, 51)
fx = Sound()
goomba = Enemy(1000, level.ground, 51, 51)
brick = Object('brick', 500, 400, 51, 51)
brick2 = Object('brick', 250, level.ground, 51, 51)
coin = Object('coin', 350, 400, 51, 51)
coin2 = Object('coin', 200, 400, 51, 51)
coin_list = [coin, coin2]
brick_list = [brick, brick2]


def move():
    player.x += player.accelerate
    goomba.x -= goomba.speed


def control():
    global run
    for event in pygame.event.get():  # check anything happening from user/check if user do something.
        if event.type == pygame.QUIT:  # if you pressed the 'x' button on screen.
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()
        # elif event.type == pygame.KEYUP:
        #     if event.key == pygame.K_SPACE:
        #         player.jump_cut()

    keys = pygame.key.get_pressed()  # enable press and hold key.

    if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] or keys[pygame.K_a] and keys[pygame.K_d]:
        player.accelerate = 0
        player.left = False
        player.right = False
        player.walk_count = 0

    elif keys[pygame.K_LEFT] and player.x > 0 or keys[
        pygame.K_a] and player.x > 0:  # press or hold left key, prevent going out of border of the screen.
        if player.accelerate > 0:
            player.accelerate = 0
        else:
            player.speed = -0.5
            player.accelerate += player.speed
        player.left = True
        player.was_left = True
        player.right = False
        player.was_right = False

    elif keys[pygame.K_RIGHT] and player.x < level.bg_width - 51 or keys[
        pygame.K_d] and player.x < level.bg_width - 51:
        if player.accelerate < 0:
            player.accelerate = 0
        else:
            player.speed = 0.5
            player.accelerate += player.speed
        player.left = False
        player.was_left = False
        player.right = True
        player.was_right = True

    # if keys[pygame.K_UP] and y > 0 or keys[pygame.K_w] and y > 0:
    #     y -= speed
    #
    # if keys[pygame.K_DOWN] and y < screen_height or keys[pygame.K_s] and y < screen_height:
    #     y += speed

    else:  # if no keys are held or pressed.
        if player.x < 0:
            player.x = 0
        elif player.x > level.bg_width + 51 + 384:
            player.x = level.bg_width - 51 - 384
        elif player.accelerate < 0 or player.accelerate > 0:
            player.accelerate *= 0.76
        player.left = False
        player.right = False
        player.walk_count = 0

    if not player.fell:
        if keys[pygame.K_SPACE]:
            player.jump_state = True
            player.left = False
            player.right = False
            if player.jump_count >= 0:
                player.y -= (player.jump_count**2) * 0.55 * 1
                player.jump_count -= 1
            else:
                player.fell = True
        else:
            player.jump_count = -1
            player.fell = True
    else:
        if player.y < level.ground:
            player.y -= (player.jump_count**2) * 0.55 * -1
            player.jump_count -= 1

        elif player.y > level.ground:
            player.y = level.ground

        else:
            player.jump_state = False
            player.jump_count = 10
            player.fell = False

    if player.accelerate <= -player.max_speed:
        player.accelerate = -player.max_speed

    elif player.accelerate >= player.max_speed:
        player.accelerate = player.max_speed


def camera():
    global mario, character_pos_x, coin_list, brick_list
    stage_width = level.bg_width
    start_scroll = screen_width / 2
    character_width = 51
    character_pos_x = character_width
    player_pos_x = character_width
    stage_pos_x = 0
    speed = player.x

    player_pos_x += speed
    if player_pos_x < start_scroll:  # create start
        character_pos_x = player_pos_x

    elif player_pos_x > stage_width - start_scroll:  # create end
        character_pos_x = player_pos_x - stage_width + screen_width
        stage_pos_x += -stage_width + start_scroll + 384

    else:  # scrolling bg in middle
        character_pos_x = start_scroll
        stage_pos_x += -speed + start_scroll - 48

    rel_x = stage_pos_x % level.bg_width
    screen.blit(level.bg, (rel_x - level.bg_width, 0))
    if rel_x < screen_width:
        screen.blit(level.bg, (rel_x, 0))

    player.draw(int(character_pos_x))
    goomba.draw(int(stage_pos_x))

    for brick in brick_list:
        # player.collide(brick, brick_list)
        brick.draw(int(stage_pos_x))

    for coin in coin_list:
        player.collide(coin, coin_list)
        coin.draw(int(stage_pos_x))


def screen_update():
    # screen.fill((0,0,0))  # print bg and prevent rectangle overlapping.
    # screen.blit(level.bg, (0,0))
    camera()
    # pygame.draw.rect(screen, (255,0,0), (player.x, y, width, height))  # create a rectangle inside screen, what color, location, and size.
    # pygame.draw.circle
    # pygame.draw.polygon
    move()
    collision()
    pygame.display.set_caption("Super Mario Bros [FPS]: %.2f" % (clock.get_fps()))
    pygame.display.update()  # print changes


def collision():
    if player.rect.colliderect(goomba.rect):
        # goomba.speed = 0
        print('hit')

    elif player.rect.colliderect(brick.rect):
        player.y = brick.y + 60
        print('nope')

    # elif player.rect.bottom.colliderect(goomba.rect.top):
    #     print('ok')

    elif player.rect.colliderect(brick2.rect):
        if player.speed > 0:
            player.y = 400
            player.x = 20
            print('nope')

        if player.speed < 0:
            player.x = 20
            print('nope')


def start_game():
    global run
    run = True
    while run:
        # pygame.time.delay(100)  # give time delay 0.1 second so its not quick A.K.A. LAG.
        clock.tick(FPS)  # every second at most 60 frames should pass.

        control()

        screen_update()

start_game()

pygame.quit()  # end program and close the screen.
