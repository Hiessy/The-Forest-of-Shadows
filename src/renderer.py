import pygame

TILE_SIZE = 64
WINDOW_WIDTH, WINDOW_HEIGHT = TILE_SIZE * 5, TILE_SIZE * 5

class Renderer:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("The Forest of Shadows")
        self.font = pygame.font.SysFont('Arial', 18)

    def draw_world(self, player_pos):
        self.screen.fill((0, 0, 0))  # Black background

        # Draw a simple grid and mark the player
        for x in range(5):
            for y in range(5):
                rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(self.screen, (50, 50, 50), rect, 1)

        # Draw the player in the center
        player_rect = pygame.Rect(2 * TILE_SIZE, 2 * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        pygame.draw.rect(self.screen, (0, 255, 0), player_rect)

    def draw_text(self, lines):
        for i, line in enumerate(lines):
            text_surface = self.font.render(line, True, (255, 255, 255))
            self.screen.blit(text_surface, (10, WINDOW_HEIGHT - 100 + i * 20))

    def update(self, player_pos, log=[]):
        self.draw_world(player_pos)
        self.draw_text(log)
        pygame.display.flip()

    def quit(self):
        pygame.quit()
