# FILE = "day06/test-input.txt"
FILE = "day06/input.txt"

with open(FILE) as f:
    datastream = f.readlines()[0]

for i in range(3, len(datastream)):
    last_four = datastream[i - 3 : i + 1]
    if len(set(last_four)) == 4:
        print(f"Start of packet marker detected at position: {i + 1}")
        break

for i in range(13, len(datastream)):
    last_fourteen = datastream[i - 13 : i + 1]
    if len(set(last_fourteen)) == 14:
        print(f"Start of message marker detected at position: {i + 1}")
        break
