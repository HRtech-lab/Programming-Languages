# Online variance and testing

Compute the population variance after each reading without losing its small variation around a large baseline.

The raw second moment minus the squared mean is mathematically correct but can cancel numerically. Welford updates a running mean and a sum of squared deviations. A two-pass calculation on each short prefix gives a separate check. The population denominator is the prefix length. A sample variance would use one fewer and be undefined on the first observation.

A struct keeps count, mean and sum of squared deviations together. The denominator converts the accumulator into a population variance.

[Worked notebook](lesson.ipynb) · [Python script](lesson.py)

[native.c](native.c)

## Execute the native listing

A struct keeps count, mean and sum of squared deviations together. The denominator converts the accumulator into a population variance. Track object lifetime, element count and representation separately. Bounds do not automatically travel with a pointer. Compiler warnings help expose conversions that deserve inspection.

## Read the output

The first variance is zero. Subsequent variances describe the spread seen so far, and shifting every input by a constant preserves them in exact arithmetic. The marks show the independent Python reference at each position.

## Recorded output

```text
Runtime: C
Native stdout: 0 0.25 1.55555552244 2.4999999553
Largest absolute difference: 4.47e-08
```

## Interpreting the result

The first variance is zero. Subsequent variances describe the spread seen so far, and shifting every input by a constant preserves them in exact arithmetic.

![Online variance and testing, worked result](figure.svg)

## Exercise

Subtract the billion-unit offset and compare the reported variances. Then implement the raw-moment formula and inspect its rounding error.

## References

[C language reference and standard revisions](https://en.cppreference.com/w/c/language)

[Welford, corrected sums of squares (1962)](https://doi.org/10.1080/00401706.1962.10490022)
