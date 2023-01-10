import pytest
from monkey import Monkey


def test_init():
    monkey = Monkey(
        [
            "Monkey 0:",
            "Starting items: 79, 98",
            "Operation: new = old * 19",
            "Test: divisible by 23",
            "If true: throw to monkey 2",
            "If false: throw to monkey 3",
        ]
    )
    assert (
        monkey.id == 0
        and monkey.items == [79, 98]
        and monkey.operator == "*"
        and monkey.op_value == "19"
        and monkey.test_value == 23
        and monkey.to_monkey_if_true == 2
        and monkey.to_monkey_if_false == 3
    )


def test_inspect_item():
    lcm = 96577
    monkey = Monkey(
        [
            "Monkey 0:",
            "Starting items: 79, 98",
            "Operation: new = old * 19",
            "Test: divisible by 23",
            "If true: throw to monkey 2",
            "If false: throw to monkey 3",
        ]
    )
    monkey.inspect_item(79, lcm)
    assert monkey.worry_level == 500


# Monkey 0:
# "Starting items: 79, 98",
# "Operation: new = old * 19",
# "Test: divisible by 23",
# "If true: throw to monkey 2",
# "If false: throw to monkey 3"

# Monkey 1:
#   Starting items: 54, 65, 75, 74
#   Operation: new = old + 6
#   Test: divisible by 19
#     If true: throw to monkey 2
#     If false: throw to monkey 0

# Monkey 2:
#   Starting items: 79, 60, 97
#   Operation: new = old * old
#   Test: divisible by 13
#     If true: throw to monkey 1
#     If false: throw to monkey 3

# Monkey 3:
#   Starting items: 74
#   Operation: new = old + 3
#   Test: divisible by 17
#     If true: throw to monkey 0
#     If false: throw to monkey 1
