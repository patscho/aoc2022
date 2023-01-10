# FILE = "day08/test-input.txt"
FILE = "day08/input.txt"


def visible_from_left(row_index, column_index):
    # row is fixed, column changes
    for i in range(column_index):
        if rows[row_index][i] >= rows[row_index][column_index]:
            return False
    return True


def visible_from_right(row_index, column_index):
    # row is fixed, column changes
    for i in range(column_index + 1, number_of_columns):
        if rows[row_index][i] >= rows[row_index][column_index]:
            return False
    return True


def visible_from_top(row_index, column_index):
    # rows change, column stays the same
    for i in range(row_index):
        if rows[i][column_index] >= rows[row_index][column_index]:
            return False
    return True


def visible_from_bottom(row_index, column_index):
    # rows change column is fixed
    for i in range(row_index + 1, number_of_rows):
        if rows[i][column_index] >= rows[row_index][column_index]:
            return False
    return True


with open(FILE) as f:
    lines = f.readlines()
    lines = [item.strip() for item in lines]

rows = []
for line in lines:
    line_list = list(line)
    ints_list = [int(item) for item in line_list]
    rows.append(ints_list)
# print(rows)

number_of_rows = len(rows)
number_of_columns = len(rows[0])
number_of_trees = number_of_rows * number_of_columns

# first row is visible by default
# for r in range(1, number_of_rows - 1):
# hidden = 0
# for r in range(1, number_of_rows - 1):
#     for c in range(1, number_of_columns - 1):
#         if (
#             not visible_from_left(r, c)
#             and not visible_from_right(r, c)
#             and not visible_from_top(r, c)
#             and not visible_from_bottom(r, c)
#         ):
#             hidden += 1

# # print(columns)
# print(f"Number of hidden trees: {hidden}")
# print(f"Number of visible trees: {number_of_trees - hidden}")

# part 2
def look_right(row_index, col_index):
    if col_index == number_of_columns - 1:
        return 0
    else:
        right = 1
        for i in range(col_index + 1, number_of_columns - 1):
            if rows[row_index][i] < rows[row_index][col_index]:
                right += 1
            else:
                break
        return right


def look_left(row_index, col_index):
    if col_index == 0:
        return 0
    else:
        left = 1
        for i in range(col_index - 1, 0, -1):
            if rows[row_index][i] < rows[row_index][col_index]:
                left += 1
            else:
                break
    return left


def look_down(row_index, col_index):
    if row_index == number_of_rows - 1:
        return 0
    else:
        down = 1
        for i in range(row_index + 1, number_of_rows - 1):
            if rows[i][col_index] < rows[row_index][col_index]:
                down += 1
            else:
                break
        return down


def look_up(row_index, col_index):
    if row_index == 0:
        return 0
    else:
        up = 1
        for i in range(row_index - 1, 0, -1):
            if rows[i][col_index] < rows[row_index][col_index]:
                up += 1
            else:
                break
        return up


def scenic_score(row_index, col_index):
    left = look_left(row_index, col_index)
    right = look_right(row_index, col_index)
    top = look_up(row_index, col_index)
    bottom = look_down(row_index, col_index)
    return left * right * top * bottom


high_score = 0
high_row = 0
high_col = 0
for r in range(number_of_rows):
    for c in range(number_of_columns):
        score = scenic_score(r, c)
        if score > high_score:
            high_score = score
            high_row = r
            high_col = c
print(f"Highest scenic score: {high_score}")
print(f"tree with high score is: {high_row}, {high_col}")
# print(look_left(2, 0))
# print(look_right(2, 0))
# print(look_down(2, 0))
# print(look_up(2, 0))
# print(look_left(0, 0))
# print(look_left(0, 1))
# print(look_left(0, 2))
# print(look_left(0, 3))
# print(look_right(0, 0))
