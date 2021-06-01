import pygame

BASCKET_COLOR = (73, 53, 72)
BASCKET_WIDTH = 80
BASCKET_HEIGHT = 90


class Bascket(pygame.sprite.Sprite):
    """Bascket sprite"""

    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([BASCKET_WIDTH, BASCKET_HEIGHT])
        self.image.fill((0,0,0))
        self.image.set_colorkey((0,0,0))

        pygame.draw.rect(self.image, BASCKET_COLOR, [0, 0, BASCKET_WIDTH, BASCKET_HEIGHT])

        self.rect = self.image.get_rect()
        self.rect.x = 190
        self.rect.y = 360


    def moveUp(self):
        if self.rect.y == 360:
            self.rect.y = 170


    def moveDown(self):
        if self.rect.y == 170:
            self.rect.y = 360


    def moveLeft(self):
        if self.rect.x == 610 - BASCKET_WIDTH:
            self.rect.x = 190


    def moveRight(self):
        if self.rect.x == 190:
            self.rect.x = 610 - BASCKET_WIDTH
