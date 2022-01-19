# Importing the neccesary modules
import sys
import pygame 
from settings import Settings

def run_game():
    #Initialize the game
    pygame.init()
    ai_settings = Settings()

    # Specifying the screen dimensions
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    #Title of the window
    pygame.display.set_caption("Space Invaders")

    # While Loop to update screen action.
    while True:
        # Wait for a keyboard input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        # Filling the background with the color mentioned in the tuple bg_color
        screen.fill(ai_settings.bg_color)

        # Make the screen visible
        pygame.display.flip()

#Run the game
if __name__ == "__main__":
    run_game()