import pygame
pygame.init()

window_width = 100
window_height = 70
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Buddy Game")
clock = pygame.time.Clock()
running = True
Slime = pygame.image.load("slime.png")
Slime = pygame.transform.scale(Slime, (50, 40))
screen.blit(Slime, (27, 35))
button = pygame.Rect(100, 100, 100, 50)



while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            print(mouse_pos)

    pygame.display.flip()