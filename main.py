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
        selected_loop = 3
        return True
    else:
        return False


def track_points() -> int:
    if player.check_collision(Comet.comet, True):
        return 100 + clock.tick()
    else:
        return clock.tick()


def game_loop() -> None:
    global points
    variable_rate = ASTEROIDSPAWNRATE
    cooldown = variable_rate
    Comet.create_comet(SCREEN)
    player.set_pos([window_size[0] // 2, window_size[1] // 5 * 4])
    Asteroid.asteroids.empty()
    while True:
        clock.tick(FPSCAP)
        check_quit_conditions()

        SCREEN.fill((0, 0, 0))
        cooldown -= 1
        print(variable_rate)
        if cooldown <= 0:
            Asteroid.add_asteroid(Asteroid(SCREEN))
            cooldown = variable_rate

            if variable_rate > ASTEROIDSPAWNCAP:
                variable_rate -= clock.get_rawtime()

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
    play_button_active = Button(
        play_button_colour_active, play_button_size, play_button_pos, play_button_text
    )
    play_button_passive = Button(
        play_button_colour_passive, play_button_size, play_button_pos, play_button_text
    )

    designer_button_colour_active = pygame.Color(0, 255, 0)
    designer_button_colour_passive = pygame.Color(0, 207, 0)
    designer_button_size = play_button_size
    designer_button_pos = (play_button_pos[0], window_size[1] // 4 * 3)
    designer_button_text = "Enter rocket designer"
    designer_button_active = Button(
        designer_button_colour_active,
        designer_button_size,
        designer_button_pos,
        designer_button_text,
    )
    designer_button_passive = Button(
        designer_button_colour_passive,
        designer_button_size,
        designer_button_pos,
        designer_button_text,
    )

    button_selected = 2
    while True:
        clock.tick()
        check_quit_conditions()
        SCREEN.fill((0, 0, 0))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            pygame.time.delay(200)
            button_selected += 1
        elif keys[pygame.K_w]:
            pygame.time.delay(200)
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


def get_high_scores() -> dict:
    with open("highScores.json", "r") as file:
        data = json.load(file)
        return data


def set_high_scores(obj):
    with open("highScores.json", "w") as file:
        json.dump(obj, file)


def scoreboard_loop() -> None:
    global selected_loop, points
    leaderboard_text = Text(window_size[0] // 56, FONT)
    text_colour = pygame.Color(255, 255, 255)
    scores = get_high_scores()
    while True:
        check_quit_conditions()

        clock.tick()

        SCREEN.fill((0, 0, 0))

        keys = pygame.key.get_pressed()

        leaderboard_text.display(
            "Game over!",
            [window_size[0] // 2, window_size[1] // 12],
            text_colour,
            SCREEN,
        )
        leaderboard_text.display(
            "High scores:",
            [window_size[0] // 2, window_size[1] // 12 * 2],
            text_colour,
            SCREEN,
        )
        leaderboard_text.display(
            "Press backspace to return",
            [window_size[0] // 2, window_size[1] // 12 * 11],
            text_colour,
            SCREEN,
        )
        leaderboard_text.display(
            f"Your score: {points}",
            [window_size[0] // 2, window_size[1] // 12 * 10],
            text_colour,
            SCREEN,
        )

        tmp = 3
        for i in scores.items():
            if tmp >= 8:
                break
            tmp += 1
            leaderboard_text.display(
                f"{i[0]} : {i[1]}",
                [window_size[0] // 2, window_size[1] // 12 * tmp],
                text_colour,
                SCREEN,
            )

        if keys[pygame.K_BACKSPACE]:
            if scores.get(os.getlogin(), 0) < points:
                scores[os.getlogin()] = points
            set_high_scores(scores)
            selected_loop = 0
            points = 0
            break

        pygame.display.flip()


def rocket_designer_loop():
    global selected_loop

    top_selected = 0
    middle_selected = 0
    engine_selected = 0
    level_selected = 0

    component_size = (window_size[0] // COMPONENTRESIZEVAL, window_size[0] // COMPONENTRESIZEVAL)

    while True:
        check_quit_conditions()

        SCREEN.fill((0,0,0))

        # select level
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            pygame.time.delay(200)
            if level_selected < 2:
                level_selected += 1
            else:
                level_selected = 0
        if keys[pygame.K_s]:
            pygame.time.delay(200)
            if level_selected > 0:
                level_selected -= 1
            else:
                level_selected = 2

        # select component
        match level_selected:
            case 0:
                if keys[pygame.K_d]:
                    pygame.time.delay(200)
                    if top_selected < 2:
                        top_selected += 1
                    else:
                        top_selected = 0
                if keys[pygame.K_a]:
                    pygame.time.delay(200)
                    if top_selected < 0:
                        top_selected -= 1
                    else:
                        top_selected = 2
            case 1:
                if keys[pygame.K_d]:
                    pygame.time.delay(200)
                    if middle_selected < 2:
                        middle_selected += 1
                    else:
                        middle_selected = 0
                if keys[pygame.K_a]:
                    pygame.time.delay(200)
                    if middle_selected < 0:
                        middle_selected -= 1
                    else:
                        middle_selected = 2
            case 2:
                if keys[pygame.K_d]:
                    pygame.time.delay(200)
                    if engine_selected < 2:
                        engine_selected += 1
                    else:
                        engine_selected = 0
                if keys[pygame.K_a]:
                    pygame.time.delay(200)
                    if engine_selected < 0:
                        engine_selected -= 1
                    else:
                        engine_selected = 2
        
        print(level_selected, top_selected, middle_selected, engine_selected)

        # get the selected component
        top_component = COMPONENTS["top level"][top_selected]
        middle_component = COMPONENTS["middle level"][middle_selected]
        engine_component = COMPONENTS["engine"][engine_selected]

        # Get the necessary information for displaying
        top_component_skin = pygame.image.load(top_component.skin)
        top_component_skin = pygame.transform.scale(top_component_skin, component_size)
        middle_component_skin = pygame.image.load(middle_component.skin)
        middle_component_skin = pygame.transform.scale(middle_component_skin, component_size)
        engine_component_skin = pygame.image.load(engine_component.skin)
        engine_component_skin = pygame.transform.scale(engine_component_skin, component_size)

        SCREEN.blit(top_component_skin, top_component_skin.get_rect(center=(window_size[0] // 2, window_size[1] // 5 + 128)))
        SCREEN.blit(middle_component_skin, middle_component_skin.get_rect(center=(window_size[0] // 2, window_size[1] // 5 * 2 + 128)))
        SCREEN.blit(engine_component_skin, engine_component_skin.get_rect(center=(window_size[0] // 2, window_size[1] // 5 * 3 + 128)))

        pygame.display.flip()


if __name__ == "__main__":
    while True:
        match selected_loop:
            case 0:
                main_menu_loop()
            case 1:
                game_loop()
            case 2:
                rocket_designer_loop()
            case 3:
                scoreboard_loop()
