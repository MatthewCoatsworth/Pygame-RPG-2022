#import exsternal libaryes
#requied for dipaing srites and hadling imputs
from tkinter.tix import Tree
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

    def new(self):
        #starts a new game
        self.playing = True
        self.player = Player(self, 1, 2)

    def events(self):
        #game loop evnets
        for event in pygame.event.get():
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
    g.main

pygame.quit()
sys.exit()