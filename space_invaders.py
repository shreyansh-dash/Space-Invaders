# Importing the neccesary modules
import sys
import pygame 
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #Initialize the game
    pygame.init()
    ai_settings = Settings()

    # Specifying the screen dimensions
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    #Title of the window
    pygame.display.set_caption("Space Invaders")

    # Make a ship
    ship = Ship(ai_settings, screen)

    # While Loop to update screen action.
    while True:
        # Wait for a keyboard input
        gf.check_events(ship)

        # Update the motion of the ship based on the keyboard input
        ship.update()
        
        # Filling the background with the color mentioned in the tuple bg_color
        gf.update_screen(ai_settings, screen, ship)



#Run the game
if __name__ == "__main__":
    run_game()