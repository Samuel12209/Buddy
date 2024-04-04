import pygame
import time
import random
pygame.init()

random_number = random.randint(1, 5)
window_width = 100
window_height = 70
screen = pygame.display.set_mode((window_width, window_height))
BLACK = (0, 0, 0)
screen.fill(BLACK)
loop = 0
pygame.display.set_caption("Buddy")
clock = pygame.time.Clock()
slimex, slimey = 27, 35
Slime = pygame.image.load("assets\slime.png").convert_alpha()
pygame.display.set_icon(Slime)
screen.fill(BLACK)
action = False
print("slime smile")
Slime = pygame.image.load("assets\slime.png").convert_alpha()
Slime = pygame.transform.scale(Slime, (50, 40))
screen.fill(BLACK)
screen.blit(Slime, (slimex, slimey))
pygame.display.update()

PLACEHOLDER = "assets\slime.png"
heart = "assets\heart.png"
slime_smile = "assets\slime_smile.png"
slime_eating = "assets\slime_eat1.png"
slime_neutral = "assets\slime.png"
slime_mouth_closed = "assets\slime_eat2.png"

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    mouse_pos = pygame.mouse.get_pos()

    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        action = True
        if 27 < mouse_pos[0] < 77 and 35 < mouse_pos[1] < 75:
            print("slime smile")
            Slime = pygame.image.load(slime_smile).convert_alpha()
            Slime = pygame.transform.scale(Slime, (50, 40))
            screen.fill(BLACK)
            screen.blit(Slime, (slimex, slimey))
            pygame.display.update()
            print("slime normal")
            Slime = pygame.image.load(slime_neutral).convert_alpha()
            Slime = pygame.transform.scale(Slime, (50, 40))
            screen.fill(BLACK)
            screen.blit(Slime, (slimex, slimey))
            pygame.time.delay(1000)
            pygame.display.update()
            action = False

    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
        action = True
        if 27 < mouse_pos[0] < 77 and 35 < mouse_pos[1] < 75:
            print("Feeding")
            Slime = pygame.image.load(slime_eating).convert_alpha()
            Slime = pygame.transform.scale(Slime, (50, 40))
            screen.blit(Slime, (slimex, slimey))
            pygame.display.update()
            time.sleep(1)
            Slime = pygame.image.load(slime_mouth_closed).convert_alpha()
            Slime = pygame.transform.scale(Slime, (50, 40))
            screen.blit(Slime, (slimex, slimey))
            pygame.display.update()
            time.sleep(1)
            Slime =  pygame.image.load(slime_neutral).convert_alpha()
            Slime = pygame.transform.scale(Slime, (50, 40))
            screen.blit(Slime, (slimex, slimey))
            pygame.display.update()


pygame.display.update()
pygame.time.delay(10)
pygame.display.flip()