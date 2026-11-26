# A practical course in C

This course follows a reading from its initial representation through validation, aggregation and numerical verification. The eight lectures can be read as a sequence. Each opens with an observable question and ends with a change to the fixture that tests your understanding.

## Arrays, pointers and lifetimes

An array object has a size, but many expressions convert an array to a pointer to its first element. After that conversion the callee needs an explicit length. The prefix example accepts both pointers and a shared element count. The allocation workshop calculates capacity before calling malloc and releases the allocation exactly once. Derive the number of complete windows before assigning indices.

## Errors and representations

C represents many errors with return values, status flags or errno. A numeric conversion can return zero after reading zero, or after failing to find digits. Check the end pointer to distinguish the two. Choose an accumulator wide enough for the specified input range. The file exercise deliberately uses small fixture values and short, one-field rows.

## Testing an interface

Compile with warnings enabled, include empty-input cases and inspect every bound before dereferencing. Boundary-value tests complement compiler diagnostics. The values printed by the native binary are checked separately from the independent Python calculation.

## Working with a numerical reference

An example is easier to trust when it can fail for a specific reason. Before executing any chapter, write down the output length, the unit and one boundary value. Check the native output against a second calculation. In the variance chapter the comparison uses a separate prefix calculation. In the temperature chapter a familiar fixed point provides a check independent of the programming language.

## 1. Values and numeric types

Convert five readings from Celsius to Fahrenheit and examine where arithmetic changes type. The offset belongs after multiplication by the scale factor. Check the freezing point by hand, then inspect a value that would expose early integer division. All plotted points share the same transformation, so equal increments on the input scale must give equal increments on the output scale.

An array has a known extent where it is declared. sizeof on the actual array gives a byte count. The literal 9.0 promotes the calculation before division.

By the end of this lecture you should be able to read a value and identify its representation.

[Native source](01%20Values%20and%20numeric%20types/native.c) · [Executed notebook](01%20Values%20and%20numeric%20types/lesson.ipynb) · [Python companion](01%20Values%20and%20numeric%20types/lesson.py)

```text
Runtime: C
Native stdout: 14 32 50 68 86
Largest absolute difference: 0
```

A straight line is expected. The intercept is 32 and a ten-degree Celsius step adds 18 degrees Fahrenheit. Add −40 and a fractional Celsius reading. Describe any type change needed by the native programme.

## 2. Control flow and boundary cases

Assign each observation to a band, including the observations exactly on a boundary. Use three disjoint intervals. Values at or below zero enter the first band. Positive values below 20 enter the second. Everything at or above 20 enters the last band. Summing the band counts gives a conservation check that catches dropped observations, although it cannot by itself detect a misplaced observation.

Counts are initialised to zero. The branch produces a valid index for each of the three categories.

By the end of this lecture you should be able to trace conditions at their boundaries.

[Native source](02%20Control%20flow%20and%20boundary%20cases/native.c) · [Executed notebook](02%20Control%20flow%20and%20boundary%20cases/lesson.ipynb) · [Python companion](02%20Control%20flow%20and%20boundary%20cases/lesson.py)

```text
Runtime: C
Native stdout: 2 3 2
Largest absolute difference: 0
```

Read each bar as a count. A boundary convention is part of the specification and should be stated before choosing the test inputs. Add values 19 and 20, then predict which two bars change. Test a list that leaves a category empty.

## 3. Collections and prefix sums

Keep the balance after every signed change, including a negative change and a zero. After processing position i, the state equals the sum of the first i changes. That invariant gives a proof by induction and a simple reference implementation. A one-pass algorithm costs linear time. Computing each prefix separately costs quadratic time but is convenient for checking six short observations.

The caller passes an input pointer, an output pointer and the common length. const protects the input through this pointer.

By the end of this lecture you should be able to carry state through an ordered collection.

[Native source](03%20Collections%20and%20prefix%20sums/native.c) · [Executed notebook](03%20Collections%20and%20prefix%20sums/lesson.ipynb) · [Python companion](03%20Collections%20and%20prefix%20sums/lesson.py)

```text
Runtime: C
Native stdout: 3 2 6 4 4 6
Largest absolute difference: 0
```

A flat section corresponds to a zero change. The final balance must equal the sum of the full input even when earlier balances fall. Insert a negative change at the start. Verify both the prefix values and the final-sum property.

![Collections and prefix sums](03%20Collections%20and%20prefix%20sums/figure.svg)

## 4. Bisection and numerical functions

Approximate square roots by repeatedly halving a bracket. For positive n, the target root lies in [0, max(1,n)]. The square is monotone there, so the comparison with n selects the half that still contains the root. Each exact-arithmetic iteration halves the interval width. In floating-point arithmetic two endpoints eventually round to the same value. Zero has a simple exact answer.

The Boolean result carries success. An output pointer carries the computed value on the success path.

By the end of this lecture you should be able to specify a numeric invariant and error contract.

[Native source](04%20Bisection%20and%20numerical%20functions/native.c) · [Executed notebook](04%20Bisection%20and%20numerical%20functions/lesson.ipynb) · [Python companion](04%20Bisection%20and%20numerical%20functions/lesson.py)

