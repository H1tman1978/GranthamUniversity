import pygame as pg
from settings import *


class GameSprite(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def move(self, dx=0, dy=0):
        if not self.collide_with_walls(dx, dy):
            self.x += dx
            self.y += dy

    def collide_with_walls(self, dx=0, dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE


class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


class Mountain(Wall):
    def __init__(self, game, x, y):
        Wall.__init__(self, game, x, y)
        self.image.fill(MOUNTAIN)


class Ocean(Wall):
    def __init__(self, game, x, y):
        Wall.__init__(self, game, x, y)
        self.image.fill(OCEAN)


class Forest(Wall):
    def __init__(self, game, x, y):
        Wall.__init__(self, game, x, y)
        self.image.fill(FOREST)


class River(Wall):
    def __init__(self, game, x, y):
        Wall.__init__(self, game, x, y)
        self.image.fill(RIVER)


class Terrain(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.terrain
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(BROWN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


class Grass(Terrain):
    def __init__(self, game, x, y):
        Terrain.__init__(self, game, x, y)
        self.image.fill(GRASS)


class Beach(Terrain):
    def __init__(self, game, x, y):
        Terrain.__init__(self, game, x, y)
        self.image.fill(BEACH)


class Road(Terrain):
    def __init__(self, game, x, y):
        Terrain.__init__(self, game, x, y)
        self.image.fill(ROAD)


class Bridge(Road):
    def __init__(self, game, x, y):
        Road.__init__(self, game, x, y)
        self.image.fill(BLACK)
