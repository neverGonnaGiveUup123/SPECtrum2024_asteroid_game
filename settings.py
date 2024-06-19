from component import Component

# set to (0,0) to make it fullscreen
WINDOWSIZE = (0, 0)

# starting spawn rate for the asteroids
ASTEROIDSPAWNRATE = 50

# minimum allowed cooldown for asteroid spawning
ASTEROIDSPAWNCAP = 12

# max fps
FPSCAP = 60

FONT = "PressStart2P-vaV7.ttf"

# set the values for all the components in the rocket designer
COMPONENTS = {
    "top level" : [
        Component("blueSquare.png", "Research module. More points, bigger hitbox", points_multiplier=0.2), 
        Component("greenSquare.png", "Compact. Less points, smaller hitbox", points_multiplier= -0.2), 
        Component("redSquare.png", "Regular. Normal aspects")
        ],
    "middle level" : [
        Component("blueSquare.png", "Research module. Reduced velocity, more points", velocity=-120 // FPSCAP, points_multiplier=0.2), 
        Component("greenSquare.png", "Compact. Increased velocity, less points", velocity=120 // FPSCAP, points_multiplier=-0.2), 
        Component("redSquare.png", "Regular. Normal aspects")
        ],
    "engine" : [
        Component("blueSquare.png", "small engine", velocity=420 // FPSCAP), 
        Component("greenSquare.png", "medium engine", velocity=570 // FPSCAP), 
        Component("redSquare.png", "large engine", velocity=720 // FPSCAP)
        ],
    "weapons" : [
        Component("redSquare.png", "Machine guns. Low damage, fast firerate"), 
        Component("blueSquare.png", "Death ray. Big damage, long reload.")
        ]
}

# how big each component is. Bigger number = smaller
COMPONENTRESIZEVAL = 8