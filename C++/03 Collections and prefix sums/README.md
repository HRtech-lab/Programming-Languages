# Collections and prefix sums

Keep the balance after every signed change, including a negative change and a zero.

After processing position i, the state equals the sum of the first i changes. That invariant gives a proof by induction and a simple reference implementation. A one-pass algorithm costs linear time. Computing each prefix separately costs quadratic time but is convenient for checking six short observations.

partial_sum reads a half-open range and writes through back_inserter. The destination vector owns its elements and can grow as needed.

[Worked notebook](lesson.ipynb) · [Python script](lesson.py)

[native.cpp](native.cpp)

## Execute the native listing

partial_sum reads a half-open range and writes through back_inserter. The destination vector owns its elements and can grow as needed. Look at the lifetime of each object and the owner of its storage. Passing a const reference permits observation without copying the container. Algorithms operate on half-open iterator ranges.

## Read the output

A flat section corresponds to a zero change. The final balance must equal the sum of the full input even when earlier balances fall. The marks show the independent Python reference at each position.

## Recorded output

```text
Runtime: C++
Native stdout: 3 2 6 4 4 6
Largest absolute difference: 0
```

## Interpreting the result

A flat section corresponds to a zero change. The final balance must equal the sum of the full input even when earlier balances fall.

![Collections and prefix sums, worked result](figure.svg)

## Exercise

Insert a negative change at the start. Verify both the prefix values and the final-sum property.

## References

[C++ language and standard library reference](https://en.cppreference.com/w/cpp)
