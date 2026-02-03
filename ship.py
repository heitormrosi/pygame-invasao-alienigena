import pygame

class Ship:
    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        
        # Alinha o retângulo da espaçonave com o retângulo da janela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    
    def blitme(self) -> None:
        self.screen.blit(self.image, self.rect)