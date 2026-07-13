import pygame
from config import *

class Enemy:
    def __init__(self, name, hp, mp, atk, def_, spd):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.atk = atk
        self.def_ = def_
        self.spd = spd
        self.x = 0
        self.y = 0
        self.width = 32
        self.height = 32
    
    def draw(self, screen):
        """Draw enemy sprite"""
        pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))
        
        # Draw eyes
        pygame.draw.circle(screen, BLACK, (self.x + 8, self.y + 8), 2)
        pygame.draw.circle(screen, BLACK, (self.x + 24, self.y + 8), 2)
        
        # Draw name
        font = pygame.font.Font(None, 18)
        name_text = font.render(self.name, True, WHITE)
        screen.blit(name_text, (self.x - 5, self.y - 20))
