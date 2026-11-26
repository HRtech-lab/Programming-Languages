def root(n, iterations=55):
    if n < 0:
        raise ValueError("expected a nonnegative input")
    if n == 0:
        return 0.0
    low, high = 0.0, max(1.0, n)
    for _ in range(iterations):
        middle = (low + high) / 2
        if middle * middle < n:
            low = middle
        else:
            high = middle
    return (low + high) / 2

print(*(root(x) for x in (0, 0.5, 2, 10, 25)))
