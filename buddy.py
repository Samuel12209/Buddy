import pygame
import time
import random
pygame.init()

food_amount_max = 100
random_number = random.randint(1, 5)
window_width = 100
window_height = 70
screen = pygame.display.set_mode((window_width, window_height))
loop = 0
backround_image = pygame.image.load("pixelworld.png")
screen.blit(backround_image, (-5, -30))
pygame.display.set_caption("Buddy")
clock = pygame.time.Clock()
slimex, slimey = 27, 35
Slime = pygame.image.load("slime.png").convert_alpha()
pygame.display.set_icon(Slime)
action = False
print("slime smile")
Slime = pygame.image.load("slime.png").convert_alpha()
Slime = pygame.transform.scale(Slime, (50, 40))
screen.blit(Slime, (slimex, slimey))
foodicon = pygame.image.load("minecraft_hunger icon.png").convert_alpha()
foodicon = pygame.transform.scale(foodicon, (25, 20))
screen.blit(foodicon, (3, 3))
pygame.display.update()

PLACEHOLDER = "slime.png"
heart = "heart.png"
slime_smile = "slime_smile.png"
slime_smile2 = "slime_smile2.png"
slime_eating = "slime_eat1.png"
slime_neutral = "slime.png"
slime_mouth_closed = "slime_eat2.png"
food_icon = "minecraft_hunger icon.png"


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
            screen.blit(backround_image, (-5, -30))
            screen.blit(Slime, (slimex, slimey))
            pygame.display.update()
            time.sleep(0.25)
            print("Smile 2")
            Slime = pygame.image.load(slime_smile2).convert_alpha()
            Slime = pygame.transform.scale(Slime, (50, 40))
            screen.blit(backround_image, (-5, -30))
            screen.blit(Slime, (slimex, slimey))
            pygame.display.update()
            time.sleep(0.5)
            print("slime normal")
            Slime = pygame.image.load(slime_neutral).convert_alpha()
            Slime = pygame.transform.scale(Slime, (50, 40))
            screen.blit(backround_image, (-5, -30))
            screen.blit(Slime, (slimex, slimey))
            pygame.display.update()
            action = False

    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
        action = True
        if 27 < mouse_pos[0] < 77 and 35 < mouse_pos[1] < 75:
            print("Feeding")
            Slime = pygame.image.load(slime_smile2).convert_alpha()
            Slime = pygame.transform.scale(Slime, (50, 40))
            screen.blit(Slime, (slimex, slimey))
            pygame.display.update()
            time.sleep(1)
            Slime = pygame.image.load(slime_eating).convert_alpha()
            slime = pygame.transform.scale(Slime, (50, 40))
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