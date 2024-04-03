import pygame
import time
pygame.init()

window_width = 100
window_height = 70
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Buddy")
clock = pygame.time.Clock()
running = True
Slime = pygame.image.load("slime.png").convert_alpha()
Slime = pygame.transform.scale(Slime, (50, 40))
screen.blit(Slime, (27, 35))
pygame.display.set_icon(Slime)
font = pygame.font.Font(None, 5)
BLACK = (0, 0, 0)


while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if 27 < mouse_pos[0] < 77 and 35 < mouse_pos[1] < 75:
                print("slime clicked")
                Slime = pygame.image.load("slime_smile.png").convert_alpha()
                Slime = pygame.transform.scale(Slime, (50, 40))
                screen.blit(Slime, (27, 35))
                pygame.display.update()
                time.sleep(1)
                print("slime smiling")
                Slime = pygame.image.load("slime.png").convert_alpha()
                Slime = pygame.transform.scale(Slime, (50, 40))
                screen.blit(Slime, (27, 35))
                pygame.display.update()
        
                
    pygame.display.flip()