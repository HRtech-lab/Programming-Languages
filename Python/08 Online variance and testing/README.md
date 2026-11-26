# Online variance and testing

Compute the population variance after each reading without losing its small variation around a large baseline.

The raw second moment minus the squared mean is mathematically correct but can cancel numerically. Welford updates a running mean and a sum of squared deviations. A two-pass calculation on each short prefix gives a separate check. The population denominator is the prefix length. A sample variance would use one fewer and be undefined on the first observation.

A dataclass holds mutable running state. Updating two instances independently is a direct test for accidental shared state.

[Worked notebook](lesson.ipynb) · [Python script](lesson.py)

[native.py](native.py)

## Execute the native listing

A dataclass holds mutable running state. Updating two instances independently is a direct test for accidental shared state. Python evaluates the iterator when the caller asks for its next item. Put the break point inside the loop when inspecting a lazy calculation.

## Read the output

The first variance is zero. Subsequent variances describe the spread seen so far, and shifting every input by a constant preserves them in exact arithmetic. The marks show the independent Python reference at each position.

## Recorded output

```text
Runtime: Python
Native stdout: 0.0 0.25 1.555555522441864 2.4999999552965164
Largest absolute difference: 4.47e-08
```

## Interpreting the result

The first variance is zero. Subsequent variances describe the spread seen so far, and shifting every input by a constant preserves them in exact arithmetic.

![Online variance and testing, worked result](figure.svg)

## Exercise

Subtract the billion-unit offset and compare the reported variances. Then implement the raw-moment formula and inspect its rounding error.

## References

[Python language tutorial](https://docs.python.org/3/tutorial/)

[Welford, corrected sums of squares (1962)](https://doi.org/10.1080/00401706.1962.10490022)
