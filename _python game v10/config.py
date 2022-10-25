"""This file contains the tile map and global variables for my game."""
# for variables

# size in px
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640
TILESIZE = 32
# frams per second
FPS = 60
# colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
# set the player speed for movment
PLAYER_SPEED = 3
# set layers for sprites
PLAYER_LAYER = 4
BLOCK_LAYER = 2
GROUND_LAYER = 1
NPC_LAYER = 3
DOOR_LAYER = 3
KEY_LAYER = 3
TEXTBOX_LAYER = 3

# create the easy map for the environment
tilemap_easy = [
    'BBBBBBBBBBBBBBBBBBBB',
    'B..................B',
    'B.......BB....BB...B',
    'B....BBB......B....B',
    'B..........BBB.....B',
    'B.........BBB......B',
    'B.........BBB......B',
    'B........PBBB......B',
    'B..................B',
    'B...BBB............B',
    'B.BB..BB..WWWWDWWWWB',
    'B....BBB..W........B',
    'BB.....B..W.N......B',
    'B......BBBWWWWWWWWWB',
    'B.........B....B...B',
    'B.........B.B..B.K.B',
    'B...........B......B',
    'BBBBBBBBBBBBBBBBBBBB',
]

# create the medium map for the environment
tilemap_medium = [
    ".................BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
    ".................BB..............B...........B..BB",
    ".................BB..B..B........B...........B..BB",
    ".................BB..B..B..BBBBBBB..BBBB..B..B..BB",
    ".................BB..B..B..B..B..B..B.....B.....BB",
    "BBBBBBBBBBBBBBBBBBB..B..B..B..B..B..B.....B.....BB",
    "B................BBBBB..B.....B..B..B..BBBBBBBBBBB",
    "B........P.......BB.....B.....B.....B..B........BB",
    "B................BB.....B.....B.....B..B........BB",
    "B................BB..BBBB..BBBBBBB..B..B..B..B..BB",
    "B................BB...K.B...........B.....B..B..BBWWWWWWWWWWWWW",
    "B................BB.....B...........B.....B..B..BB............W",
    "B................BB..BBBB..BBBBBBB..BBBBBBB..BBBBB............W",
    "B................BB..B.....B.....B....B.........D.............W",
    "B................BB..B.....B.....B....B.........BB..........N.W",
    "B....................BBBBBBBBBB..B..BBBBBBBBBB..BB............W",
    "B.............................B..B...........B..BBWWWWWWWWWWWWW",
    "B................BB...........B..B...........B..BB",
    "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",

]

# create the hard map for the environment
tilemap_hard = [
    ".................BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
    ".................BB..............B...........BK.BB",
    ".................BB..B..B........B...........B..BB",
    ".................BB..B..B..BBBBBBB..BBBB..B..B..BB",
    ".................BB..B..B..B..B..B..B.....B.....BB",
    "BBBBBBBBBBBBBBBBBBB..B..B..B..B..B..B.....B.....BB",
    "B................BBBBB..B.....B..B..B..BBBBBBBBBBB",
    "B........P.......BB.....B.....B.....B..B........BB",
    "B................BB.....B.....B.....B..B........BB",
    "B................BB..BBBB..BBBBBBB..B..B..B..B..BB",
    "B................BB.....B...........B.....B..B..BBWWWWWWWWWWWWW",
    "B................BB.....B...........B.....B..B..BB............W",
    "B................BB..BBBB..BBBBBBB..BBBBBBB..BBBBB............W",
    "B................BB..B.....B.....B...........B..D.............W",
    "B................BB..B.....B.....B...........B..BB..........N.W",
    "B....................BBBBBBBBBB..B..BBBBBBBBBB..BB............W",
    "B.............................B..B........B.....BBWWWWWWWWWWWWW",
    "B................BB...........B..B........B.....BB",
    "BBBBBBBBBBBBBBBBBBBBBBBBB..B..B..BBBBBBB..B..BBBBB",
    ".................BB..B.....B.....B.....B.....B..BB",
    ".................BB..B.....B.....B.....B.....B..BB",
    ".................BB..B..BBBBBBBBBB..BBBBBBBBBB..BB",
    ".................BB.....B........B........B.....BB",
    ".................BB.....B........B........B.....BB",
    ".................BB..BBBB..B..BBBBBBB..B..BBBB..BB",
    ".................BB.....B..B........B..B........BB",
    ".................BB.....B..B........B..B........BB",
    ".................BB..BBBB..B..BBBBBBB..B..BBBB..BB",
    ".................BB........B...........B........BB",
    ".................BB........B...........B........BB",
    ".................BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
]
