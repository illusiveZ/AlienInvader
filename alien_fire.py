import pygame
from pygame.sprite import Sprite

class AlienFire(Sprite):
    """Control the bullets that are fired by the alien ships"""
    def __init__(self, ai_settings, screen, alien):
        super().__init__()
        self.screen = screen

        # Create the bullet in position (0, 0) and set right position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = alien.rect.centerx
        self.rect.bottom = alien.rect.bottom

        # Store as a float
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.alien_fire_speed_factor

    def update(self):
        """Move bullet down the screen"""
        self.y += self.speed_factor
        # Update the rect posn
        self.rect.y = self.y

    def draw_alien_bullet(self):
        """Draw the alien bullet"""
        pygame.draw.rect(self.screen, self.color, self.rect)