```text
Runtime: C
Native stdout: 0 0.707106781187 1.41421356237 3.16227766017 5
Largest absolute difference: 3.1e-12
```

Accuracy should be checked against an independent implementation on both sides of one. A fixed number of bisection steps is adequate for this small range. Test 0.01, 1 and a larger value. Replace the fixed iteration count with an absolute or relative tolerance and justify the stopping condition.

## 5. Records and missing values

Compute mean readings by instrument while retaining the difference between zero and an absent reading. Define the unit of observation before grouping. Each row is one reading from one instrument. The correct denominator is the number of observed values for that instrument. A measurement of zero belongs in that denominator. The result is ordered by identifier so it can be compared independently of map iteration order.

A struct stores a label, an integer and a presence flag. A valid measured zero can therefore be distinguished from a missing observation.

By the end of this lecture you should be able to group records with explicit missingness.

[Native source](05%20Records%20and%20missing%20values/native.c) · [Executed notebook](05%20Records%20and%20missing%20values/lesson.ipynb) · [Python companion](05%20Records%20and%20missing%20values/lesson.py)

```text
Runtime: C
Native stdout: 4 8 2
Largest absolute difference: 0
```

Instrument B has one observed value and one missing value. Its average stays at eight. An empty instrument would need an explicit missing-output convention. Add a genuine zero to B and a new instrument with no observed values. Decide on a representation for the empty result.

## 6. File input and validation

Read a one-column file and report the valid count, sum, range and number of rejected records. The supplied CSV has a header and short, unquoted single-field rows. It contains four small integers and two nonnumeric tokens. Keep data-reading errors distinct from bad fields. A rejected row should be counted exactly once and excluded from every numeric statistic. General CSV with embedded commas or quoted newlines needs a CSV parser.

strtol exposes the first unconsumed character and reports overflow via errno. The fixture is a small one-column file with short unquoted rows.

By the end of this lecture you should be able to validate rows at the file boundary.

[Native source](06%20File%20input%20and%20validation/native.c) · [Executed notebook](06%20File%20input%20and%20validation/lesson.ipynb) · [Python companion](06%20File%20input%20and%20validation/lesson.py)

```text
Runtime: C
Native stdout: 4 21 2 9 2
Largest absolute difference: 0
```

The first statistic counts accepted rows and the last counts rejected rows. Together they must account for all six input observations. The sum and extrema refer to accepted rows only. Insert another malformed row, rerun and compare the counts. Define an explicit policy for a file with no valid rows.

## 7. Dynamic allocation and ownership

Follow a feature that shapes how this language is used in practice. Work with a small fixture so that every returned value can be checked by hand. Keep the ordering of inputs visible. Trace resource ownership, data shape or scheduling as appropriate, and identify the exact point where the result becomes available to the caller.

The output buffer is allocated once, sized for the number of complete windows and released when printing is finished. A running sum avoids rescanning the window.

By the end of this lecture you should be able to use a language-specific abstraction.

[Native source](07%20Dynamic%20allocation%20and%20ownership/native.c) · [Executed notebook](07%20Dynamic%20allocation%20and%20ownership/lesson.ipynb) · [Python companion](07%20Dynamic%20allocation%20and%20ownership/lesson.py)

```text
Runtime: C
Native stdout: 4.66666666667 4.33333333333 4 3.66666666667
Largest absolute difference: 3.33e-12
```

The independent calculation describes the expected output. Its agreement with the native result tests both the values and their order. Change the input length, add a repeated value and predict all output positions before running the programme.

![Dynamic allocation and ownership](07%20Dynamic%20allocation%20and%20ownership/figure.svg)

## 8. Online variance and testing

Compute the population variance after each reading without losing its small variation around a large baseline. The raw second moment minus the squared mean is mathematically correct but can cancel numerically. Welford updates a running mean and a sum of squared deviations. A two-pass calculation on each short prefix gives a separate check. The population denominator is the prefix length. A sample variance would use one fewer and be undefined on the first observation.

A struct keeps count, mean and sum of squared deviations together. The denominator converts the accumulator into a population variance.

By the end of this lecture you should be able to check an online calculation with an independent reference.

[Native source](08%20Online%20variance%20and%20testing/native.c) · [Executed notebook](08%20Online%20variance%20and%20testing/lesson.ipynb) · [Python companion](08%20Online%20variance%20and%20testing/lesson.py)

```text
Runtime: C
Native stdout: 0 0.25 1.55555552244 2.4999999553
Largest absolute difference: 4.47e-08
```

The first variance is zero. Subsequent variances describe the spread seen so far, and shifting every input by a constant preserves them in exact arithmetic. Subtract the billion-unit offset and compare the reported variances. Then implement the raw-moment formula and inspect its rounding error.

![Online variance and testing](08%20Online%20variance%20and%20testing/figure.svg)

## Capstone

Build a small component that accepts a stream of labelled readings, validates individual fields and emits a population variance for each group. Give it a deliberate policy for a group with no numeric rows. Use at least one test with two observations of identical value, one with a malformed field and one with a large offset. Provide a short argument for the update invariant, report native output for each fixture and compare the results against a two-pass reference.

## References

[Language reference](https://en.cppreference.com/w/c/language) · [Welford, corrected sums of squares](https://doi.org/10.1080/00401706.1962.10490022)
