import pytest
from cpu import CPU


def test_noop():
    cpu = CPU()
    cpu.noop()
    assert cpu.end_x == 1 and cpu.cycle == 1


def test_addx_3():
    cpu = CPU()
    cpu.addx(3)
    assert cpu.end_x == 4 and cpu.cycle == 2


def test_exmample_input_1():
    instructions = ["noop", "addx 3", "addx -5"]
    cpu = CPU()
    for i in instructions:
        if i == "noop":
            cpu.noop()
        else:
            number = i.split()[1]
            cpu.addx(int(number))
    assert cpu.end_x == -1 and cpu.cycle == 5
