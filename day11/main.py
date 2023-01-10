from monkey import Monkey
import math

FILE = "day11/input-test.txt"
# FILE = "day11/input.txt"


def lcm(lst):
    lcm_temp = max(lst)
    while True:
        if all(lcm_temp % x == 0 for x in lst):
            break
        lcm_temp = lcm_temp + 1
    return lcm_temp


monkeys = {}

with open(FILE) as f:
    data = f.readlines()
    data = [item.strip() for item in data]
    for i in range(0, len(data), 7):
        slice = data[i : i + 6]
        monkey = Monkey(slice)
        monkeys[monkey.id] = monkey

dividers_list = []
for i in range(len(monkeys)):
    dividers_list.append(monkeys[i].test_value)

lcm = lcm(dividers_list)
print(lcm)
# print(monkeys)
for _ in range(10000):
    for i in range(len(monkeys)):
        while len(monkeys[i].items) > 0:
            item = monkeys[i].items[0]
            monkeys[i].inspect_item(item, lcm)
            worry_level = monkeys[i].worry_level
            if worry_level % monkeys[i].test_value == 0:
                to_monkey = monkeys[i].to_monkey_if_true
            else:
                to_monkey = monkeys[i].to_monkey_if_false
            monkeys[i].items.remove(item)
            monkeys[to_monkey].items.append(worry_level)


# print("==================")
# print(monkeys[0].items)
# print(monkeys[1].items)
# print(monkeys[2].items)
# print(monkeys[3].items)
# print("==================")

business = []
for i in range(len(monkeys)):
    business.append(monkeys[i].items_inspected)
print(business)
business.sort(reverse=True)
print(business[0] * business[1])
