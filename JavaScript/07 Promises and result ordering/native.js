async function calibrate(x) {
  return 3 * x + 2;
}
async function main() {
  const inputs = [-1, 0, 2, 5];
  const predictions = await Promise.all(inputs.map(calibrate));
  console.log(...predictions);
}
main().catch(error => { console.error(error); process.exitCode = 1; });
