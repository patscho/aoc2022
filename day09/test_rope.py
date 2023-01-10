import pytest
from rope import Rope


def test_up():
    rope = Rope(2)
    rope.move("u")
    assert rope.knots[0].pos == (0, 1)


def test_down():
    rope = Rope(2)
    rope.move("d")
    assert rope.knots[0].pos == (0, -1)


def test_left():
    rope = Rope(2)
    rope.move("l")
    assert rope.knots[0].pos == (-1, 0)


def test_right():
    rope = Rope(2)
    rope.move("r")
    assert rope.knots[0].pos == (1, 0)


def test_two_up_two_right():
    rope = Rope(2)
    rope.move("u")
    rope.move("u")
    rope.move("r")
    rope.move("r")
    assert rope.knots[0].pos == (2, 2) and rope.knots[-1].pos == (1, 2)


def test_rope_3_two_up_two_right():
    rope = Rope(3)
    rope.move("u")
    rope.move("u")
    rope.move("r")
    rope.move("r")
    assert rope.knots[0].pos == (2, 2) and rope.knots[-1].pos == (1, 1)


def test_rope_4_5_times_up_right():
    rope = Rope(4)
    for _ in range(5):
        rope.move("u")
        rope.move("r")
    assert rope.get_head_pos() == (5, 5) and rope.get_tail_pos() == (2, 2)


def test_part_1():
    moves = ["R 4", "U 4", "L 3", "D 1", "R 4", "D 1", "L 5", "R 2"]
    rope = Rope(2)
    for move in moves:
        direction, amount = move.split()
        for _ in range(int(amount)):
            rope.move(direction)
    assert len(set(rope.visited_by_tail)) == 13


def test_part_2():
    moves = ["R 5", "U 8", "L 8", "D 3", "R 17", "D 10", "L 25", "U 20"]
    rope = Rope(10)
    for move in moves:
        direction, amount = move.split()
        for _ in range(int(amount)):
            rope.move(direction)
    assert len(set(rope.visited_by_tail)) == 36
