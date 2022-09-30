#import exsternal libaryes
#requied for dipaing srites and hadling imputs
import pygame
#sys is uesd to end the game
import sys  
#import local files
from sprites import *
from config import *
print("""✅keys.png by BizmasterStudios from https://opengameart.org/content/key-icons licened under Creative Commons Attribution 4.0 International(I have modifide the file )""")
print("""✅'Antifarea's RPG sprite set 1, enlarged w/ transparent background, fixed' by Antifarea from https://opengameart.org/content/antifareas-rpg-sprite-set-1-enlarged-w-transparent-background-fixed licened under Creative Commons Attribution 3.0 Unported""")

#create class called game
class Game:
    def __init__(self):
        #initialise pygame
        pygame.init()
        #set screen size with pygame
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        #sets time for refresh rate with pygame
        self.clock = pygame.time.Clock()
        #set the font to use in the game
        self.font = pygame.font.Font('ariali.ttf', 14)
        #manage when to close game
        self.running = True
        #load the sprite sheets
        self.char_spritesheet = Spritesheet('img/chars.png')
        self.obj_spritesheet = Spritesheet('img/objects.png')
        self.key_spritesheet = Spritesheet('img/keys.png')
        self.textbox_spritesheet = Spritesheet('img/extbox.png')



    def createTilemap(self):
        Textbox(self, 50, SCREEN_HEIGHT -120)
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
        self.textbox = pygame.sprite.LayeredUpdates()
        #set the text to display to no text 
        self.displaytext = ""

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
        self.textbox.update()

    def draw(self):
        #show screen, characters and set background color 
        self.screen.fill(BLACK)
        #make the sprites appear on the screen 
        self.all_sprites.draw(self.screen)
        #dispaly a box for text to apear in
        self.textbox.draw(self.screen)
        #make the "displaytext" variable appar in the text box with a white font color 
        text = self.font.render(self.displaytext, True, WHITE)
        text_rect = text.get_rect(x=70, y=SCREEN_HEIGHT-110)
        self.screen.blit(text,text_rect)
        #set the refresh rate 
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