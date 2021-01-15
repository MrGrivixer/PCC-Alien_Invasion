class Settings:
    """Store all static game settings"""

    def __init__(self):
        """Static settings"""
        self.bg_color = (0, 204, 255)

    def initialize_dynamic_settings(self):
        """Settings that can change"""
        self.player_speed = 2