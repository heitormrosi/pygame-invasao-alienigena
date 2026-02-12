import sys

import pygame
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from bullet import Bullet

def check_events(
        ai_settings: Settings, 
        screen: pygame.Surface, 
        ship: Ship, 
        bullets: Group
        ) -> None:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(
                    event, 
                    ai_settings,
                    screen,
                    ship,
                    bullets
                )
            elif event.type == pygame.KEYUP:
                check_keyup_events(event, ship)


def check_keydown_events(
        event: pygame.event.Event, 
        ai_settings: Settings, 
        screen: pygame.Surface, 
        ship: Ship, 
        bullets: Group
        ) -> None:
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_SPACE:
        fire_bullet(
            ai_settings,
            screen,
            ship,
            bullets
        )


def check_keyup_events(event: pygame.event.Event, ship: Ship) -> None:
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(
          ai_settings: Settings, 
          screen: pygame.Surface, 
          ship: Ship, 
          bullets: Group
          ) -> None:
    screen.fill(ai_settings.bg_color)
    
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Renderiza a espaçonave na tela
    ship.blitme()
    
    # Atualiza a renderização da janela
    pygame.display.flip()

def update_bullets(bullets):
    """ Atualiza a posição dos projéteis e se livra dos projéteis antigos. """

    # Atualiza as posições dos projéteis 
    bullets.update()
    # Livra-se dos projéteis que desapareceram 
    for bullet in bullets.copy(): 
        if bullet.rect.bottom <= 0: 
            bullets.remove(bullet)


def fire_bullet(
        ai_settings: Settings,
        screen: pygame.Surface,
        ship: Ship,
        bullets: Group
        ) -> None:
    if len(bullets) < ai_settings.bullets_allowed:
        bullets.add(
            Bullet(
                ai_settings,
                screen,
                ship
            )
        )