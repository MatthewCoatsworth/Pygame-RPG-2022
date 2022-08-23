#characters and envoroments
import pygame
from config import *
import math #used for maths calulations
import random #to genarate random number

class Spritesheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        #Create a sprite that is a image/surface 
        sprite = pygame.Surface([width, height])
        #Draw the sprite
        sprite.blit(self.sheet, (0,0), (x,y,width,height))
        #made the background of the image/surafce tranparent
        sprite.set_colorkey(BLACK)
        return sprite




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
        self.height = TILESIZE


        #set start movement for player
        self.x_change = 0 
        self.y_change = 0
        self.facing = 'down'

        #no longer needed code
        #self.image = pygame.Surface([self.width,self.hight])
        #self.image.fill(RED)

        #set player sprite image and hitbox
        self.image = self.game.char_spritesheet.get_sprite(0,0, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        #Initialise animation loop for player
        self.animation_loop = 0



    def update(self):
        #move player
        self.movement()
        #animate the player
        self.animate()
        #change horizontal movement speed
        self.rect.x += self.x_change
        #Check if the player has colided with a block on x-axis
        self.collide_blocks('x')

        #change vertical movement speed
        self.rect.y += self.y_change
        #Check if the player has colided with a block on y-axis
        self.collide_blocks('y')

        #stop moving
        self.x_change = 0
        self.y_change = 0


    def movement(self):
        #Moving player using input keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            #moves evrything inclouding player to the right
            for sprite in self.game.all_sprites:
                sprite.rect.x += PLAYER_SPEED
            #move player to the left so the player stays in the center of the screen 
            self.x_change -= PLAYER_SPEED
            #sets player direction 
            self.facing = 'left'

        if keys[pygame.K_RIGHT]:
            for sprite in self.game.all_sprites:
                sprite.rect.x -= PLAYER_SPEED
            self.x_change += PLAYER_SPEED
            self.facing = 'right'

        if keys[pygame.K_UP]:
            for sprite in self.game.all_sprites:
                sprite.rect.y += PLAYER_SPEED
            self.y_change -= PLAYER_SPEED
            self.facing = 'up'
            
        if keys[pygame.K_DOWN]:
            for sprite in self.game.all_sprites:
                sprite.rect.y -= PLAYER_SPEED
            self.y_change += PLAYER_SPEED
            self.facing = 'down'


            

    def collide_blocks(self, direction):

        if direction == "x":
            #when the player intesects with another object in the group called block the player stops moveing
            hits = pygame.sprite.spritecollide(self, self.game.block, False)
            if hits:
                #if player moving right 
                if self.x_change > 0:
                    #move the player left off of the block
                    self.rect.x = hits[0].rect.left - self.rect.width
                    #move all the sprites in the game right to cacel out the code under movement method while the player is not moveing
                    for sprite in self.game.all_sprites:
                        sprite.rect.x += PLAYER_SPEED
                #if player moveing left 
                if self.x_change < 0:
                    #move the player right off of the block
                    self.rect.x = hits[0].rect.right
                    #move all the sprites in the game left to cacel out the code under movement method while the player is not moveing
                    for sprite in self.game.all_sprites:
                        sprite.rect.x -= PLAYER_SPEED
                   
        #when the player intesects with another object in the group called block the player stops moveing
        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.block, False)
            if hits:
                #if player moving down
                if self.y_change > 0:
                    #move the player up off of the block
                    self.rect.y = hits[0].rect.top - self.rect.height
                    #move all the sprites in the game in the oppersit driction that they are moved in the movement method while the player is not moveing
                    for sprite in self.game.all_sprites:
                        sprite.rect.y += PLAYER_SPEED
                    #if player moving up
                if self.y_change < 0:
                    #move the player down off of the block
                    self.rect.y = hits[0].rect.bottom
                    #move all the sprites in the game in the oppersit driction that they are moved in the movement method while the player is not moveing
                    for sprite in self.game.all_sprites:
                        sprite.rect.y -= PLAYER_SPEED



    def animate(self):
        #create one array for each drection totaling 4 arrays
        #each arry as 3 sprites so when the player moves 3 imagers are looped
        down_animations = [self.game.char_spritesheet.get_sprite(0, 0, self.width, self.height),
                           self.game.char_spritesheet.get_sprite(32, 0, self.width, self.height),
                           self.game.char_spritesheet.get_sprite(64, 0, self.width, self.height)]

        up_animations = [self.game.char_spritesheet.get_sprite(0, 96, self.width, self.height),
                         self.game.char_spritesheet.get_sprite(32, 96, self.width, self.height),
                         self.game.char_spritesheet.get_sprite(64, 96, self.width, self.height)]

        left_animations = [self.game.char_spritesheet.get_sprite(0, 32, self.width, self.height),
                           self.game.char_spritesheet.get_sprite(32, 32, self.width, self.height),
                           self.game.char_spritesheet.get_sprite(64, 32, self.width, self.height)]

        right_animations = [self.game.char_spritesheet.get_sprite(0, 64, self.width, self.height),
                            self.game.char_spritesheet.get_sprite(32, 64, self.width, self.height),
                            self.game.char_spritesheet.get_sprite(64, 64, self.width, self.height)]
       
        #if the player is facing down
        if self.facing == 'down':
            #if the player is not moving on the y accsess
            if self.y_change == 0:
                #set the image to standing still facing down
                self.image = down_animations[1]
            #if the player is moveing loop the animation
            else:
                #Rounds down to smallest whole number therefor 1.6 --> 1.0 set image to "self.game.char_spritesheet.get_sprite(0, 0, self.width, self.height)"
                self.image = down_animations[math.floor(self.animation_loop)]
                #add 0.3 to the loop 60 times per second
                self.animation_loop += 0.3
                #when 0.3 had been added so that the number is >= 3 then set the number to 0
                if self.animation_loop >= 3:
                    self.animation_loop = 0

        #if the player is facing up
        if self.facing == 'up':
            #if the player is not moving on the y accsess
            if self.y_change == 0:
                #set the image to standing still facing up
                self.image = up_animations[1]
            #if the player is moveing loop the animation
            else:
                #Rounds down to smallest whole number
                self.image = up_animations[math.floor(self.animation_loop)]
                #add 0.3 to the loop 60 times per second
                self.animation_loop += 0.3
                #when 0.3 had been added so that the number is >= 3 then set the number to 0
                if self.animation_loop >= 3:
                    self.animation_loop = 0

        #if the player is facing left
        if self.facing == 'left':
            #if the player is not moving on the x accsess
            if self.x_change == 0:
                #set the image to standing still facing left
                self.image = left_animations[1]
            #if the player is moveing loop the animation
            else:
                #Rounds down to smallest whole number
                self.image = left_animations[math.floor(self.animation_loop)]
                #add 0.3 to the loop 60 times per second
                self.animation_loop += 0.3
                #when 0.3 had been added so that the number is >= 3 then set the number to 0
                if self.animation_loop >= 3:
                    self.animation_loop = 0

        #if the player is facing right
        if self.facing == 'right':
            #if the player is not moving on the x accsess
            if self.x_change == 0:
                #set the image to standing still facing up
                self.image = right_animations[1]
            #if the player is moveing loop the animation
            else:
                #Rounds down to smallest whole number
                self.image = right_animations[math.floor(self.animation_loop)]
                #add 0.3 to the loop 60 times per second
                self.animation_loop += 0.3
                #when 0.3 had been added so that the number is >= 3 then set the number to 0
                if self.animation_loop >= 3:
                    self.animation_loop = 0







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
        self.height = TILESIZE

        #no longer needed code
        #self.image = pygame.Surface([self.width,self.height])
        #self.image.fill(BLUE)

        #set block sprite image and hitbox
        self.image = self.game.obj_spritesheet.get_sprite(32,448, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class Ground(pygame.sprite.Sprite):
    #Initialise ground
    def __init__(self, game, x, y):
        self.game = game
        #set the ground layer
        self._layer = GROUND_LAYER
        #add sprites to the group 
        self.groups = self.game.all_sprites 
        #use pygame to initialize the ground
        pygame.sprite.Sprite.__init__(self, self.groups)

        #set the location each tile
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        #set block sprite image and hitbox
        self.image = self.game.obj_spritesheet.get_sprite(0,32, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y



class NPC1(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        #creates a NPC
        self.game = game
        #set the NPC layer
        self._layer = NPC_LAYER
        #add sprites to the NPC group
        self.groups = self.game.all_sprites, self.game.npc
        #use pygame to initialize NPC
        pygame.sprite.Sprite.__init__(self, self.groups)
        #set start location for NPC
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        #set NPC sprite image and hitbox
        self.image = self.game.char_spritesheet.get_sprite(320,0, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        #Initialise animation loop for NPC
        self.animation_loop = 0

