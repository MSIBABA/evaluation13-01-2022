import random

import pygame
from pygame.math import Vector2

import core

class Vaisseaux:
    def __init__(self):
        self.debug = False
        self.pos = (400,400)
        self.vel = Vector2(random.uniform(-5, 5), random.uniform(-5, 5))
        self.acc = Vector2()
        self.maxAcc = 1
        self.maxSpeed = 6
        self.perception = 80
        self.freeze = False
        self.prey = None
        self.huntFactor = 0.4
        self.alignFactor = 0.1
        self.cohesionFactor = 2
        self.color = (255,255,255)
        self.taille = 10
        self.masse = 5



    def show(self):
        a = 0 - self.vel.angle_to(Vector2(0, 1))

        p1 = self.pos + Vector2(-5, 0).rotate(a)
        p2 = self.pos + Vector2(0, 15).rotate(a)
        p3 = self.pos + Vector2(5, 0).rotate(a)

        core.Draw.polygon((255, 0, 0), ((p1), (p2), (p3)))



