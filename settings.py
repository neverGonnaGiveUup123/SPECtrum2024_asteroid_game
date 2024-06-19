from component import Component

WINDOWSIZE = (0, 0)

ASTEROIDSPAWNRATE = 50

ASTEROIDSPAWNCAP = 12

FPSCAP = 60

FONT = "PressStart2P-vaV7.ttf"

COMPONENTS = {
    "top level" : [
        Component("blueSquare.png", "Research module. More points, bigger hitbox", points_multiplier=0.4), 
        Component("greenSquare.png", "Compact. Less points, smaller hitbox", points_multiplier= -0.4), 
        Component("redSquare.png", "Regular. Normal aspects")
        ],
    "middle level" : [
        Component("blueSquare.png", "Research module. Reduced velocity, more points", velocity=-2, points_multiplier=0.4), 
        Component("greenSquare.png", "Compact. Increased velocity, less points", velocity=2, points_multiplier=-0.4), 
        Component("redSquare.png", "Regular. Normal aspects")
        ],
    "engine" : [
        Component("blueSquare.png", "small engine", velocity=3), 
        Component("greenSquare.png", "medium engine", velocity=5), 
        Component("redSquare.png", "large engine", velocity=7)
        ],
    "weapons" : [
        Component("redSquare.png", "Machine guns. Low damage, fast firerate"), 
        Component("blueSquare.png", "Death ray. Big damage, long reload.")
        ]
}

COMPONENTRESIZEVAL = 8