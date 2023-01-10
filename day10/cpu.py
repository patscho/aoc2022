import math

interesting_cycles = [20, 60, 100, 140, 180, 220]


class CPU:
    def __init__(self) -> None:
        self.start_x = 1
        self.end_x = 1
        self.cycle = 0
        self.signal_strengths = []
        self.crt_rows = {}

    def noop(self):
        self.start_x = self.end_x
        self.add_cycle()

    def addx(self, value):
        self.start_x = self.end_x
        self.add_cycle()
        self.add_cycle()
        self.end_x += value

    def add_cycle(self):
        self.cycle += 1
        if self.cycle in interesting_cycles:
            signal_strength = self.start_x * self.cycle
            self.signal_strengths.append(signal_strength)
        self.draw_pixel()

    def draw_pixel(self):
        pixel_number = (self.cycle - 1) % 40
        row_number = math.floor((self.cycle - 1) / 40)
        if self.start_x == 0:
            sprite = [0, 1, 2]
        elif self.start_x == 39:
            sprite = [37, 38, 39]
        else:
            sprite = [self.start_x - 1, self.start_x, self.start_x + 1]

        if (self.cycle - 1) % 40 == 0:
            self.crt_rows[row_number] = []

        print(
            f"cycle: {self.cycle}, row: {row_number}, sprite: {sprite}, x: {self.start_x}"
        )
        if pixel_number in sprite:
            self.crt_rows[row_number].append("#")
        else:
            self.crt_rows[row_number].append(".")
