import pygame

from alien import Alien

class Fleet:
    #A class to represent the alien fleet.

    def __init__(self, ai_game):
        #Create the fleet of aliens.

        #Create an alien and find the number of aliens in a row.
        #Spacing between each alien is equal to one alien width.
        self.settings = ai_game.settings
        self.alien = ai_game.alien
        self.ship = ai_game.ship

    def create_fleet(self):
        alien_fleet = pygame.sprite.Group()
        #create the full fleet of aliens.
        for row_number in range(self._number_rows()):
            for alien_number in range(self._number_aliens()):
                alien = Alien(self.alien)
                alien.create_alien(alien_number, row_number)
                alien_fleet.add(alien)
        return alien_fleet

    def _number_rows(self):
        #Determine the number of rows of aliens that fit on the screen.
        alien_height = self.alien.rect.height
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        return number_rows

    def _number_aliens(self):
        alien_width = self.alien.rect.width
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        return number_aliens_x