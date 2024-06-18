from component import Component

WINDOWSIZE = (800, 800)

ASTEROIDSPAWNRATE = 50

ASTEROIDSPAWNCAP = 12

FPSCAP = 60

FONT = "PressStart2P-vaV7.ttf"

COMPONENTS = {
    "top level" : [Component("blueSquare.png", "blue"), Component("greenSquare.png", "green"), Component("redSquare.png", "red")],
    "middle level" : [Component("blueSquare.png", "blue"), Component("greenSquare.png", "green"), Component("redSquare.png", "red")],
    "engine" : [Component("blueSquare.png", "blue"), Component("greenSquare.png", "green"), Component("redSquare.png", "red")]
}

COMPONENTRESIZEVAL = 5