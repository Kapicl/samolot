import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60
SPEED = 5

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Два самолёта")

bg = pygame.image.load("back.jpg")
plane1 = pygame.image.load("plane1.png")  # Самолёт (клавиатура)
plane2 = pygame.image.load("plane2.png")  # Самолёт (мышь)

plane1_rect = plane1.get_rect()
plane2_rect = plane2.get_rect()

plane1_rect.topleft = (100, 250)
plane2_rect.topleft = (500, 250)

running = True
clock = pygame.time.Clock()
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and plane1_rect.left > 0:
        plane1_rect.x -= SPEED
    if keys[pygame.K_RIGHT] and plane1_rect.right < WIDTH:
        plane1_rect.x += SPEED
    if keys[pygame.K_UP] and plane1_rect.top > 0:
        plane1_rect.y -= SPEED
    if keys[pygame.K_DOWN] and plane1_rect.bottom < HEIGHT:
        plane1_rect.y += SPEED

    mouse_x, mouse_y = pygame.mouse.get_pos()
    plane2_rect.center = (mouse_x, mouse_y)

    screen.blit(bg, (0, 0))
    screen.blit(plane1, plane1_rect)
    screen.blit(plane2, plane2_rect)
    pygame.display.flip()

pygame.quit()
