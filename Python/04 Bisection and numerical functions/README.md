# Bisection and numerical functions

Approximate square roots by repeatedly halving a bracket.

For positive n, the target root lies in [0, max(1,n)]. The square is monotone there, so the comparison with n selects the half that still contains the root. Each exact-arithmetic iteration halves the interval width. In floating-point arithmetic two endpoints eventually round to the same value. Zero has a simple exact answer.

A function can return a float or raise ValueError. A generator expression calls it for each radicand.

[Worked notebook](lesson.ipynb) · [Python script](lesson.py)

[native.py](native.py)

## Execute the native listing

A function can return a float or raise ValueError. A generator expression calls it for each radicand. Python evaluates the iterator when the caller asks for its next item. Put the break point inside the loop when inspecting a lazy calculation.

## Read the output

Accuracy should be checked against an independent implementation on both sides of one. A fixed number of bisection steps is adequate for this small range. The marks show the independent Python reference at each position.

## Recorded output

```text
Runtime: Python
Native stdout: 0.0 0.7071067811865475 1.414213562373095 3.162277660168379 5.0
Largest absolute difference: 4.44e-16
```

## Interpreting the result

Accuracy should be checked against an independent implementation on both sides of one. A fixed number of bisection steps is adequate for this small range.

![Bisection and numerical functions, worked result](figure.svg)

## Exercise

Test 0.01, 1 and a larger value. Replace the fixed iteration count with an absolute or relative tolerance and justify the stopping condition.

## References

[Python language tutorial](https://docs.python.org/3/tutorial/)
