# Zelda Game in Python
Using Pygame

Using this project as way to learn some game development concepts

<https://www.youtube.com/watch?v=QU1pPzEGrqw&t=225s>

## Level class

this needs to be able to efficiently manage all the sprites for the level, including the map, player, enegmies etc.

Everything will be grouped as either "visible" or "obstacle"

visible
- drawn sprites
- player can collide with these

Obstacle
- static sprites (drawn once)
- player cannot collide with these

## Sprite Group

stores a group of sprites
calls update method and draw methods of all the sprites

### draw

calls the `blit` method of all sprites with the image and the rect (size and pos) of the sprite