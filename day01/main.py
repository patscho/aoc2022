calorie_list = []
with open("day01/input.txt") as f:
    tmp = 0
    for line in f:
        if line.strip() != "":
            tmp += int(line.strip())
        else:
            calorie_list.append(tmp)
            tmp = 0
print(max(calorie_list))
print(sum(sorted(calorie_list)[-3:]))
