import pygame
import random
import math

ENEMY_RADIUS = 10
ENEMY_COLOR = (255, 255, 255)
ENEMY_VELOCITY = 3
BLACK = (0,0,0)

class Enemy(pygame.sprite.Sprite):

    def __init__(self, player_pos):
        super().__init__()

        self.image = pygame.Surface([ENEMY_RADIUS * 2, ENEMY_RADIUS * 2])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.circle(self.image, ENEMY_COLOR, [ENEMY_RADIUS, ENEMY_RADIUS], ENEMY_RADIUS)

        self.rect = self.image.get_rect()

        x = random.randint(0, 800 - 2 * ENEMY_RADIUS)
        y = random.randint(0, 600 - 2 * ENEMY_RADIUS)
        
        distance = math.sqrt(pow((x + ENEMY_RADIUS - player_pos[0] - 15), 2) + pow((y + ENEMY_RADIUS - player_pos[1] - 15), 2))

        while distance < 30:
            x = random.randint(0, 800 - 2 * ENEMY_RADIUS)
            y = random.randint(0, 600 - 2 * ENEMY_RADIUS)

            distance = math.sqrt(pow((x + ENEMY_RADIUS - player_pos[0] - 15), 2) + pow((y + ENEMY_RADIUS - player_pos[1] - 15), 2))
        
        self.rect.x = x
        self.rect.y = y

        self.last_collision = pygame.time.get_ticks()



    
    def update(self, player_pos):

        #Velocity counter
        x1 = player_pos[0] - self.rect.x
        y1 = player_pos[1] - self.rect.y

        z = x1 *x1 + y1 *y1
        a = z / (ENEMY_VELOCITY * ENEMY_VELOCITY)  # Devide by bv^2 because z is already ^2

        if(a > 0):
            self.velocity = [x1 / math.sqrt(a), y1 / math.sqrt(a)]

        self.rect.x += (self.velocity[0] + random.randint(0,3))
        self.rect.y += (self.velocity[1] + random.randint(0,3))
