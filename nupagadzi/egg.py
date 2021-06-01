import pygame

EGG_COLOR = (149, 217, 218)
BLACK = (0, 0, 0)
EGG_RADIUS = 20

class Egg(pygame.sprite.Sprite):
    """Egg sprite"""

    def __init__(self, position):
        super().__init__()

        self.image = pygame.Surface([EGG_RADIUS * 2, EGG_RADIUS*2])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.circle(self.image, EGG_COLOR, (EGG_RADIUS, EGG_RADIUS), EGG_RADIUS)

        self.rect = self.image.get_rect()

        # Positioning according to position
        if position == 'LU':
            self.rect.x = EGG_RADIUS
            self.rect.y = 100 - EGG_RADIUS

        if position == 'LD':
            self.rect.x = EGG_RADIUS
            self.rect.y = 300 - EGG_RADIUS

        if position == 'RU':
            self.rect.x = 800 - EGG_RADIUS
            self.rect.y = 100 - 2 * EGG_RADIUS

        if position == 'RD':
            self.rect.x = 800 - EGG_RADIUS
            self.rect.y = 300 - 2 * EGG_RADIUS


        # Velocity based on position
        if position == 'LU' or position == 'LD':
            self.velocity = [6, 2]

        if position == 'RU' or position == 'RD':
            self.velocity = [-6, 2]


    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        if self.rect.x > 220 and self.rect.x < 550 and self.rect.y < 460:
            self.rect.y = 500
            self.velocity = [0, 10]