import operator

operators = {
    "+": operator.add,
    "-": operator.sub,
    "/": operator.truediv,
    "*": operator.mul,
}

FILE = "day21/input.txt"
# FILE = "day21/test-input.txt"

with open(FILE) as f:
    data = [item.strip() for item in f.readlines()]

monkeys = {}
for monkey in data:
    name, job = monkey.split(":")[0].strip(), monkey.split(":")[1].strip()
    monkeys[name] = job


def yell(name):
    if monkeys[name].isnumeric():
        return int(monkeys[name])
    else:
        job = monkeys[name].split()
        return operators[job[1]](yell(job[0]), yell(job[2]))


# part 1
print(yell("root"))


def yell_2(name):
    if name == "humn":
        return int(monkeys[name])
    if monkeys[name].isnumeric():
        return int(monkeys[name])
    else:
        job = monkeys[name].split()
        return operators[job[1]](yell_2(job[0]), yell_2(job[2]))


# part 2
root_job = monkeys["root"].split()
monkey_a = root_job[0]
monkey_b = root_job[2]
result_a = yell_2(monkey_a)
result_b = yell_2(monkey_b)
print(f"Result A: {result_a} result B: {result_b}")


for i in range(3916491093810, 3916491093820):
    monkeys["humn"] = i
    result_a = yell_2(monkey_a)
    result_b = yell_2(monkey_b)
    print(i, result_a, result_b)
