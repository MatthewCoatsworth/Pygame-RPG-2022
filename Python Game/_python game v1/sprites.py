#characters and envoroments
import pygame
from config import *
import math #used for maths calulations
import random   #to genarate random number

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        #creates a player
        self.game = game
        self._layer =PLAYER_LAYER
        self.groups = self.game.all_sprite
        pygame.sprite.Sprite.__init__(self, self.groups)
        #set start location for player
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.hight = TILESIZE

        self.image = pygame.Surface([self.width,self.hight])
        self.image.fill(RED)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
