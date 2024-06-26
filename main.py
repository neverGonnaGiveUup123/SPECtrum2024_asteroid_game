import sys
import os
import pygame
import json
from PIL import Image
from settings import *
from src.rocket import Rocket
from src.asteroid import Asteroid
from src.comet import Comet
from src.widgets import Button, Text
from src.weapons.machineGun import MachineGun

pygame.init()

SCREEN = pygame.display.set_mode(WINDOWSIZE)

pygame.mouse.set_visible(False)

window_size = pygame.display.get_window_size()

clock = pygame.time.Clock()

player = Rocket(SCREEN)

points = 0

selected_loop = 0

# set image sizes
explosion = Image.open("src/img/explosion.png")
explosion = explosion.resize((window_size[0] // 7, window_size[0] // 7))
explosion.save("src/img/large_explosion.png")

asteroid_skin = Image.open("src/img/asteroid.png")
small_asteroid_skin = asteroid_skin.resize((window_size[0] // 10, window_size[0] // 10))
medium_asteroid_skin = asteroid_skin.resize((window_size[0] // 8, window_size[0] // 8))
large_asteroid_skin = asteroid_skin.resize((window_size[0] // 5, window_size[0] // 5))
small_asteroid_skin.save("src/img/small_asteroid_skin.png")
medium_asteroid_skin.save("src/img/medium_asteroid_skin.png")
large_asteroid_skin.save("src/img/large_asteroid_skin.png")

bullet = Image.open("src/img/bullet.png")
bullet = bullet.resize((window_size[0] // 50, window_size[0] // 50))
bullet.save("src/img/bullet.png")

def check_quit_conditions() -> None:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            os.remove("src/img/top_component_skin.png")
            os.remove("src/img/middle_component_skin.png")
            os.remove("src/imgengine_component_skin.png")
            os.remove("src/img/combined_components.png")
            pygame.quit()
            sys.exit()
    if keys[pygame.K_ESCAPE]:
        os.remove("src/img/top_component_skin.png")
        os.remove("src/img/middle_component_skin.png")
        os.remove("src/img/engine_component_skin.png")
        os.remove("src/img/combined_components.png")
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
        return 5000 + clock.tick()
    else:
        return clock.tick()


def game_loop() -> None:
    global points
    variable_rate = ASTEROIDSPAWNRATE
    cooldown = variable_rate
    Comet.create_comet(SCREEN)
    player.set_pos([window_size[0] // 2, window_size[1] // 5 * 4])
    Asteroid.asteroids.empty()

    comet_catch = Text(12, "src/PressStart2P-vaV7.ttf")
    tmp = 0
    while True:
        points += clock.tick(FPSCAP)
        check_quit_conditions()

        SCREEN.fill((0, 0, 0))
        cooldown -= 1
        # print(variable_rate)
        if cooldown <= 0:
            Asteroid.add_asteroid(Asteroid(SCREEN))
            cooldown = variable_rate

            if variable_rate > ASTEROIDSPAWNCAP:
                variable_rate -= 0.5

        Asteroid.update_all()
        if Comet.comet_exists():
            Comet.update_comet()
        else:
            Comet.create_comet(SCREEN)

        player.update()

        if player.check_collision(Comet.comet, True):
            points += 5000
            tmp = 7200 // FPSCAP
            pos = player.pos.copy()
        
        if tmp > 0:
            tmp -= 1
            comet_catch.display("+5000", pos, (0,255,0), SCREEN)

        if check_lose_conditions():
            break

        comet_catch.display(f"Score: {points}", [100, 50], (255,255,255), SCREEN)
        comet_catch.display(f"Cooldown: {player.tmp}", [100, 100], (255,255,255), SCREEN)

        pygame.display.flip()


def main_menu_loop() -> None:
    global selected_loop

    play_button_colour_active = pygame.Color(255, 0, 0)
    play_button_colour_passive = pygame.Color(55, 0, 0)
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
    designer_button_colour_passive = pygame.Color(0, 55, 0)
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

    heading = Text(36, "src/PressStart2P-vaV7.ttf")
    sub_text = Text(12, "src/PressStart2P-vaV7.ttf")

    button_selected = 2
    has_not_designed_rocket = False
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
                if os.path.isfile("src/img/combined_components.png"):
                    selected_loop = 1
                    Asteroid.asteroids.empty()
                    MachineGun.bullets.empty()
                    break
                else:
                    has_not_designed_rocket = True
        else:
            play_button_passive.display(SCREEN)
            designer_button_active.display(SCREEN)
            if keys[pygame.K_RETURN]:
                selected_loop = 2
                break
        
        if has_not_designed_rocket:
            sub_text.display("Design a rocket first!", [window_size[0] // 2, window_size[1] // 8 * 3], (255,0,0), SCREEN)

        heading.display("Asteroid Anarchy!", 
                        [window_size[0] // 2, window_size[1] // 5],
                        (0,0,255),
                        SCREEN
                        )
        sub_text.display("A SPECtrum Club game",
                        [window_size[0] // 2, window_size[1] // 8 * 2],
                        (255,255,255),
                        SCREEN
                        )
        sub_text.display("Developed by Siddharth S",
                        [window_size[0] // 2, window_size[1] // 20 * 17],
                        (255,255,255),
                        SCREEN
                        )
        sub_text.display("Press Esc to quit. Controls are WASD",
                        [window_size[0] // 2, window_size[1] // 20 * 18],
                        (255,255,255),
                        SCREEN
                        )

        pygame.display.flip()


def get_high_scores() -> dict:
    with open("src/highScores.json", "r") as file:
        data = json.load(file)
        return data


def set_high_scores(obj):
    with open("src/highScores.json", "w") as file:
        json.dump(obj, file)


def scoreboard_loop() -> None:
    global selected_loop, points
    leaderboard_text = Text(window_size[0] // 56, FONT)
    text_colour = pygame.Color(255, 255, 255)
    points *= player.points_multiplier
    points = round(points)
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
    weapon_selected = 0
    level_selected = 0

    component_size = (window_size[0] // COMPONENTRESIZEVAL, window_size[0] // COMPONENTRESIZEVAL)
    component_text = Text(11, "src/PressStart2P-vaV7.ttf")

    while True:
        check_quit_conditions()

        SCREEN.fill((0,0,0))

        # select level
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            pygame.time.delay(200)
            if level_selected < 3:
                level_selected += 1
            else:
                level_selected = 0
        if keys[pygame.K_w]:
            pygame.time.delay(200)
            if level_selected > 0:
                level_selected -= 1
            else:
                level_selected = 3

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
                    if top_selected > 0:
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
                    if middle_selected > 0:
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
                    if engine_selected > 0:
                        engine_selected -= 1
                    else:
                        engine_selected = 2
            case 3:
                if keys[pygame.K_d]:
                    pygame.time.delay(200)
                    if weapon_selected < 1:
                        weapon_selected += 1
                    else:
                        weapon_selected = 0
                if keys[pygame.K_a]:
                    pygame.time.delay(200)
                    if weapon_selected < 0:
                        weapon_selected -= 1
                    else:
                        weapon_selected = 1
        
        # print(level_selected, top_selected, middle_selected, engine_selected, weapon_selected)

        # get the selected component
        top_component = COMPONENTS["top level"][top_selected]
        middle_component = COMPONENTS["middle level"][middle_selected]
        engine_component = COMPONENTS["engine"][engine_selected]
        weapon_component = COMPONENTS["weapons"][weapon_selected]

        # Get the necessary information for displaying
        top_component_skin = pygame.image.load(top_component.skin)
        top_component_skin = pygame.transform.scale(top_component_skin, component_size)
        middle_component_skin = pygame.image.load(middle_component.skin)
        middle_component_skin = pygame.transform.scale(middle_component_skin, component_size)
        engine_component_skin = pygame.image.load(engine_component.skin)
        engine_component_skin = pygame.transform.scale(engine_component_skin, component_size)
        weapon_component_skin = pygame.image.load(weapon_component.skin)
        weapon_component_skin = pygame.transform.scale(weapon_component_skin, component_size)

        SCREEN.blit(top_component_skin, top_component_skin.get_rect(center=(window_size[0] // 2, window_size[1] // 5 + 64)))
        SCREEN.blit(middle_component_skin, middle_component_skin.get_rect(center=(window_size[0] // 2, window_size[1] // 5 * 2 + 64)))
        SCREEN.blit(engine_component_skin, engine_component_skin.get_rect(center=(window_size[0] // 2, window_size[1] // 5 * 3 + 64)))
        SCREEN.blit(weapon_component_skin, weapon_component_skin.get_rect(center=(window_size[0] // 2, window_size[1] // 5 * 4 + 64)))

        component_text.display(top_component.description, [256, window_size[1] // 5 + 64], (255,255,255), SCREEN)
        component_text.display(middle_component.description, [256, window_size[1] // 5 * 2 + 64], (255,255,255), SCREEN)
        component_text.display(engine_component.description, [256, window_size[1] // 5 * 3 + 64], (255,255,255), SCREEN)
        component_text.display(weapon_component.description, [256, window_size[1] // 5 * 4 + 64], (255,255,255), SCREEN)

        component_text.display("ROCKET DESIGNER", [window_size[0] // 4 * 3, 64], (255,255,255), SCREEN)
        component_text.display("Backspace to exit", [window_size[0] // 4 * 3, 128], (255,255,255), SCREEN)
        component_text.display("Machine gun fires automatically", [window_size[0] // 4 * 3, 192], (255,255,255), SCREEN)
        component_text.display("Spacebar to fire death ray", [window_size[0] // 4 * 3, 256], (255,255,255),SCREEN)

        if keys[pygame.K_BACKSPACE]:
            velocity = top_component.velocity + middle_component.velocity + engine_component.velocity
            points_multiplier = 1 + top_component.points_multiplier + middle_component.points_multiplier

            # converting it into something pillow can understand
            pygame.image.save(top_component_skin, "src/img/top_component_skin.png")
            pygame.image.save(middle_component_skin, "src/img/middle_component_skin.png")
            pygame.image.save(engine_component_skin, "src/img/engine_component_skin.png")

            tcs_img = Image.open("src/img/top_component_skin.png")
            tcs_img = tcs_img.resize((player.size[0], player.size[1] // 3))
            mcs_img = Image.open("src/img/middle_component_skin.png")
            mcs_img = mcs_img.resize((player.size[0], player.size[1] // 3))
            ecs_img = Image.open("src/img/engine_component_skin.png")
            ecs_img = ecs_img.resize((player.size[0], player.size[1] // 3))

            combined_img = Image.new("RGB", player.size)
            combined_img.paste(tcs_img, (0,0))
            combined_img.paste(mcs_img, (0, player.size[1] // 3))
            combined_img.paste(ecs_img, (0, player.size[1] // 3 * 2))
            combined_img.save("src/img/combined_components.png")

            player.import_rocket_designer_vals(velocity, points_multiplier, pygame.image.load("src/img/combined_components.png"), weapon_selected)
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
                rocket_designer_loop()
            case 3:
                scoreboard_loop()
