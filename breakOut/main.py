import pygame
from paddle import Paddle
from ball import Ball
from brick import Brick

pygame.init()

#Global colors
WHITE = (255,255,255)
DARKBLUE = (0,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
ORANGE = (255,100,0)
YELLOW = (255,255,0)

COLOR_LIST = [RED, ORANGE, YELLOW, LIGHTBLUE]

score = 0
lives = 3

# Open new window
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout Game")

# List containing all the sprites
all_sprites_list = pygame.sprite.Group()

# Create Paddle
paddle = Paddle(LIGHTBLUE, 100, 10)
paddle.rect.x = 350
paddle.rect.y = 560

# Create Ball
ball = Ball(WHITE,10,10)
ball.rect.x = 400
ball.rect.y = 540

# Create Bricks
all_bricks = pygame.sprite.Group()

for j in range(3):
    for i in range(7):
        brick = Brick(COLOR_LIST[j], 80, 30)
        brick.rect.x = 60 + i*100
        if j == 0:
            brick.rect.y = 60
        elif j == 1:
            brick.rect.y = 100
        elif j == 2:
            brick.rect.y = 140
        all_sprites_list.add(brick)
        all_bricks.add(brick)


# Add paddle to the sprite list
all_sprites_list.add(paddle)
all_sprites_list.add(ball)

# LoopStopper
carryOn = True

# Clock to controll FPS
clock = pygame.time.Clock()

# Main Loop

while carryOn:
    # Quit Game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                carryOn = False

    # Moving Paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        paddle.moveRight(5)

    # ---Game Logic
    all_sprites_list.update()

    # Check if the ball is bouncing against any of the 4 walls:
    if ball.rect.x >= 790:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y > 590:
        ball.velocity[1] = -ball.velocity[1]
        lives -= 1
        if lives == 0:
            # Game over for 5 seconds
            font = pygame.font.Font(None, 74)
            text = font.render("GAME OVER", 1, WHITE)
            screen.blit(text,(250,300))
            pygame.display.flip()
            pygame.time.wait(3000)

            # Stopper:
            carryOn = False
    if ball.rect.y < 40:
        ball.velocity[1] = -ball.velocity[1]

    # Detect collision between the ball and the paddle
    if pygame.sprite.collide_mask(ball, paddle):
        ball.rect.x -= ball.velocity[0]
        ball.rect.y -= ball.velocity[1]
        ball.bouncePaddle()

    # Collision between ball and bricks
    brick_collision_list = pygame.sprite.spritecollide(ball, all_bricks, False)
    for brick in brick_collision_list:
        ball.bounceBrick()
        score += 1
        brick.kill()
        if len(all_bricks) == 0:
            # Display win message for 3 seconds
            font = pygame.font.Font(None, 74)
            text = font.render("LEVEL COMPLETE", 1, WHITE)
            screen.blit(text, (200,300))
            pygame.display.flip()
            pygame.time.wait(3000)

            carryOn = False

    # ---Drawing code
    # First, clear the screen to dark blue.
    screen.fill(DARKBLUE)
    pygame.draw.line(screen, WHITE, [0, 38], [800, 38], 2)

    # Display the score and the number of lives at the top of the screen
    font = pygame.font.Font(None, 34)
    text = font.render("Score: " + str(score), 1, WHITE)
    screen.blit(text, (20, 10))
    text = font.render("Lives: " + str(lives), 1, WHITE)
    screen.blit(text, (650, 10))

    #  Draw all sprites to the screen
    all_sprites_list.draw(screen)

    # Screen update screen with what we've drawn
    pygame.display.flip()

    # 60 fps
    clock.tick(60)


pygame.quit()
