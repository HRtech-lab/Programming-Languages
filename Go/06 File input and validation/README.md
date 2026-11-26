# File input and validation

Read a one-column file and report the valid count, sum, range and number of rejected records.

The supplied CSV has a header and short, unquoted single-field rows. It contains four small integers and two nonnumeric tokens. Keep data-reading errors distinct from bad fields. A rejected row should be counted exactly once and excluded from every numeric statistic. General CSV with embedded commas or quoted newlines needs a CSV parser.

Scanner controls line-by-line input. A scan error, an unparseable field and an empty data file are separate cases.

[Worked notebook](lesson.ipynb) · [Python script](lesson.py)

[native.go](native.go) · [readings.csv](readings.csv)

## Execute the native listing

Scanner controls line-by-line input. A scan error, an unparseable field and an empty data file are separate cases. Trace the result and error at the point where each function returns. Slice length, map lookup status and channel synchronisation are explicit parts of the interface.

## Read the output

The first statistic counts accepted rows and the last counts rejected rows. Together they must account for all six input observations. The sum and extrema refer to accepted rows only. The marks show the independent Python reference at each position.

## Recorded output

```text
Runtime: Go
Native stdout: 4 21 2 9 2
Largest absolute difference: 0
```

## Interpreting the result

The first statistic counts accepted rows and the last counts rejected rows. Together they must account for all six input observations. The sum and extrema refer to accepted rows only.

![File input and validation, worked result](figure.svg)

## Exercise

Insert another malformed row, rerun and compare the counts. Define an explicit policy for a file with no valid rows.

## References

[The Go Programming Language Specification](https://go.dev/ref/spec)
