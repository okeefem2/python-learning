import pygame.sprite


# Custom class that extends a sprite group
# to give camera functionality
# keeps sprites sorted by y coordinate
from player import Player


class YSortCameraGroup(pygame.sprite.Group):

    def __init__(self):
        # general setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2  # x direction. reminder // is "floor dividing"
        self.half_height = self.display_surface.get_size()[1] // 2  # y direction
        self.offset = pygame.math.Vector2()

    def camera_draw(self, player):
        self.calculate_offset(player)
        # hmmm seems ineeficient to sort each time we draw!
        # this keeps the right order of sprites for the overlap we want.
        for sprite in sorted(self.sprites(), key=lambda s: s.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)

    def calculate_offset(self, player: Player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
