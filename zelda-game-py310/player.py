import pygame
from pygame.sprite import AbstractGroup


class Player(pygame.sprite.Sprite):
    def __init__(self, position, groups: list[AbstractGroup],
                 obstacle_sprites: AbstractGroup):  # TODO type for obstacles
        super().__init__(groups[0])  # TODO some type weirdness here
        self.image = pygame.image.load('./graphics/test/player.png').convert_alpha()
        # For the user of this class
        # the position passed to the constructor will set the top left of the tile to that position
        self.rect = self.image.get_rect(topleft=position)
        self.hitbox = self.rect.inflate(0, -26)

        self.direction = pygame.math.Vector2()  # x,y vector defaulting to 0,0
        self.speed = 5
        self.obstacle_sprites = obstacle_sprites


    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0

    def move(self, speed):
        # If the length of the vector
        if self.direction.magnitude() != 0:
            # Normalize the vector to make sure it is 1 and not something else
            # to make sure the speed is the same for any directional movement
            self.direction = self.direction.normalize()
        self.hitbox.x += self.direction.x * speed
        self.collision_x()
        self.hitbox.y += self.direction.y * speed
        self.collision_y()
        # simple movement, refactored to use independent directions above ^^
        # self.rect.center += self.direction * speed
        self.rect.center = self.hitbox.center

    def update(self):
        self.input()
        self.move(self.speed)

    def collision_x(self):
        # NOTE the video uses a single collision function with a direction passed as an arg, I prefere
        # splitting functionality to be more clear about what's going on. We'll see how that goes!
        for obstacle_sprite in self.obstacle_sprites:
            # Is there some collision between the obstacle and the sprite?
            if obstacle_sprite.hitbox.colliderect(self.hitbox):
                # We assume that the collision is happening in the direction of the player movement
                # Because the obstacles are static
                if self.direction.x > 0:  # we are moving right
                    self.hitbox.right = obstacle_sprite.hitbox.left  # stick the player to the obstacle boundary
                if self.direction.x < 0:  # we are moving left
                    self.hitbox.left = obstacle_sprite.hitbox.right

    def collision_y(self):
        for obstacle_sprite in self.obstacle_sprites:
            # Is there some collision between the obstacle and the sprite?
            if obstacle_sprite.hitbox.colliderect(self.hitbox):
                # We assume that the collision is happening in the direction of the player movement
                # Because the obstacles are static
                if self.direction.y > 0:  # we are moving down
                    self.hitbox.bottom = obstacle_sprite.hitbox.top  # stick the player to the obstacle boundary
                if self.direction.y < 0:  # we are moving up
                    self.hitbox.top = obstacle_sprite.hitbox.bottom
