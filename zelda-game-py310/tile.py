import pygame
from pygame.sprite import AbstractGroup


class Tile(pygame.sprite.Sprite):
    def __init__(self, position, groups: list[AbstractGroup]):
        super().__init__(groups)
        self.image = pygame.image.load('./graphics/test/rock.png').convert_alpha()
        # For the user of this class
        # the position passed to the constructor will set the top left of the tile to that position
        self.rect = self.image.get_rect(topleft=position)
        self.hitbox = self.rect.inflate(0, -10)
