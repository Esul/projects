import pygame


BLACK = (0,0,0)


class Paddle(pygame.sprite.Sprite):
    """
    Paddle
    """

    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the paddle and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draw a rectangle -> paddle
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Fetch the rectangle object that has the same dimensions of the image.
        self.rect = self.image.get_rect()

    def moveLeft(self, pixels):
        self.rect.x -= pixels
        if self.rect.x < 0:
            self.rect.x = 0

    def moveRight(self, pixels):
        self.rect.x += pixels
        if self.rect.x > 700:
            self.rect.x = 700
