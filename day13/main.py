import ast
import itertools

FILE = "day13/input-test.txt"
# FILE = "day13/input.txt"

with open(FILE) as f:
    raw_input = f.readlines()
    data = [item.strip() for item in raw_input]
    data = [ast.literal_eval(item) for item in data if item != ""]

is_in_order_counter = 0


def is_in_order(left: list, right: list):
    global is_in_order_counter
    is_in_order_counter += 1
    # print(f"is_in_order iteration: {is_in_order_counter}")
    # print(left, right)
    if len(left) == 0 and len(right) > 0:
        return True
    elif len(left) > 0 and len(right) == 0:
        return False
    biggest = max([len(left), len(right)])
    # print(smallest)
    # print(left, right)
    for i in range(biggest):
        # print(f"length left: {len(left)}, var i: {i}")
        if len(left) <= i:
            return True
        elif len(right) <= i:
            return False
        # print(i)
        # Allebei int
        if type(left[i]) == int and type(right[i]) == int:
            # print(f"both ints {left[i]} {right[i]}")
            if left[i] < right[i]:
                return True
            elif left[i] > right[i]:
                # print(f"left: {left[i]}, right: {right[i]}")
                return False
            else:
                # print("continuing")
                continue
        # Allebei list
        elif type(left[i]) == list and type(right[i]) == list:
            # print(left[i], right[i])
            if left[i] == [] and right[i] == []:
                continue
            elif left[i] == []:
                return True
            else:
                result = is_in_order(left[i], right[i])
                if result is not None:
                    return result
                else:
                    continue
        # Een int en een list
        elif type(left[i]) == int:
            # print(left[i], right[i])
            return is_in_order([left[i]], right[i])
        else:
            # print(left[i], right[i])
            return is_in_order(left[i], [right[i]])


def order_packets(data):
    data.append([[2]])
    data.append([[6]])


in_order_pairs = []
pair_index = 0
for i in range(0, len(data), 2):
    # print(data[i], data[i + 1])
    pair_index += 1
    if is_in_order(data[i], data[i + 1]):
        in_order_pairs.append(pair_index)

print(sum(in_order_pairs))


order_packets(data)
