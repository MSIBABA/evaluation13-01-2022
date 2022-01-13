import random

import pygame
from pygame.math import Vector2

import core


class Asteroide:
    def __init__(self):
        self.pos = Vector2(random.randint (0,800),random.randint (0,800))
        self.taille = random.randint(3, 7)
        self.color = (255,255,255)
        self.masse = 10
        self.acceleration = 5
        self.maxAcceleration = 10
        self.maxVitesse = 10
        self.vision= 20

    def show (self):
        core.Draw.circle(self.color,[int(self.pos.x),int(self.pos.y)],self.taille)

    def deplacement(self, asteroide):




        if self.acceleration.length() > self.maxAcceleration:
            self.acceleration.scale_to_length(self.maxAcceleration)

        self.vitesse = self.vitesse + self.acceleration

        if self.vitesse.length() > self.maxVitesse:
            self.vitesse.scale_to_length(self.maxVitesse)

        self.position = self.position + self.vitesse

        self.acceleration = Vector2(0, 0)


