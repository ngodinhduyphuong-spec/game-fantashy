from config import *

class GameMap:
    def __init__(self):
        self.width = SCREEN_WIDTH // TILE_SIZE
        self.height = SCREEN_HEIGHT // TILE_SIZE
        self.tiles = self.generate_map()
    
    def generate_map(self):
        """Generate simple map"""
        tiles = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                # Simple tile type (0 = grass, 1 = water, 2 = mountain)
                if (x + y) % 3 == 0:
                    row.append(1)  # Water
                else:
                    row.append(0)  # Grass
            tiles.append(row)
        return tiles
    
    def get_tile(self, x, y):
        """Get tile at position"""
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.tiles[y][x]
        return -1
