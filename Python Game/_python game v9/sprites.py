"""this python file manages the Sprite classes and methods for my game."""
# characters and envoroments
import pygame
from config import *
# used for maths calulations
import math


class Player(pygame.sprite.Sprite):
    """Represents the player sprite."""

    def __init__(self, game, x, y):
        """Initialize the player.

        Input
            game: The game that is running
            x: horizontal start postion of where it appears on the screen
            y: Vertical start postion of where it appears on the screen
        """
        # creates a player
        self.game = game
        # set the player layer
        self._layer = PLAYER_LAYER
        # add sprites to the player group
        self.groups = self.game.all_sprites
        # use pygame to initialize player
        pygame.sprite.Sprite.__init__(self, self.groups)
        # set start location for player
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        # set start movement for player
        self.x_change = 0
        self.y_change = 0
        self.facing = 'down'

        # set player sprite image and hitbox
        self.image = self.game.char_spritesheet.get_sprite(0, 74, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        # Initialise animation loop for player
        self.animation_loop = 0
        # set the status of "haskey" to false
        self.haskey = False

    def update(self):
        """Update the player."""
        # move player
        self.movement()
        # animate the player
        self.animate()
        # change horizontal movement speed
        self.rect.x += self.x_change
        # Check if the player has colided with a block on x-axis
        self.collide_blocks('x')
        # change vertical movement speed
        self.rect.y += self.y_change
        # Check if the player has colided with a block on y-axis
        self.collide_blocks('y')
        # stop moving
        self.x_change = 0
        self.y_change = 0

    def movement(self):
        """Move player using input keys."""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            # moves evrything in the all sprites-
            # group (which includes the player) to the right
            for sprite in self.game.all_sprites:
                sprite.rect.x += PLAYER_SPEED
            # moves the player to the left so the-
            # player stays in the center of the screen
            self.x_change -= PLAYER_SPEED
            # sets player direction
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
        """Manage what happens when the player collides with another sprite."""
        if direction == "x":
            # when the player collides with an object in the-
            # group called block stop the player from moveng in that direction
            hits = pygame.sprite.spritecollide(self, self.game.block, False)
            if hits:
                # if player moving right
                if self.x_change > 0:
                    # move the player left off of the block
                    self.rect.x = hits[0].rect.left - self.rect.width
                    # after the collision reset the player's-
                    # position off of the other block
                    for sprite in self.game.all_sprites:
                        sprite.rect.x += PLAYER_SPEED
                # if player moveing left
                if self.x_change < 0:
                    # move the player right off of the block
                    self.rect.x = hits[0].rect.right
                    # after the collision reset the player's-
                    # position off of the other block
                    for sprite in self.game.all_sprites:
                        sprite.rect.x -= PLAYER_SPEED
        # when the player collides with an object in the-
        # group called block stop the player from moveng in that direction
        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.block, False)
            if hits:
                # if player moving down
                if self.y_change > 0:
                    # move the player up off of the block
                    self.rect.y = hits[0].rect.top - self.rect.height
                    # after the collision reset the player's-
                    # position off of the other block
                    for sprite in self.game.all_sprites:
                        sprite.rect.y += PLAYER_SPEED
                    # if player moving up
                if self.y_change < 0:
                    # move the player down off of the block
                    self.rect.y = hits[0].rect.bottom
                    # after the collision reset the player's-
                    # position off of the other block
                    for sprite in self.game.all_sprites:
                        sprite.rect.y -= PLAYER_SPEED

    def animate(self):
        """Animate the Player.

        create one array for each drection totaling 4 arrays
        each arry as 3 sprites so when the player moves 3 imagers are looped.
        """
        down_animations = [self.game.char_spritesheet.get_sprite(0, 74, self.width, self.height),
                           self.game.char_spritesheet.get_sprite(32, 74, self.width, self.height),
                           self.game.char_spritesheet.get_sprite(64, 74, self.width, self.height)]

        up_animations = [self.game.char_spritesheet.get_sprite(0, 2, self.width, self.height),
                         self.game.char_spritesheet.get_sprite(32, 2, self.width, self.height),
                         self.game.char_spritesheet.get_sprite(64, 2, self.width, self.height)]

        left_animations = [self.game.char_spritesheet.get_sprite(0, 110, self.width, self.height),
                           self.game.char_spritesheet.get_sprite(32, 110, self.width, self.height),
                           self.game.char_spritesheet.get_sprite(64, 110, self.width, self.height)]

        right_animations = [self.game.char_spritesheet.get_sprite(0, 38, self.width, self.height),
                            self.game.char_spritesheet.get_sprite(32, 38, self.width, self.height),
                            self.game.char_spritesheet.get_sprite(64, 38, self.width, self.height)]
        # if the player is facing down
        if self.facing == 'down':
            # if the player is not moving on the y accsess
            if self.y_change == 0:
                # set the image to standing still facing down
                self.image = down_animations[1]
            # if the player is moveing loop the animation
            else:
                # Rounds down to smallest whole number
                # therefor 1.6 --> 1.0
                self.image = down_animations[math.floor(self.animation_loop)]
                # add 0.3 to the loop 60 times per second
                self.animation_loop += 0.3
                # when number is >= 3 then set the number to 0
                if self.animation_loop >= 3:
                    self.animation_loop = 0
        # if the player is facing up
        if self.facing == 'up':
            # if the player is not moving on the y accsess
            if self.y_change == 0:
                # set the image to standing still facing up
                self.image = up_animations[1]
            # if the player is moveing loop the animation
            else:
                # Rounds down to smallest whole number
                self.image = up_animations[math.floor(self.animation_loop)]
                # add 0.3 to the loop 60 times per second
                self.animation_loop += 0.3
                # when number is >= 3 then set the number to 0
                if self.animation_loop >= 3:
                    self.animation_loop = 0
        # if the player is facing left
        if self.facing == 'left':
            # if the player is not moving on the x accsess
            if self.x_change == 0:
                # set the image to standing still facing left
                self.image = left_animations[1]
            # if the player is moveing loop the animation
            else:
                # Rounds down to smallest whole number
                self.image = left_animations[math.floor(self.animation_loop)]
                # add 0.3 to the loop 60 times per second
                self.animation_loop += 0.3
                # when the number is >= 3 then set the number to 0
                if self.animation_loop >= 3:
                    self.animation_loop = 0
        # if the player is facing right
        if self.facing == 'right':
            # if the player is not moving on the x accsess
            if self.x_change == 0:
                # set the image to standing still facing up
                self.image = right_animations[1]
            # if the player is moveing loop the animation
            else:
                # Rounds down to smallest whole number
                self.image = right_animations[math.floor(self.animation_loop)]
                # add 0.3 to the loop 60 times per second
                self.animation_loop += 0.3
                # when the number is >= 3 then set the number to 0
                if self.animation_loop >= 3:
                    self.animation_loop = 0
















