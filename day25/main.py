snafu_2_digital = {"=": -2, "-": -1, "0": 0, "1": 1, "2": 2}
digital_2_snafu = {-2: "=", -1: "-", 0: "0", 1: "1", 2: "2"}


def convert_snafu_to_digital(snafu_string):
    digital_value = 0
    reverse = snafu_string[::-1]
    for i in range(len(reverse)):
        digital_value += 5**i * snafu_2_digital[reverse[i]]
    return digital_value


def convert_digital_to_snafu(number):
    quotient = number // 5
    remainder = number % 5
    # print(quotient, remainder)
    if remainder > 2:
        remainder -= 5
        quotient += 1
    if quotient <= 2:
        return digital_2_snafu[quotient] + digital_2_snafu[remainder]
    else:
        return convert_digital_to_snafu(quotient) + digital_2_snafu[remainder]


FILE = "day25/input.txt"
# FILE = "day25/test-input.txt"

with open(FILE) as f:
    data = [item.strip() for item in f.readlines()]

total = 0
for item in data:
    total += convert_snafu_to_digital(item)

print(f"Digital sum of SNAFU numbers: {total}")
print(f"SNAFU input for Bob: {convert_digital_to_snafu(total)}")
