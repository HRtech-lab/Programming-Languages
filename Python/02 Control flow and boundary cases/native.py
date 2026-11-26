counts = [0, 0, 0]
for value in [-4, 0, 5, 12, 18, 25, 31]:
    if value <= 0:
        category = 0
    elif value < 20:
        category = 1
    else:
        category = 2
    counts[category] += 1
print(*counts)
