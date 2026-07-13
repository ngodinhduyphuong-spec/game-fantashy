import pygame
from config import *

class MenuState:
    def __init__(self):
        self.options = ["New Game", "Load Game", "Settings", "Exit"]
        self.selected = 0
        self.font_large = pygame.font.Font(None, 72)
        self.font_medium = pygame.font.Font(None, 48)
    
    def handle_event(self, event, game):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected = (self.selected - 1) % len(self.options)
            elif event.key == pygame.K_DOWN:
                self.selected = (self.selected + 1) % len(self.options)
            elif event.key == pygame.K_RETURN:
                self.select_option(game)
    
    def select_option(self, game):
        if self.selected == 0:  # New Game
            from game_states.exploring import ExploringState
            game.change_state(ExploringState())
        elif self.selected == 3:  # Exit
            import sys
            sys.exit()
    
    def update(self, game):
        pass
    
    def draw(self, screen):
        # Draw title
        title = self.font_large.render("FINAL FANTASY", True, YELLOW)
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 100))
        screen.blit(title, title_rect)
        
        # Draw subtitle
        subtitle_font = pygame.font.Font(None, 32)
        subtitle = subtitle_font.render("RPG Game", True, CYAN)
        subtitle_rect = subtitle.get_rect(center=(SCREEN_WIDTH // 2, 180))
        screen.blit(subtitle, subtitle_rect)
        
        # Draw menu options
        for i, option in enumerate(self.options):
            color = YELLOW if i == self.selected else WHITE
            text = self.font_medium.render(option, True, color)
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, 300 + i * 80))
            screen.blit(text, text_rect)
            
            # Draw selector
            if i == self.selected:
                selector = self.font_medium.render("> ", True, YELLOW)
                selector_rect = selector.get_rect(right=text_rect.left - 20, centery=text_rect.centery)
                screen.blit(selector, selector_rect)
