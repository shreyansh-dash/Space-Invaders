import sys
import pygame

def check_events(ship):
    """Respond to keyboard and mouse input"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:

            # Move the ship to right
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            

def update_screen(ai_settings, screen, ship):
    """Update images on the screen and flip to the new screen"""

    # Redraw the screen every time in an infinte loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    #Show the most recently updated screen
    pygame.display.flip()