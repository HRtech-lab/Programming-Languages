const counts = [0, 0, 0];
for (const x of [-4, 0, 5, 12, 18, 25, 31]) {
  const band = x <= 0 ? 0 : x < 20 ? 1 : 2;
  counts[band] += 1;
}
console.log(...counts);
