from absl import app
from absl import flags
from typing import Any

import copy


def parse(path: str) -> list[int]:
    with open(path) as f:
        return [int(l) for l in f.read().splitlines()]


def mixin(xs: list[int], repeat=1) -> list[int]:
    n = len(xs)
    xs = copy.copy(xs)
    idxs = list(range(n))

    for _ in range(repeat):
        for i in range(n):
            print(f"first i is: {i}")
            i = idxs.index(i)
            print(f"second i is: {i}")
            m = xs[i] % (n - 1)
            print(f"{m}, {xs[i]}")
            for (j, k) in zip(range(i, i + m), range(i + 1, i + m + 1)):
                print((j, k))
                j, k = j % n, k % n
                xs[j], xs[k] = xs[k], xs[j]
                idxs[j], idxs[k] = idxs[k], idxs[j]

    return xs


def grove_coordinates(xs: list[int]) -> tuple[int, ...]:
    n = len(xs)
    i = xs.index(0)
    return tuple(xs[(i + 1000 * offset) % n] for offset in [1, 2, 3])


def main(argv):
    xs = parse("day20/test-input.txt")

    # Part 1.
    print(sum(grove_coordinates(mixin(xs))))

    # # Part 2.
    # xs = [811589153 * x for x in xs]
    # print(sum(grove_coordinates(mixin(xs, repeat=10))))


if __name__ == "__main__":
    app.run(main)
