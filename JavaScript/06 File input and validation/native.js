const {readFileSync} = require("node:fs");
const lines = readFileSync("readings.csv", "utf8").trimEnd().split(/\r?\n/).slice(1);
const valid = lines.filter(s => /^[+-]?\d+$/.test(s.trim())).map(Number);
if (!valid.length) throw new Error("no numeric rows");
console.log(valid.length, valid.reduce((a, b) => a + b, 0),
            Math.min(...valid), Math.max(...valid), lines.length - valid.length);
