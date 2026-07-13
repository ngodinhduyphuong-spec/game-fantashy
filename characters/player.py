import pygame
from config import *

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 32
        self.height = 32
        
        # Stats
        self.name = "Hero"
        self.max_hp = 150
        self.hp = 150
        self.max_mp = 80
        self.mp = 80
        self.atk = 12
        self.def_ = 6
        self.spd = 9
        self.level = 1
        self.exp = 0
    
    def move(self, dx, dy):
        """Move player on map"""
        new_x = self.x + dx * TILE_SIZE
        new_y = self.y + dy * TILE_SIZE
        
        # Boundary check
        if 0 <= new_x < SCREEN_WIDTH - self.width and 0 <= new_y < SCREEN_HEIGHT - self.height:
            self.x = new_x
            self.y = new_y
    
    def update(self):
        """Update player state"""
        # Regenerate MP slowly
        if self.mp < self.max_mp:
            self.mp += 0.1
    
    def draw(self, screen):
        """Draw player character"""
        # Draw simple player sprite
        pygame.draw.rect(screen, YELLOW, (self.x, self.y, self.width, self.height))
        
        # Draw eyes
        pygame.draw.circle(screen, BLACK, (self.x + 8, self.y + 8), 2)
        pygame.draw.circle(screen, BLACK, (self.x + 24, self.y + 8), 2)
        
        # Draw name above
        font = pygame.font.Font(None, 18)
        name_text = font.render(self.name, True, WHITE)
        screen.blit(name_text, (self.x - 5, self.y - 20))
