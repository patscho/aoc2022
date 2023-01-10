import math


class Monkey:
    def __init__(self, arg_list: list):
        self.arg_list = arg_list
        self.id = self.init_id()
        self.items = self.init_items()
        self.operator, self.op_value = self.init_operation()
        self.test_value = self.init_test_value()
        self.to_monkey_if_true = self.init_to_monkey_if_true()
        self.to_monkey_if_false = self.init_to_monkey_if_false()
        self.items_inspected = 0
        self.worry_level_reduction = True

    def init_id(self):
        return int(self.arg_list[0].split()[1].split(":")[0])

    def init_items(self):
        items = self.arg_list[1].split(":")[1].split(",")
        items = [int(item) for item in items]
        return items

    def init_operation(self):
        op = self.arg_list[2].split()
        return op[4], (op[5])

    def init_test_value(self):
        return int(self.arg_list[3].split()[3])

    def init_to_monkey_if_true(self):
        return int(self.arg_list[4].split()[-1])

    def init_to_monkey_if_false(self):
        return int(self.arg_list[5].split()[-1])

    def inspect_item(self, item: int, lcm: int):
        if self.op_value == "old":
            item_value = item
        else:
            item_value = int(self.op_value)

        if self.operator == "+":
            worry_level = item + item_value
        else:
            worry_level = item * item_value

        if self.worry_level_reduction:
            self.worry_level = math.floor(worry_level / 3)
        else:
            self.worry_level = worry_level % lcm
        self.items_inspected += 1
