from valve import Valve

FILE = "day16/input.txt"

with open(FILE) as f:
    data = [item.strip() for item in f.readlines()]

valves = []

for line in data:
    d = line.split()
    valve_id = d[1]
    flow_rate = int(d[4].split("=")[1].split(";")[0])
    neighbors = [n.strip(",") for n in d[9:]]
    valves.append(Valve(valve_id, flow_rate, neighbors))

print(valves[0].flow_rate)
print(valves[0].neighbors)
