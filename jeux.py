import math

import pygame
from pygame.math import Vector2

import core
from asteroide import Asteroide
from vaisseaux import Vaisseaux

def setup():
    print("-------START--------")
    core.fps = 20
    core.WINDOW_SIZE = [800,800]

    #creation creep

    core.memory("asteroide",[])

    core.memory("nbAsteroide",50)

    for i in range(0,core.memory("nbAsteroide")):
        core.memory("asteroide").append(Asteroide())



    core.memory("vaisseaux",[])

    core.memory("nbVaisseaux",1)

    for i in range(0,core.memory("nbVaisseaux")):
        core.memory("vaisseaux").append(Vaisseaux())


    print("Setup END-----------")

def run():
    core.cleanScreen()
    for c in core.memory("asteroide"):
        c.show()

    dX, dY = pygame.mouse.get_pos()

    for c in core.memory("vaisseaux"):
        c.show()









core.main(setup, run)