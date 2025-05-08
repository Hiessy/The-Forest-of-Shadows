# src/renderer.py
import pygame
import sys

TILE_SIZE = 40
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BG_COLOR = (30, 30, 30)
WALL_COLOR = (100, 100, 255)
FOV_COLOR = (180, 180, 180)

class Renderer:
    def __init__(self, world, player):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Dungeon RPG View")
        self.clock = pygame.time.Clock()
        self.world = world
        self.player = player

    def draw_world(self):
        self.screen.fill(BG_COLOR)

        px, py = self.player.position
        direction = self.player.direction  # e.g., 'N', 'E', 'S', 'W'

        # Draw simple "forward-facing" 3 blocks based on direction
        visible_tiles = self.get_visible_tiles(px, py, direction)
        for pos in visible_tiles:
            x, y = pos
            if self.world[y][x] == 'W':
                pygame.draw.rect(self.screen, WALL_COLOR, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            else:
                pygame.draw.rect(self.screen, FOV_COLOR, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)

    def get_visible_tiles(self, x, y, direction):
        tiles = []
        if direction == 'N':
            tiles = [(x, y-1), (x-1, y-1), (x+1, y-1)]
        elif direction == 'S':
            tiles = [(x, y+1), (x-1, y+1), (x+1, y+1)]
        elif direction == 'E':
            tiles = [(x+1, y), (x+1, y-1), (x+1, y+1)]
        elif direction == 'W':
            tiles = [(x-1, y), (x-1, y-1), (x-1, y+1)]
        return [tile for tile in tiles if 0 <= tile[0] < len(self.world[0]) and 0 <= tile[1] < len(self.world)]

    def run(self):
        while True:
            self.handle_events()
            self.draw_world()
            pygame.display.flip()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
