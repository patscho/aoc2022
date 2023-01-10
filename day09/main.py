from rope import Rope

FILE = "day09/test-input-2.txt"
# FILE = "day09/input.txt"

with open(FILE) as f:
    moves = f.readlines()
    moves = [move.strip() for move in moves]
print(moves)

# Part 1
def part1():
    rope = Rope(2)
    for move in moves:
        direction, amount = move.split()
        for _ in range(int(amount)):
            rope.move(direction)
    print(len(set(rope.visited_by_tail)))


# Part 2
def part2():
    rope = Rope(10)
    for move in moves:
        direction, amount = move.split()
        for _ in range(int(amount)):
            rope.move(direction)
    print(len(set(rope.visited_by_tail)))


part1()
part2()
