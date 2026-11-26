# A practical course in R

This course follows a reading from its initial representation through validation, aggregation and numerical verification. The eight lectures can be read as a sequence. Each opens with an observable question and ends with a change to the fixture that tests your understanding.

## Vectors, attributes and data frames

Most basic R operations act on vectors. A vector has a type and may also have names, dimensions or class attributes. A data frame preserves columns as distinct vectors, so a numeric measurement and a grouping identifier can retain their meanings. Factors add an explicit set of levels. That matters for an empty category, which can disappear from an ordinary frequency table.

## Missing observations and model formulas

NA is part of the data model. A missing value can propagate through arithmetic unless the operation explicitly handles it. Make the exclusion at the point where it changes the denominator. In the modelling workshop, a formula describes both a response and its predictors. The fitted model stores the terms used to construct the design that predict needs for new rows.

## Testing an interface

Use stopifnot for small invariants and all.equal for floating-point comparisons. Inspect attributes as well as numeric data if a caller relies on named columns or factor levels. The labs launch Rscript with --vanilla to isolate each example from saved workspaces and startup profiles.

## Working with a numerical reference

An example is easier to trust when it can fail for a specific reason. Before executing any chapter, write down the output length, the unit and one boundary value. Check the native output against a second calculation. In the variance chapter the comparison uses a separate prefix calculation. In the temperature chapter a familiar fixed point provides a check independent of the programming language.

## 1. Values and numeric types

Convert five readings from Celsius to Fahrenheit and examine where arithmetic changes type. The offset belongs after multiplication by the scale factor. Check the freezing point by hand, then inspect a value that would expose early integer division. All plotted points share the same transformation, so equal increments on the input scale must give equal increments on the output scale.

A vectorised expression applies one transformation to all observations. The scalar constants recycle to the vector length.

By the end of this lecture you should be able to read a value and identify its representation.

[Native source](01%20Values%20and%20numeric%20types/native.R) · [Executed notebook](01%20Values%20and%20numeric%20types/lesson.ipynb) · [Python companion](01%20Values%20and%20numeric%20types/lesson.py)

```text
Runtime: R
Native stdout: 14 32 50 68 86
Largest absolute difference: 0
```

A straight line is expected. The intercept is 32 and a ten-degree Celsius step adds 18 degrees Fahrenheit. Add −40 and a fractional Celsius reading. Describe any type change needed by the native programme.

## 2. Control flow and boundary cases

Assign each observation to a band, including the observations exactly on a boundary. Use three disjoint intervals. Values at or below zero enter the first band. Positive values below 20 enter the second. Everything at or above 20 enters the last band. Summing the band counts gives a conservation check that catches dropped observations, although it cannot by itself detect a misplaced observation.

A factor with explicit levels fixes the order of a table and preserves categories with zero observations.

By the end of this lecture you should be able to trace conditions at their boundaries.

[Native source](02%20Control%20flow%20and%20boundary%20cases/native.R) · [Executed notebook](02%20Control%20flow%20and%20boundary%20cases/lesson.ipynb) · [Python companion](02%20Control%20flow%20and%20boundary%20cases/lesson.py)

```text
Runtime: R
Native stdout: 2 3 2
Largest absolute difference: 0
```

Read each bar as a count. A boundary convention is part of the specification and should be stated before choosing the test inputs. Add values 19 and 20, then predict which two bars change. Test a list that leaves a category empty.

## 3. Collections and prefix sums

Keep the balance after every signed change, including a negative change and a zero. After processing position i, the state equals the sum of the first i changes. That invariant gives a proof by induction and a simple reference implementation. A one-pass algorithm costs linear time. Computing each prefix separately costs quadratic time but is convenient for checking six short observations.

cumsum returns one result per input. tail extracts the final total and stopifnot checks a property of the vector.

By the end of this lecture you should be able to carry state through an ordered collection.

[Native source](03%20Collections%20and%20prefix%20sums/native.R) · [Executed notebook](03%20Collections%20and%20prefix%20sums/lesson.ipynb) · [Python companion](03%20Collections%20and%20prefix%20sums/lesson.py)

```text
Runtime: R
Native stdout: 3 2 6 4 4 6
Largest absolute difference: 0
```

A flat section corresponds to a zero change. The final balance must equal the sum of the full input even when earlier balances fall. Insert a negative change at the start. Verify both the prefix values and the final-sum property.

![Collections and prefix sums](03%20Collections%20and%20prefix%20sums/figure.svg)

## 4. Bisection and numerical functions

Approximate square roots by repeatedly halving a bracket. For positive n, the target root lies in [0, max(1,n)]. The square is monotone there, so the comparison with n selects the half that still contains the root. Each exact-arithmetic iteration halves the interval width. In floating-point arithmetic two endpoints eventually round to the same value. Zero has a simple exact answer.

vapply specifies the result shape and type expected from each call. A scalar function keeps the bracket invariant easy to inspect.

By the end of this lecture you should be able to specify a numeric invariant and error contract.

[Native source](04%20Bisection%20and%20numerical%20functions/native.R) · [Executed notebook](04%20Bisection%20and%20numerical%20functions/lesson.ipynb) · [Python companion](04%20Bisection%20and%20numerical%20functions/lesson.py)

