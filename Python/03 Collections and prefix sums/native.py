from itertools import accumulate

changes = [3, -1, 4, -2, 0, 2]
balances = accumulate(changes)
print(*balances)
