#characters and envoroments
import pygame
from config import *
import math #used for maths calulations
import random   #to genarate random number

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        #creates a player
        self.game = game
        #set the player layer
        self._layer =PLAYER_LAYER
        #add sprites to the player group
        self.groups = self.game.all_sprites
        #use pygame to initialize player
        pygame.sprite.Sprite.__init__(self, self.groups)
        #set start location for player
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.hight = TILESIZE


        #set start movement for player
        self.x_change = 0 
        self.y_change = 0
        self.facing = 'down'

        #set player sprite image and hitbox
        self.image = pygame.Surface([self.width,self.hight])
        self.image.fill(RED)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        #move player
        self.movement()
        #change mevement speed
        self.rect.x += self.x_change
        self.rect.y += self.y_change
        self.x_change = 0
        self.y_change = 0

    def movement(self):
        #Moving player using input keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x_change -= PLAYER_SPEED
            self.facing = 'left'
        if keys[pygame.K_RIGHT]:
            self.x_change += PLAYER_SPEED
            self.facing = 'right'
        if keys[pygame.K_UP]:
            self.y_change -= PLAYER_SPEED
            self.facing = 'up'
        if keys[pygame.K_DOWN]:
            self.y_change += PLAYER_SPEED
            self.facing = 'down'
            
class Block(pygame.sprite.Sprite):
    #Initialise block
    def __init__(self, game, x, y):
        self.game = game
        #set the Block layer
        self._layer = BLOCK_LAYER
        #add sprites to the block group 
        self.groups = self.game.all_sprites, self.game.block 
        #use pygame to initialize the blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        #set the location each block
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.hight = TILESIZE


        #set start movement for player
        self.x_change = 0 
        self.y_change = 0
        self.facing = 'down'

        #set block sprite image and hitbox
        self.image = pygame.Surface([self.width,self.hight])
        self.image.fill(BLUE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y