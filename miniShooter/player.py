import pygame
import math

BLACK = (0,0,0)
PLAYER_COLOR = (85, 80, 92)
BULLET_COLOR = (199, 80, 0)
RADIUS = 20
PLAYER_IMAGE = pygame.image.load("images/player.png")
BULLET_VELOCITY = 15


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Making background and making it transparent
        self.image = pygame.Surface([RADIUS * 2, RADIUS * 2])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Drawing circle
        #pygame.draw.circle(self.image, PLAYER_COLOR, (RADIUS, RADIUS), RADIUS)
        self.rect = self.image.get_rect()


    # MOVING

    def moveUp(self):
        self.rect.y -= 8
        if self.rect.y < 0:
            self.rect.y = 600 - RADIUS
    
    
    def moveRight(self):
        self.rect.x += 8
        if self.rect.x > 800:
            self.rect.x = -RADIUS


    def moveDown(self):
        self.rect.y += 8
        if self.rect.y > 600:
            self.rect.y = -RADIUS
    
    
    def moveLeft(self):
        self.rect.x -= 8
        if self.rect.x < 0:
            self.rect.x = 800 - RADIUS


class Aim(pygame.sprite.Sprite):
    def __init__(self, player_pos, mouse_pos):
        super().__init__()

        self.image = pygame.Surface([800, 600])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.line(self.image, PLAYER_COLOR, (player_pos[0] + 20, player_pos[1] + 20), mouse_pos, 2 )

        self.rect = self.image.get_rect()


class Shoot(pygame.sprite.Sprite):
    def __init__(self, player_pos, mouse_pos):
        super().__init__()

        self.image = pygame.Surface([10, 10])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, BULLET_COLOR, [0,0, 10,10])
        self.rect = self.image.get_rect()

        self.rect.x = player_pos[0] + RADIUS
        self.rect.y = player_pos[1] + RADIUS

        # Velocity counter
        x1 = mouse_pos[0] - player_pos[0]
        y1 = mouse_pos[1] - player_pos[1]

        z = x1 *x1 + y1 *y1
        a = z / (BULLET_VELOCITY * BULLET_VELOCITY)  # Devide by bv^2 because z is already ^2

        self.velocity = [x1 / math.sqrt(a), y1 / math.sqrt(a)]
    
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]