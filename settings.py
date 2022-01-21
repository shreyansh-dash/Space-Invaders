class Settings():
    """Class to store settings for Space Invaders"""
    def __init__(self):
        """Initialize the game settings"""
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        # Ship speed 
        self.ship_speed_factor = 1.5

        # Bullet Settings
        self.bullet_speed_factor = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

        