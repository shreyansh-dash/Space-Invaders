import pygame 

class Ship():
    def __init__(self, screen):
        """Initialize the ship and its starting position"""
        self.screen = screen

        # Load the image and get its coordinates
        self.image = pygame.image.load('assets/logo.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Start new ship at the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Assuming the ship is not moving
        self.moving_right = False

    def update(self):
        """Update the position of the ship based on the keyboard input"""        
        if self.moving_right:
            self.rect.centerx += 1

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)


