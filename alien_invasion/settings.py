from screeninfo import get_monitors

class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the fame's settings."""
        # Screen Settings
        primary_monitor = get_monitors()[0]
        self.screen_width = primary_monitor.width
        self.screen_height = primary_monitor.height
        # self.screen_width = 1200
        # self.screen_height = 800
        self.bg_color = (230, 230, 230) # light gray