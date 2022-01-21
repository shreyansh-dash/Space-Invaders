import pygame 

class Ship():
    def __init__(self, ai_settings, screen):
        """Initialize the ship and its starting position"""
        self.screen = screen 
        self.ai_settings = ai_settings

        # Load the image and get its coordinates
        self.image = pygame.image.load('assets/logo.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Start new ship at the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store the value of ship's center as a decimal value
        self.center = float(self.rect.centerx)

        # Assuming the ship is not moving
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the position of the ship based on the keyboard input"""        
        
        # Update ship's center coordinate
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Update rect object from self.object
        self.rect.centerx = self.center


    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)


