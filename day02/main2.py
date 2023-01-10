""" column 1: A - Rock, B - Paper, C - Scissors
    column 2: X - Rock, Y - Paper, Z - Scissors"""
LOSE = 0
DRAW = 3
WIN = 6
ROCK = 1
PAPER = 2
SCISSORS = 3

score = 0
with open("day02/input.txt") as f:
    games = f.readlines()
games = [game.strip() for game in games]
for game in games:
    elf_move = game[0]
    my_move = game[-1]
    if elf_move == "A":
        if my_move == "X":
            score += LOSE + SCISSORS
        elif my_move == "Y":
            score += DRAW + ROCK
        else:
            score += WIN + PAPER
    elif elf_move == "B":
        if my_move == "X":
            score += LOSE + ROCK
        elif my_move == "Y":
            score += DRAW + PAPER
        else:
            score += WIN + SCISSORS
    else:
        if my_move == "X":
            score += LOSE + PAPER
        elif my_move == "Y":
            score += DRAW + SCISSORS
        else:
            score += WIN + ROCK

print(score)
