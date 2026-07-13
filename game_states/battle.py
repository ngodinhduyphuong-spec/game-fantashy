import pygame
import random
from config import *
from characters.player import Player
from enemies.enemy import Enemy

class BattleState:
    def __init__(self):
        # Initialize party
        self.player = Player(100, 100)
        self.enemies = [
            Enemy("Goblin", hp=30, mp=10, atk=5, def_=2, spd=6),
            Enemy("Orc", hp=50, mp=15, atk=8, def_=3, spd=5)
        ]
        
        self.font_large = pygame.font.Font(None, 36)
        self.font_medium = pygame.font.Font(None, 28)
        self.font_small = pygame.font.Font(None, 20)
        
        self.battle_log = ["Battle started!", "Choose your action:"]
        self.selected_action = 0
        self.actions = ["Attack", "Magic", "Item", "Run"]
        self.turn_phase = "player_action"  # player_action, enemy_turn, battle_end
        self.battle_over = False
        self.player_won = False
    
    def handle_event(self, event, game):
        if event.type == pygame.KEYDOWN:
            if self.turn_phase == "player_action":
                if event.key == pygame.K_UP:
                    self.selected_action = (self.selected_action - 1) % len(self.actions)
                elif event.key == pygame.K_DOWN:
                    self.selected_action = (self.selected_action + 1) % len(self.actions)
                elif event.key == pygame.K_RETURN:
                    self.execute_player_action()
            
            elif self.battle_over and event.key == pygame.K_RETURN:
                from game_states.menu import MenuState
                game.change_state(MenuState())
    
    def execute_player_action(self):
        action = self.actions[self.selected_action]
        
        if action == "Attack":
            target = random.choice(self.enemies)
            damage = max(1, self.player.atk - target.def_ + random.randint(-3, 3))
            target.hp -= damage
            self.battle_log.append(f"Player attacks {target.name} for {damage} damage!")
            
            if target.hp <= 0:
                self.enemies.remove(target)
                self.battle_log.append(f"{target.name} defeated!")
        
        elif action == "Magic":
            if self.player.mp >= 10:
                self.player.mp -= 10
                damage = 20
                for enemy in self.enemies:
                    enemy.hp -= damage
                self.battle_log.append(f"Player cast Fireball! Dealt {damage} damage to all!")
            else:
                self.battle_log.append("Not enough MP!")
                return
        
        elif action == "Run":
            self.battle_over = True
            self.player_won = False
            self.battle_log.append("Escaped from battle!")
            return
        
        # Check if all enemies defeated
        if len(self.enemies) == 0:
            self.battle_over = True
            self.player_won = True
            self.battle_log.append("Victory!")
            return
        
        # Enemy turn
        self.turn_phase = "enemy_turn"
    
    def update(self, game):
        if self.turn_phase == "enemy_turn":
            for enemy in self.enemies:
                damage = max(1, enemy.atk - self.player.def_ + random.randint(-2, 2))
                self.player.hp -= damage
                self.battle_log.append(f"{enemy.name} attacks for {damage} damage!")
            
            if self.player.hp <= 0:
                self.battle_over = True
                self.player_won = False
                self.battle_log.append("You have been defeated!")
            else:
                self.turn_phase = "player_action"
    
    def draw(self, screen):
        screen.fill(BLACK)
        
        # Draw background
        pygame.draw.rect(screen, (50, 50, 100), (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
        
        # Draw player status
        player_y = 50
        player_text = self.font_large.render("You", True, YELLOW)
        screen.blit(player_text, (50, player_y))
        
        hp_text = self.font_small.render(f"HP: {self.player.hp}/{self.player.max_hp}", True, RED)
        screen.blit(hp_text, (50, player_y + 40))
        
        mp_text = self.font_small.render(f"MP: {self.player.mp}/{self.player.max_mp}", True, BLUE)
        screen.blit(mp_text, (50, player_y + 60))
        
        # Draw enemies
        for i, enemy in enumerate(self.enemies):
            enemy_y = 50 + i * 150
            enemy_text = self.font_large.render(enemy.name, True, RED)
            screen.blit(enemy_text, (SCREEN_WIDTH - 300, enemy_y))
            
            hp_text = self.font_small.render(f"HP: {enemy.hp}/{enemy.max_hp}", True, RED)
            screen.blit(hp_text, (SCREEN_WIDTH - 300, enemy_y + 40))
        
        # Draw battle log
        log_y = SCREEN_HEIGHT // 2 + 50
        log_title = self.font_medium.render("Battle Log:", True, WHITE)
        screen.blit(log_title, (50, log_y - 40))
        
        for i, log_entry in enumerate(self.battle_log[-5:]):
            log_text = self.font_small.render(log_entry, True, WHITE)
            screen.blit(log_text, (50, log_y + i * 25))
        
        # Draw action menu
        if not self.battle_over:
            menu_y = SCREEN_HEIGHT - 150
            menu_title = self.font_medium.render("Choose Action:", True, YELLOW)
            screen.blit(menu_title, (50, menu_y))
            
            for i, action in enumerate(self.actions):
                color = YELLOW if i == self.selected_action else WHITE
                action_text = self.font_small.render(action, True, color)
                screen.blit(action_text, (50 + i * 150, menu_y + 40))
        
        # Draw battle end message
        if self.battle_over:
            if self.player_won:
                end_text = self.font_large.render("VICTORY!", True, GREEN)
            else:
                end_text = self.font_large.render("GAME OVER!", True, RED)
            
            end_rect = end_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            screen.blit(end_text, end_rect)
            
            continue_text = self.font_small.render("Press ENTER to continue", True, WHITE)
            continue_rect = continue_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 80))
            screen.blit(continue_text, continue_rect)
