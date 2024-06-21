from src.component import Component

# set to (0,0) to make it fullscreen
WINDOWSIZE = (0, 0)

# starting spawn rate for the asteroids
ASTEROIDSPAWNRATE = 50

# minimum allowed cooldown for asteroid spawning
ASTEROIDSPAWNCAP = 10

# max fps
FPSCAP = 60

FONT = "src/PressStart2P-vaV7.ttf"

# set the values for all the components in the rocket designer
COMPONENTS = {
    "top level" : [
        Component("src/img/researchModuleHead.png", "Research module. More points, bigger hitbox", points_multiplier=0.2), 
        Component("src/img/compactHead.png", "Compact. Less points, smaller hitbox", points_multiplier= -0.2), 
        Component("src/img/normalHead.png", "Regular. Normal aspects")
        ],
    "middle level" : [
        Component("src/img/researchBody.png", "Research module. Reduced velocity, more points", velocity=-120 // FPSCAP, points_multiplier=0.2), 
        Component("src/img/compactBody.png", "Compact. Increased velocity, less points", velocity=120 // FPSCAP, points_multiplier=-0.2), 
        Component("src/img/normalBody.png", "Regular. Normal aspects")
        ],
    "engine" : [
        Component("src/img/smallEngine.png", "small engine", velocity=420 // FPSCAP), 
        Component("src/img/mediumEngine.png", "medium engine", velocity=570 // FPSCAP), 
        Component("src/img/largeEngine.png", "large engine", velocity=720 // FPSCAP)
        ],
    "weapons" : [
        Component("src/img/redSquare.png", "Machine guns. Low damage, fast firerate"), 
        Component("src/img/blueSquare.png", "Death ray. Big damage, long reload.")
        ]
}

# how big each component is. Bigger number = smaller
COMPONENTRESIZEVAL = 8