class Moments {
  count = 0;
  centre = 0;
  m2 = 0;
  add(x) {
    this.count += 1;
    const delta = x - this.centre;
    this.centre += delta / this.count;
    this.m2 += delta * (x - this.centre);
    return this.m2 / this.count;
  }
}
const state = new Moments();
console.log(...[1, 2, 4, 5].map(x => state.add(1e9 + x)));
