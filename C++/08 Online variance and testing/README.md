# Online variance and testing

Compute the population variance after each reading without losing its small variation around a large baseline.

The raw second moment minus the squared mean is mathematically correct but can cancel numerically. Welford updates a running mean and a sum of squared deviations. A two-pass calculation on each short prefix gives a separate check. The population denominator is the prefix length. A sample variance would use one fewer and be undefined on the first observation.

Zero member initialisers establish a valid empty accumulator. Updating the object changes only its own state.

[Worked notebook](lesson.ipynb) · [Python script](lesson.py)

[native.cpp](native.cpp)

## Execute the native listing

Zero member initialisers establish a valid empty accumulator. Updating the object changes only its own state. Look at the lifetime of each object and the owner of its storage. Passing a const reference permits observation without copying the container. Algorithms operate on half-open iterator ranges.

## Read the output

The first variance is zero. Subsequent variances describe the spread seen so far, and shifting every input by a constant preserves them in exact arithmetic. The marks show the independent Python reference at each position.

## Recorded output

```text
Runtime: C++
Native stdout: 0 0.25 1.55555552244 2.4999999553
Largest absolute difference: 4.47e-08
```

## Interpreting the result

The first variance is zero. Subsequent variances describe the spread seen so far, and shifting every input by a constant preserves them in exact arithmetic.

![Online variance and testing, worked result](figure.svg)

## Exercise

Subtract the billion-unit offset and compare the reported variances. Then implement the raw-moment formula and inspect its rounding error.

## References

[C++ language and standard library reference](https://en.cppreference.com/w/cpp)

[Welford, corrected sums of squares (1962)](https://doi.org/10.1080/00401706.1962.10490022)
