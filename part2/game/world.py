
import pygame as pg
import random
from .settings import TILE_SIZE



class World:
    #grid_length is the total length of the grid
    def __init__(self, grid_length_x, grid_length_y, width, height): #self.world = World(10, 10, self.width, self.height)
        self.grid_length_x = grid_length_x
        self.grid_length_y = grid_length_y
        self.width = width
        self.height = height

        self.grass_tiles = pg.Surface((width, height)) #create a surface
        self.tiles = self.load_images() #dictionary of images
        self.world = self.create_world() #world to be a double list

    def create_world(self):
        world = []
        #grid_length: total length of the grid

        self.grass_tiles.fill(( 137, 207, 240)) #fill the surface with a color
        for grid_x in range(self.grid_length_x):
            world.append([]) # initiate an empty list then let grid_x run
            for grid_y in range(self.grid_length_y): #let grid_y run
                world_tile = self.grid_to_world(grid_x, grid_y) #create a dictionary
                world[grid_x].append(world_tile) #append the dictionary to the list

                render_pos = world_tile["render_pos"]  #get the render position of the tile
                self.grass_tiles.blit(self.tiles["block"] , (render_pos[0] + self.width/4, render_pos[1] + self.height/4)) #blit(surface, coordinates) to draw the surface with the block image
                #draw the surface with the block image+

        return world

    def grid_to_world(self, grid_x, grid_y):

        rect = [
            (grid_x * TILE_SIZE, grid_y * TILE_SIZE),
            (grid_x * TILE_SIZE + TILE_SIZE, grid_y * TILE_SIZE),
            (grid_x * TILE_SIZE + TILE_SIZE, grid_y * TILE_SIZE + TILE_SIZE),
            (grid_x * TILE_SIZE, grid_y * TILE_SIZE + TILE_SIZE)
        ]

        #coordinate needed for creating a rectangle

        iso_poly = [self.cart_to_iso(x, y) for x, y in rect]

        #convert the coordinate of a rectangle to isometric coordinates

        minx = min([x for x, y in iso_poly])
        miny = min([y for x, y in iso_poly])

        #from there we can get the minimum x and y coordinates

        r = random.randint(1, 100)

        if r <= 10:
            tile = "tree"
        elif 10 < r <= 20:
            tile = "rock"
        else:
            tile = ""

        #randomly assign a tree (10%), rock (10%) or nothing (80%) to the tile

        out = {
            "grid": [grid_x, grid_y],
            "cart_rect": rect,
            "iso_poly": iso_poly,
            "render_pos": [minx, miny], #render position 
            "tile": tile
        }

        return out

    def cart_to_iso(self, x, y):
        iso_x = x - y
        iso_y = (x + y)/2
        return iso_x, iso_y

    def load_images(self):

        block = pg.image.load("assets/graphics/block.png")
        tree = pg.image.load("assets/graphics/tree.png")
        rock = pg.image.load("assets/graphics/rock.png")

        return {"block": block, "tree": tree, "rock": rock}


