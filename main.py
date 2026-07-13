import pygame
import sys
from config import *
from game import Game

def main():
    pygame.init()
    
    # Create game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Final Fantasy - RPG Game")
    
    # Create clock for FPS
    clock = pygame.time.Clock()
    
    # Initialize game
    game = Game(screen)
    
    # Main game loop
    running = True
    while running:
        clock.tick(FPS)
        
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            game.handle_event(event)
        
        # Update game
        game.update()
        
        # Draw game
        game.draw()
        
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
