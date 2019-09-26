import pygame

class staticGameObject:
    change = False
    posx = 0
    posy = 0
    sprite = "/path/to/sprite"

    def process():
        print("collide")

class physicsGameObject:
    posx = 0
    posy = 0
    vx = 0
    vy = 0
    sprite = "/path/to/sprite"
    physicsBody = "Define Later"

    def process():
        move()
        collide()


    def move():
        posx += vx
        posy += vy

    def collide():
        print("collide")
