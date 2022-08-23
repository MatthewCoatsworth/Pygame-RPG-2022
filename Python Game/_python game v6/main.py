#import exsternal libaryes
#requied for dipaing srites and hadling imputs
import pygame
#sys is uesd to end the game
import sys  
#import local files
from sprites import *
from config import *

#create class called game
class Game:
    def __init__(self):
        #initialise pygame
        pygame.init()
        #set screen size whith pygame
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        #sets time for refresh rate with pygame
        self.clock = pygame.time.Clock()
        #manage when to close game
        self.running = True
        #load the sprite sheets
        self.char_spritesheet = Spritesheet('_python game v6/img/chars.png')
        self.obj_spritesheet = Spritesheet('_python game v6/img/objects.png')
        self.key_spritesheet = Spritesheet('_python game v6/img/keys.png')

    def createTilemap(self):
        #loop throught each row of the tile map
        for i, row in enumerate(tilemap):
            #loop throught each of the row 
            for j, column in enumerate(row):
                #Draw the gorund alywas
                Ground(self, j, i)
                #Create the player in the game where a p appears in the tile map
                if column == "p":
                    Player(self, j, i)
                #Create a barrier in the game where a B appears in the tile map
                if column == "B":
                    Block(self, j, i)
                #Create a NPC in the game where a N appears in the tile map
                if column == "N":
                    NPC1(self, j, i)
                #Create a wall in the game where a W appears in the tile map
                if column == "W":
                    Wall(self, j, i)
                
                if column == "D":
                    Lock(self, j, i) 
                    Door(self, j, i)

                if column == "K":
                    Key(self, j, i)



    def new(self):
        #starts a new game
        self.playing = True
        #initalize sprite groups
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.block = pygame.sprite.LayeredUpdates()
        self.npc = pygame.sprite.LayeredUpdates()
        self.doors = pygame.sprite.LayeredUpdates()
        self.lock = pygame.sprite.LayeredUpdates()
        self.keys = pygame.sprite.LayeredUpdates()

        #Initialise player
        self.player = Player(self, 1, 2)
        #Draw the tile map
        self.createTilemap()
        

    def events(self):
        #game loop evnets
        for event in pygame.event.get():
            #Close the program when the player quits
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        #refresh screen
        self.all_sprites.update()

    def draw(self):
        #show screen, characters, set background color and set refresh rate
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

    def main(self):
        #main game loop
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.running = False

g = Game()
g.new()
while g.running:
    g.main()

pygame.quit()
sys.exit()