import pygame

from debug import debug
from player import Player
from settings import WORLD_MAP, TILESIZE
from tile import Tile
from camera import YSortCameraGroup


class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        # sprite groups
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        self.player = None
        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for column_index, cell in enumerate(row):
                x = row_index * TILESIZE
                y = column_index * TILESIZE

                match cell:
                    case 'x':
                        Tile((x, y), [self.visible_sprites, self.obstacle_sprites])
                    case 'p':
                        # interesting pattern, the player knows about all of the sprites in the Level
                        # my intuition would be to have the level be aware of all of this, or some
                        # higher abstraction understand collisions, but no biggie. I am learning
                        self.player = Player((x, y), [self.visible_sprites], self.obstacle_sprites)
                    case _:
                        pass

    def run(self):
        # update and draw the level
        # self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.camera_draw(self.player)
        self.visible_sprites.update()
        debug(self.player.direction)
