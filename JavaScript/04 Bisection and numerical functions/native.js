function root(n) {
  if (!Number.isFinite(n) || n < 0) throw new RangeError("nonnegative finite input required");
  if (n === 0) return 0;
  let lo = 0, hi = Math.max(1, n);
  for (let i = 0; i < 55; i += 1) {
    const mid = (lo + hi) / 2;
    if (mid * mid < n) lo = mid;
    else hi = mid;
  }
  return (lo + hi) / 2;
}
console.log(...[0, 0.5, 2, 10, 25].map(root));
