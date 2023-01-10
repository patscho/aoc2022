class Cube:
    def __init__(self, xyz: tuple) -> None:
        self.x = xyz[0]
        self.y = xyz[1]
        self.z = xyz[2]
        self.xyz = xyz
        self.adjecent = [
            (self.x + 1, self.y, self.z),
            (self.x - 1, self.y, self.z),
            (self.x, self.y + 1, self.z),
            (self.x, self.y - 1, self.z),
            (self.x, self.y, self.z + 1),
            (self.x, self.y, self.z - 1),
        ]
        self.visible = 6
