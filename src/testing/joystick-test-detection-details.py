import pygame
pygame.init()
j = pygame.joystick.Joystick(0)
j.init()
joycount = pygame.joystick.get_count()
joy = j.get_name()
print joycount
print joy
