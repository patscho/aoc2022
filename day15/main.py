import itertools

# FILE = "day15/test-input.txt"
FILE = "day15/input.txt"

with open(FILE) as f:
    data = [item.strip() for item in f.readlines()]


class Sensor:
    def __init__(self, sensor, beacon) -> None:
        self.pos = sensor
        self.beacon = beacon
        self.distance = self.calc_distance()

    def calc_distance(self):
        x1, y1 = self.pos
        x2, y2 = self.beacon
        distance = abs(x1 - x2) + abs(y1 - y2)
        return distance

    def y_coverage(self, y):
        """Return the points that are covered by the sensor with an self.y of y"""
        y_diff = abs(self.pos[1] - y)
        remaining_dist = self.distance - y_diff
        x_start = self.pos[0] - remaining_dist
        x_end = self.pos[0] + remaining_dist
        points = []
        for x in range(x_start, x_end + 1):
            points.append((x, y))
        return points

    def coverage(self):
        coverage = []
        for x_diff in range(self.distance + 1):
            remaining_dist = self.distance - x_diff
            for y_diff in range(remaining_dist + 1):
                coverage.append((self.pos[0] + x_diff, self.pos[1] + y_diff))
                coverage.append((self.pos[0] + x_diff, self.pos[1] - y_diff))
                coverage.append((self.pos[0] - x_diff, self.pos[1] + y_diff))
                coverage.append((self.pos[0] - x_diff, self.pos[1] - y_diff))
        return coverage

    def borders(self):
        borders = set()
        for x_diff in range(self.distance + 1):
            remaining_dist = self.distance - x_diff
            borders.add((self.pos[0] + x_diff, self.pos[1] + remaining_dist))
            borders.add((self.pos[0] + x_diff, self.pos[1] - remaining_dist))
            borders.add((self.pos[0] - x_diff, self.pos[1] + remaining_dist))
            borders.add((self.pos[0] - x_diff, self.pos[1] - remaining_dist))
        return borders

    def borders_plus_one(self):
        borders = set()
        distance = self.distance + 1
        for x_diff in range(distance + 1):
            remaining_dist = distance - x_diff
            borders.add((self.pos[0] + x_diff, self.pos[1] + remaining_dist))
            borders.add((self.pos[0] + x_diff, self.pos[1] - remaining_dist))
            borders.add((self.pos[0] - x_diff, self.pos[1] + remaining_dist))
            borders.add((self.pos[0] - x_diff, self.pos[1] - remaining_dist))
        return borders


def parse_raw_data(data):
    sensor_x = int(data.split()[2].split("=")[1].split(",")[0])
    sensor_y = int(data.split()[3].split("=")[1].split(":")[0])
    sensor = (sensor_x, sensor_y)
    beacon_x = int(data.split()[8].split("=")[1].split(",")[0])
    beacon_y = int(data.split()[9].split("=")[1])
    beacon = (beacon_x, beacon_y)
    return sensor, beacon


def part1():
    coverage = set()
    for s in sensors:
        coverage.update(sensor.y_coverage(2000000))

    for s in sensors:
        b = s.beacon
        if b in coverage:
            coverage.remove(b)
    print(len(coverage))


def part2():
    i = 0
    borders = []
    for s in sensors:
        i += 1
        print(f"Calculating borders of sensor {i}")
        borders.append(s.borders_plus_one())
    for comb in itertools.combinations(borders, 4):
        result = comb[0].intersection(comb[1], comb[2], comb[3])
        if len(result) > 0:
            print(result)
            # frequency = (result[0][0] * 4000000) + result[0][1]
            # print(f"Frequency is: {frequency}")


sensors = []
for d in data:
    s, b = parse_raw_data(d)
    sensor = Sensor(s, b)
    sensors.append(sensor)
print("Sensors data stored....")

part2()

# Output:
# {(2594124, 3746831)}
# {(2816975, 2000000)}
# {(1932523, 967542)}
# {(2042155, 1077174)}
# {(1932524, 967543)}
# {(2572895, 2906626)}
# {(2534304, 3806651)}
