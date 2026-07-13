import pygame
from config import *
from characters.player import Player
from world.map import GameMap

class ExploringState:
    def __init__(self):
        self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.game_map = GameMap()
        self.font = pygame.font.Font(None, 24)
        self.message = ""
        self.message_timer = 0
    
    def handle_event(self, event, game):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.player.move(0, -1)
            elif event.key == pygame.K_DOWN:
                self.player.move(0, 1)
            elif event.key == pygame.K_LEFT:
                self.player.move(-1, 0)
            elif event.key == pygame.K_RIGHT:
                self.player.move(1, 0)
            elif event.key == pygame.K_SPACE:
                self.check_interaction(game)
            elif event.key == pygame.K_b:
                # Start battle for testing
                from game_states.battle import BattleState
                game.change_state(BattleState())
    
    def check_interaction(self, game):
        self.message = "You found an item!"
        self.message_timer = 120
    
    def update(self, game):
        self.player.update()
        if self.message_timer > 0:
            self.message_timer -= 1
    
    def draw(self, screen):
        # Draw background
        screen.fill((34, 139, 34))  # Forest green
        
        # Draw simple grid map
        for x in range(0, SCREEN_WIDTH, TILE_SIZE):
            pygame.draw.line(screen, (0, 100, 0), (x, 0), (x, SCREEN_HEIGHT), 1)
        for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
            pygame.draw.line(screen, (0, 100, 0), (0, y), (SCREEN_WIDTH, y), 1)
        
        # Draw player
        self.player.draw(screen)
        
        # Draw UI
        ui_text = self.font.render(f"HP: {self.player.hp}/{self.player.max_hp} | MP: {self.player.mp}/{self.player.max_mp}", True, WHITE)
        screen.blit(ui_text, (10, 10))
        
        # Draw controls
        controls = [
            "Arrow Keys: Move",
            "Space: Interact",
            "B: Battle",
            "ESC: Menu"
        ]
        for i, ctrl in enumerate(controls):
            text = self.font.render(ctrl, True, WHITE)
            screen.blit(text, (10, SCREEN_HEIGHT - 100 + i * 25))
        
        # Draw message
        if self.message_timer > 0:
            msg = self.font.render(self.message, True, YELLOW)
            msg_rect = msg.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 30))
            pygame.draw.rect(screen, BLACK, msg_rect.inflate(20, 10))
            pygame.draw.rect(screen, YELLOW, msg_rect.inflate(20, 10), 2)
            screen.blit(msg, msg_rect)