class Spritesheet:
    """Represents each sprite."""

    def __init__(self, file):
        """Load in the relevant sprite sheet.

        input
            file: is a png image file.
        """
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        """Display the relevant spray from the Sprite sheet .

        input
            x: Starting position on the horizontal axis.
            y: Starting position on the vertical axis.
            width: distance from x (width of Sprite)
            height: distance from y (higth of sprite)

        output:
            sprite:part of the Spritesheet that the player sees for the sprite.
        """
        # Create a sprite that is a image/surface
        sprite = pygame.Surface([width, height])
        # Draw the sprite
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        # made the background of the image/surafce tranparent
        sprite.set_colorkey(BLACK)
        return sprite


class Block(pygame.sprite.Sprite):
    """Represents the Block sprite.

    This sprite appears as a bush on the map that the player cannot move over.
    """

    # Initialise block
    def __init__(self, game, x, y):
        """Initialize the Block.

        Input
            game: The game that is running
            x: horizontal start postion of where it appears on the screen
            y: Vertical start postion of where it appears on the screen
        """
        self.game = game
        # set the Block layer
        self._layer = BLOCK_LAYER
        # add sprites to the block group
        self.groups = self.game.all_sprites, self.game.block
        # use pygame to initialize the blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        # set the location each block
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        # set block sprite image and hitbox
        self.image = self.game.obj_spritesheet.get_sprite(32, 448, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class Ground(pygame.sprite.Sprite):
    """Represents the ground sprite.

    This sprite appears as a grass on the map that the player can move over.
    """

    # Initialise ground
    def __init__(self, game, x, y):
        """Initialize the ground.

        Input
            game: The game that is running
            x: horizontal start postion of where it appears on the screen
            y: Vertical start postion of where it appears on the screen
        """
        self.game = game
        # set the ground layer
        self._layer = GROUND_LAYER
        # add sprites to the group
        self.groups = self.game.all_sprites
        # use pygame to initialize the ground
        pygame.sprite.Sprite.__init__(self, self.groups)

        # set the location each tile
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        # set ground sprite image and hitbox
        self.image = self.game.obj_spritesheet.get_sprite(0, 32, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y












class NPC1(pygame.sprite.Sprite):
    """Represents the NPC sprite.

    This sprite appears as a non-player character on the map
    that the player can interact with.
    """

    # Initialise NPC
    def __init__(self, game, x, y):
        """Initialize the NPC.

        Input
            game: The game that is running
            x: horizontal start postion of where it appears on the screen
            y: Vertical start postion of where it appears on the screen
        """
        # creates a NPC
        self.game = game
        # set the NPC layer
        self._layer = NPC_LAYER
        # add sprites to the NPC group
        self.groups = self.game.all_sprites, self.game.npc
        # use pygame to initialize NPC
        pygame.sprite.Sprite.__init__(self, self.groups)
        # set start location for NPC
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        # set NPC sprite image and hitbox
        self.image = self.game.char_spritesheet.get_sprite(0, 0, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        """Update the NPC.

        if the player touchs the key make it dissapar from the map
        set the variable for "haskey" to true
        """
        if pygame.Rect.colliderect(self.rect, self.game.player.rect):
            # set the text to display when the player collides with the NPC
            self.game.displaytext = '''You've made it into the building & completed the game'''


class Wall(pygame.sprite.Sprite):
    """Represents the wall sprite.

    This sprite appears as a wall on the map that the player cannot move over.
    """

    # Initialise wall
    def __init__(self, game, x, y):
        """Initialize the wall.

        Input
            game: The game that is running
            x: horizontal start postion of where it appears on the screen
            y: Vertical start postion of where it appears on the screen
        """
        self.game = game
        # set the wall layer (same as block)
        self._layer = BLOCK_LAYER
        # add sprites to the wall group
        self.groups = self.game.all_sprites, self.game.block
        # use pygame to initialize the walls
        pygame.sprite.Sprite.__init__(self, self.groups)

        # set the location each wall
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        # set wall sprite image and hitbox
        self.image = self.game.obj_spritesheet.get_sprite(0, 128, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.rect.width = TILESIZE - 8


class Door(pygame.sprite.Sprite):
    """Represents the door sprite.

    This sprite appears as a door on the map that the player can move through.
    """

    # Initialise door
    def __init__(self, game, x, y):
        """Initialize the door.

        Input
            game: The game that is running
            x: horizontal start postion of where it appears on the screen
            y: Vertical start postion of where it appears on the screen
        """
        self.game = game
        # set the door layer
        self._layer = DOOR_LAYER
        # add sprites to the door group
        self.groups = self.game.all_sprites, self.game.doors
        # use pygame to initialize the doors
        pygame.sprite.Sprite.__init__(self, self.groups)

        # set the location each door
        self.x = x * TILESIZE
        self.y = y * TILESIZE + 1
        self.width = TILESIZE
        self.height = TILESIZE

        # set door sprite image and hitbox
        self.closed = self.game.obj_spritesheet.get_sprite(64, 128, self.width, self.height)
        self.open = self.game.obj_spritesheet.get_sprite(128, 288, self.width, self.height)
        self.image = self.closed

        # match size of Hitbox to the same-
        # dimensions as the Sprite selected on the style sheet
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        """Update the door.

        open the door when the player collides with it.
        player can only collide with the door when the lock is removed.
        """
        if pygame.Rect.colliderect(self.rect, self.game.player.rect):
            self.image = self.open
            # __
            self.game.displaytext = 'congratulations you use the key and open the door'


class Lock(pygame.sprite.Sprite):
    """Represents the lock sprite.

    This is an invisible barrier on the map that the player can't move over.
    """

    # Initialise lock
    def __init__(self, game, x, y):
        """Initialize the lock.

        Input
            game: The game that is running
            x: horizontal start postion of where it appears on the screen
            y: Vertical start postion of where it appears on the screen
        """
        self.game = game
        # set the lock layer
        self._layer = BLOCK_LAYER
        # add sprites to the lock group
        self.groups = self.game.all_sprites, self.game.block, self.game.lock
        # use pygame to initialize the locks
        pygame.sprite.Sprite.__init__(self, self.groups)

        # set the location and size of each lock
        # the width and height is increased to insure the players-
        # hit box cannot come into contact with the hit box of the door
        self.x = x * TILESIZE - 5
        self.y = y * TILESIZE - 5
        self.width = TILESIZE + 10
        self.height = TILESIZE + 10

        # set lock sprite image and hitbox
        # locoantion of on sprite sheet shound be set to "288,32,"
        self.image = self.game.obj_spritesheet.get_sprite(160, 448, self.width, self.height)

        # match size of Hitbox to the same dimensions-
        # as the Sprite selected on the style sheet
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    # removes the key the invisible barrier over-
    # the door from the game when the key is collected
    def update(self):
        """Update the lock.

        the lock is removed from the game when the player collides with it.
        the text displayed in the text box is changed.
        """
        if self.game.player.haskey is True:
            self.kill()
        if pygame.Rect.colliderect(self.rect, self.game.player.rect):
            self.game.displaytext = 'NO'


class Key(pygame.sprite.Sprite):
    """Represents the key sprite.

    This sprite appears as a key on the map that the player can pick up.
    """

    # Initialise key
    def __init__(self, game, x, y):
        """Initialize the key.

        Input
            game: The game that is running
            x: horizontal start postion of where it appears on the screen
            y: Vertical start postion of where it appears on the screen
        """
        self.game = game
        # set the key layer
        self._layer = KEY_LAYER
        # add sprites to the key group
        self.groups = self.game.all_sprites, self.game.keys
        # use pygame to initialize the key
        pygame.sprite.Sprite.__init__(self, self.groups)

        # set the location and size the key
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        # set key sprite image and hitbox
        self.image = self.game.key_spritesheet.get_sprite(64, 0, self.width, self.height)

        # match size of Hitbox to the same dimensions-
        # as the Sprite selected on the style sheet
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        """Update the key.

        if the player touchs the key make it dissapar from the map
        the "haskey" variable is set to true.
        """
        if pygame.Rect.colliderect(self.rect, self.game.player.rect):
            # __
            self.game.displaytext = 'You picked up the key'
            # remove the key
            self.kill()
            # set "haskey" to true
            self.game.player.haskey = True


class Textbox(pygame.sprite.Sprite):
    """Represents the textbox sprite.

    This sprite appears as a box fixed to the bottom of the game window.
    """

    # Initialise textbox
    def __init__(self, game, x, y):
        """Initialize the text box.

        Input
            game: The game that is running
            x: horizontal start postion of where it appears on the screen
            y: Vertical start postion of where it appears on the screen
        """
        self.game = game
        # set the textbox layer
        self._layer = TEXTBOX_LAYER
        # add sprites to the textbox group.
        # the other spirtes were added to the "game.all_sprites" group-
        # however as these sprites move when the arrow keys are pressed-
        # I added the textbox to a diffrent group
        self.groups = self.game.textbox
        # use pygame to initialize the textbox
        pygame.sprite.Sprite.__init__(self, self.groups)

        # set the location each block
        self.x = x
        self.y = y
        self.width = 540
        self.height = 100

        # set block sprite image and hitbox
        self.image = self.game.textbox_spritesheet.get_sprite(0, 0, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
