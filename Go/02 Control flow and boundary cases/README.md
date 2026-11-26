# Control flow and boundary cases

Assign each observation to a band, including the observations exactly on a boundary.

Use three disjoint intervals. Values at or below zero enter the first band. Positive values below 20 enter the second. Everything at or above 20 enters the last band. Summing the band counts gives a conservation check that catches dropped observations, although it cannot by itself detect a misplaced observation.

An expressionless switch tests conditions from top to bottom. The zero value of the count array is a valid starting point.

[Worked notebook](lesson.ipynb) · [Python script](lesson.py)

[native.go](native.go)

## Execute the native listing

An expressionless switch tests conditions from top to bottom. The zero value of the count array is a valid starting point. Trace the result and error at the point where each function returns. Slice length, map lookup status and channel synchronisation are explicit parts of the interface.

## Read the output

Read each bar as a count. A boundary convention is part of the specification and should be stated before choosing the test inputs. The marks show the independent Python reference at each position.

## Recorded output

```text
Runtime: Go
Native stdout: 2 3 2
Largest absolute difference: 0
```

## Interpreting the result

Read each bar as a count. A boundary convention is part of the specification and should be stated before choosing the test inputs.

![Control flow and boundary cases, worked result](figure.svg)

## Exercise

Add values 19 and 20, then predict which two bars change. Test a list that leaves a category empty.

## References

[The Go Programming Language Specification](https://go.dev/ref/spec)
