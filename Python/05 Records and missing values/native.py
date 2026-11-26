from collections import defaultdict
from statistics import mean

observations = [("A", 3), ("B", 8), ("A", 5), ("C", 2), ("B", None)]
groups = defaultdict(list)
for name, value in observations:
    if value is not None:
        groups[name].append(value)
print(*(mean(groups[name]) for name in sorted(groups)))
