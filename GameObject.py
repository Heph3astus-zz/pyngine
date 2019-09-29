import pygame
import os
class staticGameObject:
    change = False
    posx = 0
    posy = 0
    sprite = "default.png"
    spriteImg = None

    def __init__(self):
        self.spriteImg = pygame.image.load("assets/" + self.sprite)

class physicsGameObject:

    posx = 0
    posy = 0
    vx = 0
    vy = 0
    sprite = "/path/to/sprite"
    spriteImg = None
    physicsBody = "Define Later"

    def __init__(self):
        self.spriteImg = pygame.image.load('../' + self.sprite)

    def move():
        self.posx += self.vx
        self.posy += self.vy
