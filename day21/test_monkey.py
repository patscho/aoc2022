from monkey import Monkey
import pytest


def test_monkey_1():
    monkey = Monkey("abc", "5")
    assert monkey.name == "abc" and monkey.yell() == 5


def test_monkey_2():
    monkey = Monkey("a", "3 + 5")
    assert monkey.yell() == 8


def test_monkey_3():
    monkey = Monkey("a", "5 + b")
    assert monkey.yell() == "Waiting for monkey: b"


def test_monkey_4():
    monkey = Monkey("a", "c + 7")
    assert monkey.yell() == "Waiting for monkey: c"


def test_monkey_5():
    monkey = Monkey("a", "d + e")
    assert monkey.yell() == "Waiting for monkeys: d and e"