```text
Runtime: R
Native stdout: 0.0000000000 0.7071067812 1.4142135624 3.1622776602 5.0000000000
Largest absolute difference: 3.16e-11
```

Accuracy should be checked against an independent implementation on both sides of one. A fixed number of bisection steps is adequate for this small range. Test 0.01, 1 and a larger value. Replace the fixed iteration count with an absolute or relative tolerance and justify the stopping condition.

## 5. Records and missing values

Compute mean readings by instrument while retaining the difference between zero and an absent reading. Define the unit of observation before grouping. Each row is one reading from one instrument. The correct denominator is the number of observed values for that instrument. A measurement of zero belongs in that denominator. The result is ordered by identifier so it can be compared independently of map iteration order.

split partitions a data frame column by its identifiers. mean with na.rm drops missing measurements from both numerator and denominator.

By the end of this lecture you should be able to group records with explicit missingness.

[Native source](05%20Records%20and%20missing%20values/native.R) · [Executed notebook](05%20Records%20and%20missing%20values/lesson.ipynb) · [Python companion](05%20Records%20and%20missing%20values/lesson.py)

```text
Runtime: R
Native stdout: 4 8 2
Largest absolute difference: 0
```

Instrument B has one observed value and one missing value. Its average stays at eight. An empty instrument would need an explicit missing-output convention. Add a genuine zero to B and a new instrument with no observed values. Decide on a representation for the empty result.

## 6. File input and validation

Read a one-column file and report the valid count, sum, range and number of rejected records. The supplied CSV has a header and short, unquoted single-field rows. It contains four small integers and two nonnumeric tokens. Keep data-reading errors distinct from bad fields. A rejected row should be counted exactly once and excluded from every numeric statistic. General CSV with embedded commas or quoted newlines needs a CSV parser.

Read the single column as character before interpreting it. A full integer match keeps missing tokens and malformed entries visible for the audit count.

By the end of this lecture you should be able to validate rows at the file boundary.

[Native source](06%20File%20input%20and%20validation/native.R) · [Executed notebook](06%20File%20input%20and%20validation/lesson.ipynb) · [Python companion](06%20File%20input%20and%20validation/lesson.py)

```text
Runtime: R
Native stdout: 4 21 2 9 2
Largest absolute difference: 0
```

The first statistic counts accepted rows and the last counts rejected rows. Together they must account for all six input observations. The sum and extrema refer to accepted rows only. Insert another malformed row, rerun and compare the counts. Define an explicit policy for a file with no valid rows.

## 7. Formula models and prediction

Follow a feature that shapes how this language is used in practice. Work with a small fixture so that every returned value can be checked by hand. Keep the ordering of inputs visible. Trace resource ownership, data shape or scheduling as appropriate, and identify the exact point where the result becomes available to the caller.

The formula y ~ x includes an intercept. predict builds a design for new rows using the fitted terms. Coefficients and predictions answer different questions.

By the end of this lecture you should be able to use a language-specific abstraction.

[Native source](07%20Formula%20models%20and%20prediction/native.R) · [Executed notebook](07%20Formula%20models%20and%20prediction/lesson.ipynb) · [Python companion](07%20Formula%20models%20and%20prediction/lesson.py)

```text
Runtime: R
Native stdout: -1 2 8 17
Largest absolute difference: 0
```

The independent calculation describes the expected output. Its agreement with the native result tests both the values and their order. Change the input length, add a repeated value and predict all output positions before running the programme.

![Formula models and prediction](07%20Formula%20models%20and%20prediction/figure.svg)

## 8. Online variance and testing

Compute the population variance after each reading without losing its small variation around a large baseline. The raw second moment minus the squared mean is mathematically correct but can cancel numerically. Welford updates a running mean and a sum of squared deviations. A two-pass calculation on each short prefix gives a separate check. The population denominator is the prefix length. A sample variance would use one fewer and be undefined on the first observation.

R doubles have finite precision. Centring each update avoids subtracting two large, nearly equal estimates.

By the end of this lecture you should be able to check an online calculation with an independent reference.

[Native source](08%20Online%20variance%20and%20testing/native.R) · [Executed notebook](08%20Online%20variance%20and%20testing/lesson.ipynb) · [Python companion](08%20Online%20variance%20and%20testing/lesson.py)

```text
Runtime: R
Native stdout: 0.0000000000 0.2500000000 1.5555555224 2.4999999553
Largest absolute difference: 4.47e-08
```

The first variance is zero. Subsequent variances describe the spread seen so far, and shifting every input by a constant preserves them in exact arithmetic. Subtract the billion-unit offset and compare the reported variances. Then implement the raw-moment formula and inspect its rounding error.

![Online variance and testing](08%20Online%20variance%20and%20testing/figure.svg)

## Capstone

Build a small component that accepts a stream of labelled readings, validates individual fields and emits a population variance for each group. Give it a deliberate policy for a group with no numeric rows. Use at least one test with two observations of identical value, one with a malformed field and one with a large offset. Provide a short argument for the update invariant, report native output for each fixture and compare the results against a two-pass reference.

## References

[Language reference](https://cran.r-project.org/doc/manuals/r-release/R-intro.html) · [Welford, corrected sums of squares](https://doi.org/10.1080/00401706.1962.10490022)
