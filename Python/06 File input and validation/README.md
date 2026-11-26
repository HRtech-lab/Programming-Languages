# File input and validation

Read a one-column file and report the valid count, sum, range and number of rejected records.

The supplied CSV has a header and short, unquoted single-field rows. It contains four small integers and two nonnumeric tokens. Keep data-reading errors distinct from bad fields. A rejected row should be counted exactly once and excluded from every numeric statistic. General CSV with embedded commas or quoted newlines needs a CSV parser.

DictReader associates columns with header names. A with block closes the stream even when conversion raises an exception.

[Worked notebook](lesson.ipynb) · [Python script](lesson.py)

[native.py](native.py) · [readings.csv](readings.csv)

## Execute the native listing

DictReader associates columns with header names. A with block closes the stream even when conversion raises an exception. Python evaluates the iterator when the caller asks for its next item. Put the break point inside the loop when inspecting a lazy calculation.

## Read the output

The first statistic counts accepted rows and the last counts rejected rows. Together they must account for all six input observations. The sum and extrema refer to accepted rows only. The marks show the independent Python reference at each position.

## Recorded output

```text
Runtime: Python
Native stdout: 4 21 2 9 2
Largest absolute difference: 0
```

## Interpreting the result

The first statistic counts accepted rows and the last counts rejected rows. Together they must account for all six input observations. The sum and extrema refer to accepted rows only.

![File input and validation, worked result](figure.svg)

## Exercise

Insert another malformed row, rerun and compare the counts. Define an explicit policy for a file with no valid rows.

## References

[Python language tutorial](https://docs.python.org/3/tutorial/)
