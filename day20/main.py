import copy

# FILE = "day20/test-input.txt"
FILE = "day20/input.txt"


def dict_to_list():
    new_list = []
    new_dict = {}
    # print(f"my_dict before creating list: {my_dict}")
    for i in range(len(my_dict)):
        index = my_dict[i]["index"]
        value = my_dict[i]["value"]
        new_dict[index] = value
        # print(f"i: {i}, index: {index}, value: {value}")
    # print(f"new temp dict: {new_dict}")
    for i in range(len(new_dict)):
        new_list.append(new_dict[i])
    return new_list


with open(FILE) as f:
    original_list = [int(item.strip()) for item in f.readlines()]

my_dict = {}
# construct dictionary
for i in range(len(original_list)):
    my_dict[i] = {"value": original_list[i], "index": i}

for i in range(len(original_list)):
    value = original_list[i]
    # print(f"moving item with original index: {i} with value {value}")
    if value % len(original_list) == 0:
        continue
    elif value > 0:
        forward = value % len(original_list)
    else:
        forward = (value % len(original_list)) - 1

    current_index = my_dict[i]["index"]
    new_index = current_index + forward
    if new_index > len(original_list) - 1:
        new_index = (current_index + forward + 1) % len(original_list)
        for x in range(len(original_list)):
            if my_dict[x]["index"] in range(new_index, current_index):
                my_dict[x]["index"] += 1
    else:
        for x in range(len(original_list)):
            if my_dict[x]["index"] in range(
                current_index + 1, current_index + forward + 1
            ):
                my_dict[x]["index"] -= 1
    my_dict[i]["index"] = new_index

new_list = dict_to_list()

number1 = new_list[(new_list.index(0) + 1000) % len(new_list)]
number2 = new_list[(new_list.index(0) + 2000) % len(new_list)]
number3 = new_list[(new_list.index(0) + 3000) % len(new_list)]

print(number1 + number2 + number3)
