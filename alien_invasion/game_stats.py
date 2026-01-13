class GameStats:
    """Track ststisitics for alien invasion"""

    def __init__(self, ai_game):
        """intialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit

    