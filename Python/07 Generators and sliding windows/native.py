from collections import deque

def rolling_mean(items, width):
    if width < 1:
        raise ValueError("width must be positive")
    window = deque()
    total = 0
    for value in items:
        window.append(value)
        total += value
        if len(window) > width:
            total -= window.popleft()
        if len(window) == width:
            yield total / width

print(*rolling_mean(iter([2, 4, 8, 1, 3, 7]), 3))
