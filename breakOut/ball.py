from random import randint
import pygame

BLACK = (0,0,0)


class Ball(pygame.sprite.Sprite):
    """
    Ball
    """

    def __init__(self, color, width, height):
        super().__init__()

        # Set ball color, width, height
        # Set the background color and make it transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draw the ball (a rectangle)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.velocity = [randint(-8, 8), randint(-8, -4)]

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()


    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]


    def bouncePaddle(self):
        self.velocity[1] = randint(-8, -5)

    
    def bounceBrick(self):
        self.velocity[1] = randint(5, 8)
