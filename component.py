class Component:
    def __init__(self, skin_path: str, description: str, velocity = 0) -> None:
        self.skin = skin_path
        self.velocity = velocity
        self.description = description