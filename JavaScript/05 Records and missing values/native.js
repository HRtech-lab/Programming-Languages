const rows = [["A",3], ["B",8], ["A",5], ["C",2], ["B",null]];
const groups = new Map();
for (const [id, value] of rows) {
  if (value === null) continue;
  const entry = groups.get(id) ?? {sum: 0, count: 0};
  entry.sum += value;
  entry.count += 1;
  groups.set(id, entry);
}
console.log(...[...groups.keys()].sort().map(id => {
  const {sum, count} = groups.get(id);
  return sum / count;
}));
