import pygame

BLACK = (0,0,0)


class Brick(pygame.sprite.Sprite):
    """
    Brick
    """
    def __init__(self, color, width, heigth):
        super().__init__()

        self.image = pygame.Surface([width, heigth])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, width, heigth])

        self.rect = self.image.get_rect()
