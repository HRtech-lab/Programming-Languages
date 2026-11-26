from dataclasses import dataclass

@dataclass
class Moments:
    count: int = 0
    mean: float = 0.0
    m2: float = 0.0

    def update(self, value):
        self.count += 1
        delta = value - self.mean
        self.mean += delta / self.count
        self.m2 += delta * (value - self.mean)
        return self.m2 / self.count

state = Moments()
print(*(state.update(1_000_000_000 + x) for x in [1, 2, 4, 5]))
