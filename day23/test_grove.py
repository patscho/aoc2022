import pytest
from grove import Grove

grove_data = [
    "....#..",
    "..###.#",
    "#...#.#",
    ".#...##",
    "#.###..",
    "##.#.##",
    ".#..#..",
]


def test_grove_1():
    grove = Grove(grove_data)
    assert (0, 4) in grove.elves


def test_grove_2():
    grove = Grove(grove_data)
    assert grove.is_south_empty((0, 4)) == False


def test_grove_3():
    grove = Grove(grove_data)
    assert grove.is_east_empty((0, 4)) == False
