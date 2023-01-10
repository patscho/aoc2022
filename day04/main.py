# FILE = "day04/test-input.txt"
FILE = "day04/input.txt"

full_overlap = 0
with open(FILE) as f:
    data = f.read().strip()

sections = data.split("\n")

overlaps = 0
complete_overlaps = 0
for s in sections:
    s1, s2 = s.split(",")
    s1_start, s1_end = map(int, s1.split("-"))
    s2_start, s2_end = map(int, s2.split("-"))
    if s1_start >= s2_start and s1_end <= s2_end:
        complete_overlaps += 1
    elif s1_start <= s2_start and s1_end >= s2_end:
        complete_overlaps += 1

    if s1_start <= s2_start <= s1_end or s2_start <= s1_start <= s2_end:
        overlaps += 1

print(f"complete overlaps: {complete_overlaps}")
print(f"overlaps: {overlaps}")
