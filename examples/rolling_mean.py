"""Use a Python generator to compute complete sliding-window means in one pass."""
from collections import deque


def rolling_mean(values, width):
    if width < 1:
        raise ValueError("Window width must be positive")
    window = deque()
    total = 0
    for value in values:
        window.append(value)
        total += value
        if len(window) == width:
            yield total / width
            total -= window.popleft()


if __name__ == "__main__":
    values = (x * x for x in range(1, 6))
    means = list(rolling_mean(values, 3))
    assert means == [14 / 3, 29 / 3, 50 / 3]
    print("Three-sample means:", [round(x, 2) for x in means])
