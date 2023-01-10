import copy


def mix_list(org_list: list[int]):
    for _ in range(10):
        n = len(org_list)
        # working_list = copy.copy(org_list)
        indices = list(range(n))

        for i in range(n):
            value = org_list[i] % (n - 1)
            current_index = indices.index(i)
            new_index = (current_index + value) % (n - 1)
            if new_index > current_index:
                for j in range(current_index, new_index):
                    k = j + 1
                    indices[j], indices[k] = indices[k], indices[j]
            else:
                for j in range(current_index, new_index, -1):
                    k = j - 1
                    indices[j], indices[k] = indices[k], indices[j]

        working_list = [org_list[i] for i in indices]
    return working_list


# FILE = "day20/test-input.txt"
FILE = "day20/input.txt"
with open(FILE) as f:
    original_list = [int(item.strip()) for item in f.readlines()]

second_list = [811589153 * i for i in original_list]

new_list = mix_list(second_list)
# print(new_list)


number1 = new_list[(new_list.index(0) + 1000) % len(new_list)]
number2 = new_list[(new_list.index(0) + 2000) % len(new_list)]
number3 = new_list[(new_list.index(0) + 3000) % len(new_list)]

print(number1 + number2 + number3)
