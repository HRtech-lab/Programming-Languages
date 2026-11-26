function* balances(changes) {
  let total = 0;
  for (const change of changes) {
    total += change;
    yield total;
  }
}
console.log(...balances([3, -1, 4, -2, 0, 2]));
