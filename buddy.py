import pygame
from pypresence import Presence
import time
import random
import win32gui
import win32con
import win32api
rpc = Presence("1225535870199795782")
rpc.connect()
rpc.update(state="Playing with buddy",details = "Having fun", large_image="slime_smile2")

Affection = 50
food_amount_max = 100
pygame.init()
window_width = 100
window_height = 70
screen = pygame.display.set_mode((window_width, window_height))
loop = 0
backround_image = pygame.image.load("pixelworld.png")
backround_image = pygame.transform.scale(backround_image, (120, 90))
screen.blit(backround_image, (-5, -20))
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
pygame.display.update()

food_level = 10
PLACEHOLDER = "slime.png"
heart = "heart.png"
slime_smile = "slime_smile.png"
slime_smile2 = "slime_smile2.png"
slime_eating = "slime_eat1.png"
slime_neutral = "slime.png"
slime_mouth_closed = "slime_eat2.png"
full_icon = "FULLicon.png"
slime_smile2_gold = "Slime_Smile2_Gold.png"
red_box = "redbox.png"
blank = "blank.png"

hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

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
            screen.blit(backround_image, (-5, -20))
            screen.blit(Slime, (slimex, slimey))
            pygame.display.update()
            time.sleep(0.25)
            print("Smile 2")
            Slime = pygame.image.load(slime_smile2).convert_alpha()
            Slime = pygame.transform.scale(Slime, (50, 40))
            screen.blit(backround_image, (-5, -20))
            screen.blit(Slime, (slimex, slimey))
            pygame.display.update()
            time.sleep(0.5)
            print("slime normal")
            Slime = pygame.image.load(slime_neutral).convert_alpha()
            Slime = pygame.transform.scale(Slime, (50, 40))
            screen.blit(backround_image, (-5, -20))
            screen.blit(Slime, (slimex, slimey))
            pygame.display.update()
            action = False
            Affection += 10
            print("Affection increased by 10")
    
    if Affection >= 100:
        print("Slime is very happy!")
        slime_neutral = "slime_smile2.png"
        pygame.display.update()
    else:
        slime_neutral = "slime.png"
        pygame.display.update()

    if Affection < 100:
        Slime = pygame.image.load(slime_neutral).convert_alpha()
        Slime = pygame.transform.scale(Slime, (50, 40))
        screen.blit(backround_image, (-5, -20))
        screen.blit(Slime, (slimex, slimey))
        pygame.display.update()
    
    
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
        action = True
        if 27 < mouse_pos[0] < 77 and 35 < mouse_pos[1] < 75:
            if food_level > food_amount_max:
                print("FULL")
                Fullicon = pygame.image.load(full_icon).convert_alpha()
                Fullicon = pygame.transform.scale(Fullicon, (60, 20))
                screen.blit(Fullicon, (slimex, slimey - 30))
                pygame.display.update()
                time.sleep(1)
                screen.blit(backround_image,(-5, -20))
                screen.blit(Slime,(slimex, slimey))
                pygame.display.update()
            else:
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
                if food_level < food_amount_max:
                    food_level += 10

    if food_level < 0:
        print("Slime is hungry!")
        break
        
    if Affection < 0:
        print("Slime is sad")
        break

    if food_level < 20:
        print("Slime getting hungry!")
        low_FA = pygame.image.load(red_box).convert_alpha()
        screen.blit(low_FA, (slimex - 27, slimey - 35))

        
    if Affection < 20:
        print("Slime is getting sad...")
        low_FA = pygame.image.load(red_box).convert_alpha()
        screen.blit(low_FA, (slimex - 27, slimey - 35))

    food_level -= 0.001
    print(food_level)
    Affection -= 0.001
    print(Affection)

    pygame.display.flip()
pygame.time.delay(10)