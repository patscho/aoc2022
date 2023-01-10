from rucksack import RuckSack
import string

# INPUTFILE = "day03/test-input.txt"
INPUTFILE = "day03/input.txt"

priorities = dict()
letters = string.ascii_lowercase + string.ascii_uppercase
for index, letter in enumerate(letters):
    priorities[letter] = index + 1

with open(INPUTFILE) as f:
    file_input = f.readlines()

rucksacks = [RuckSack(item.strip()) for item in file_input]

# Part 1
misplaced_items = []
for rucksack in rucksacks:
    misplaced_items.append(rucksack.in_both_compartiments()[0])
item_priorities = [priorities[item] for item in misplaced_items]
print(sum(item_priorities))

# Part 2
print(len(rucksacks))
badges = []
for x in range(0, len(rucksacks), 3):
    badge = (
        set(rucksacks[x].contents)
        & set(rucksacks[x + 1].contents)
        & set(rucksacks[x + 2].contents)
    )
    badges.append(badge.pop())
badge_priorities = [priorities[badge] for badge in badges]
print(sum(badge_priorities))
