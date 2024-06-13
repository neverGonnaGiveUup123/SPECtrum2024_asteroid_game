import sys
import os
import pygame
import json
from settings import *
from rocket import Rocket
from asteroid import Asteroid
from comet import Comet
from widgets import Button, Text

pygame.init()

SCREEN = pygame.display.set_mode(WINDOWSIZE)

window_size = pygame.display.get_window_size()

clock = pygame.time.Clock()

player = Rocket(SCREEN)

points = 0

selected_loop = 0

def check_quit_conditions() -> None:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()

def check_lose_conditions() -> None:
    global selected_loop
    if player.check_collision(Asteroid.get_asteroids(), False):
        print(f"You lose! Points gained: {pygame.time.get_ticks() + points}")
        selected_loop = 2
        return True
    else:
        return False

def track_points() -> int:
    if player.check_collision(Comet.comet, True):
        return 10000
    else:
        return 0

def game_loop() -> None:
    global points
    cooldown = ASTEROIDSPAWNRATE
    Comet.create_comet(SCREEN)
    while True:
        clock.tick(FPSCAP)

        check_quit_conditions()

        SCREEN.fill((0,0,0))
        cooldown -= 1
        # print(cooldown)
        if cooldown <= 0:
            Asteroid.add_asteroid(Asteroid(SCREEN))
            cooldown = ASTEROIDSPAWNRATE
            cooldown -= pygame.time.get_ticks() // 1000

        Asteroid.update_all()
        if Comet.comet_exists():
            Comet.update_comet()
        else:
            Comet.create_comet(SCREEN)
            
        player.update()
        points += track_points()

        if check_lose_conditions():
            break

        pygame.display.flip()

def main_menu_loop() -> None:
    global selected_loop

    play_button_colour_active = pygame.Color(255, 0, 0)
    play_button_colour_passive = pygame.Color(207, 0, 0)
    play_button_size = (window_size[0] // 2, window_size[1] // 8)
    play_button_pos = (window_size[0] // 2, window_size[1] // 2)
    play_button_text = "Start game"
    play_button_active = Button(play_button_colour_active, play_button_size, play_button_pos, play_button_text)
    play_button_passive = Button(play_button_colour_passive, play_button_size, play_button_pos, play_button_text)

    designer_button_colour_active = pygame.Color(0,255,0)
    designer_button_colour_passive = pygame.Color(0,207,0)
    designer_button_size = play_button_size
    designer_button_pos = (play_button_pos[0], window_size[1] // 4 * 3)
    designer_button_text = "Enter rocket designer"
    designer_button_active = Button(designer_button_colour_active, designer_button_size, designer_button_pos, designer_button_text)
    designer_button_passive = Button(designer_button_colour_passive, designer_button_size, designer_button_pos, designer_button_text)

    button_selected = 2
    while True:
        clock.tick(8)
        check_quit_conditions()
        SCREEN.fill((0,0,0))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            button_selected += 1
        elif keys[pygame.K_w]:
            button_selected -= 1
        
        if button_selected % 2 == 0:
            play_button_active.display(SCREEN)
            designer_button_passive.display(SCREEN)
            if keys[pygame.K_RETURN]:
                selected_loop = 1
                break
        else:
            play_button_passive.display(SCREEN)
            designer_button_active.display(SCREEN)
            if keys[pygame.K_RETURN]:
                selected_loop = 2
                break
        
        pygame.display.flip()

def get_high_scores():
    with open("highScores.json", 'r') as file:
        data = json.load(file)
        print(data)

def scoreboard_loop() -> None:
    global selected_loop
    leaderboard_text = Text(window_size[0] // 56, FONT)
    text_colour = pygame.Color(255,255,255)
    get_high_scores()
    while True:
        check_quit_conditions()

        SCREEN.fill((0,0,0))

        keys = pygame.key.get_pressed()

        leaderboard_text.display("Game over!", [window_size[0] // 2, window_size[1] // 12], text_colour, SCREEN)
        leaderboard_text.display("Press backspace to return", [window_size[0] // 2, window_size[1] // 12 * 11], text_colour, SCREEN)

        if keys[pygame.K_BACKSPACE]:
            selected_loop = 0
            break

        pygame.display.flip()

if __name__ == "__main__":
    while True:
        match selected_loop:
            case 0:
                main_menu_loop()
            case 1:
                game_loop()
            case 2:
                scoreboard_loop()