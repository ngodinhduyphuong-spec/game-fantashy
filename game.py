import pygame
from config import *
from game_states.menu import MenuState

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.current_state = MenuState()
        self.font_large = pygame.font.Font(None, 48)
        self.font_medium = pygame.font.Font(None, 36)
        self.font_small = pygame.font.Font(None, 24)
        
    def handle_event(self, event):
        """Handle input events"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                from game_states.exploring import ExploringState
                if isinstance(self.current_state, ExploringState):
                    self.current_state = MenuState()
        
        self.current_state.handle_event(event, self)
    
    def update(self):
        """Update game logic"""
        self.current_state.update(self)
    
    def draw(self):
        """Draw game screen"""
        self.screen.fill(BLACK)
        self.current_state.draw(self.screen)
    
    def change_state(self, new_state):
        """Change game state"""
        self.current_state = new_state
