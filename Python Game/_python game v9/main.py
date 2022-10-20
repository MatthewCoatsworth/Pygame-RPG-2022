"""This is a game to provied the player with a short bit of entertament."""
# import exsternal libaryes
# requied for dipaing srites and hadling imputs
import pygame
# sys is uesd to end the game
import sys
# import local files
from sprites import *
from config import *
print("""✅keys.png by BizmasterStudios from
https://opengameart.org/content/key-icons
licened under Creative Commons Attribution
4.0 International(I have modifide the file)

✅'Antifarea's RPG sprite set 1, enlarged
w/ transparent background, fixed' by Antifarea from
https://opengameart.org/content/
antifareas-rpg-sprite-set-1-enlarged-w-transparent-background-fixed
licened under Creative Commons Attribution 3.0 Unported""")


# create class called game
class Game:
    """represents the game."""

    def __init__(self):
        """Initialize the screen.

        Set screen size, font, in game time.
        Load the image to display for spites.
        """
        # initialise pygame
        pygame.init()
        # set screen size with pygame
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        # sets time for refresh rate with pygame
        self.clock = pygame.time.Clock()
        # set the font to use in the game
        self.font = pygame.font.Font('ariali.ttf', 14)
        # manage when to close game
        self.running = True
        # load the sprite sheets
        self.char_spritesheet = Spritesheet('img/chars.png')
        self.obj_spritesheet = Spritesheet('img/objects.png')
        self.key_spritesheet = Spritesheet('img/keys.png')
        self.textbox_spritesheet = Spritesheet('img/extbox.png')

    def createtilemap(self, tilemap):
        """Draw the map.

        Uses the tilemap list from config.py to draw the game map on
        the screen. It calls the relivant class function when a letter
        associated with that class apears on the tilemap.
        """
        Textbox(self, 50, SCREEN_HEIGHT - 120)
        # loop throught each row of the tile map
        for i, row in enumerate(tilemap):
            # loop throught each of the row
            for j, column in enumerate(row):
                # Draw the gorund alywas
                Ground(self, j, i)
                # Create the player where a p appears in the tile map
                if column == "P":
                    self.player = Player(self, j, i)
                # Create a barrier where a B appears in the tile map
                if column == "B":
                    Block(self, j, i)
                # Create a NPC where a N appears in the tile map
                if column == "N":
                    NPC1(self, j, i)
                # Create a wall where a W appears in the tile map
                if column == "W":
                    Wall(self, j, i)
                # Create a lock and a Door where a D appears in the tile map
                if column == "D":
                    Lock(self, j, i)
                    Door(self, j, i)
                # Create a key where a K appears in the tile map
                if column == "K":
                    Key(self, j, i)

    def new(self, tilemap):
        """Start the game and initializes variables and Sprite groups."""
        # starts a new game
        self.playing = True
        # initalize sprite groups
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.block = pygame.sprite.LayeredUpdates()
        self.npc = pygame.sprite.LayeredUpdates()
        self.doors = pygame.sprite.LayeredUpdates()
        self.lock = pygame.sprite.LayeredUpdates()
        self.keys = pygame.sprite.LayeredUpdates()
        self.textbox = pygame.sprite.LayeredUpdates()
        # set the text to display to no text
        self.displaytext = "Welcome, go find a key to enter the door"

        # Draw the tile map
        self.createtilemap(tilemap)

    def events(self):
        """Act on game event.

        Keeps the game running until the player closes it,
        if an event occurs such as pygame.QUIT the game will close.
        """
        # game loop evnets
        for event in pygame.event.get():
            # Close the program when the player quits
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        """Update what is to be displayed on the screen."""
        # refresh screen
        self.all_sprites.update()
        self.textbox.update()

    def draw(self):
        """Make all sprites and the text box appear on the screen."""
        # show screen, characters and set background color
        self.screen.fill(BLACK)
        # make the sprites appear on the screen
        self.all_sprites.draw(self.screen)
        # dispaly a box for text to apear in
        self.textbox.draw(self.screen)
        # set the font and make it white
        # make the "displaytext" variable appar in the text box
        text = self.font.render(self.displaytext, True, WHITE)
        text_rect = text.get_rect(x=70, y=SCREEN_HEIGHT-110)
        self.screen.blit(text, text_rect)
        # set the refresh rate
        self.clock.tick(FPS)
        pygame.display.update()

    def main(self):
        """Call the other classes so they run and stop when the user quits."""
        # main game loop
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.running = False


# the Questions shown to the player so they know what to type
print("*****************************************************")
print("*                                                   *")
print("*  What difficulty do you want to play              *")
print("*  [1] : Easy                                       *")
print("*  [2] : Medium                                     *")
print("*  [3] : Hard                                       *")
print("*                                                   *")
print("*****************************************************")

# set the expected and boundary values for player to select difficulty level
easy_values = ["1", "Easy", "EASY", "[1]", "e", "E", "easy"]
med_values = ["2", "Medium", "MEDIUM", "[2]", "m", "M", "medium"]
hard_values = ["3", "Hard", "HARD", "[3]", "h", "H", "hard"]

# set the difficulty variable default to ""
difficulty = ""

# while loop to make sure that the question continues-
# to be asked until the player inputs a valid response
while difficulty not in easy_values and difficulty not in med_values and difficulty not in hard_values:
    # The difficulty variable is set by the players input
    difficulty = input()
    # If statement for selecting the difficulty by checking if the-
    # player has input either at easy value medium value or hard-
    # Or if the input is invalid
    if difficulty in easy_values:
        # tells the player the difficulty that has been selected
        print("You selected easy")
        # sets the map to the easy map from the config file
        map = tilemap_easy
    # elif statement for when the player selects a medium value
    elif difficulty in med_values:
        # tells the player the difficulty that has been selected
        print("You selected medium")
        # sets the map to the medium map from the config file
        map = tilemap_medium
    # elif statement for when the player selects a hard value
    elif difficulty in hard_values:
        # tells the player the difficulty that has been selected
        print("You selected hard")
        # sets the map to the hard map from the config file
        map = tilemap_hard
    # else statement for when the player inputted an incorrect response
    else:
        print("You MUST type 1, 2 or 3 to set difficulty and start the game")

# Initialise the game
g = Game()
g.new(map)
while g.running:
    g.main()
# Exit game cleanly once the player has quit
pygame.quit()
sys.exit()
