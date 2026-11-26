# Collections and prefix sums

Keep the balance after every signed change, including a negative change and a zero.

After processing position i, the state equals the sum of the first i changes. That invariant gives a proof by induction and a simple reference implementation. A one-pass algorithm costs linear time. Computing each prefix separately costs quadratic time but is convenient for checking six short observations.

A slice borrows the vector. scan retains state inside a closure and collect materialises the returned values.

[Worked notebook](lesson.ipynb) · [Python script](lesson.py)

[native.rs](native.rs)

## Execute the native listing

A slice borrows the vector. scan retains state inside a closure and collect materialises the returned values. Read the type and ownership information at the function boundary. A borrowed slice permits access to existing storage while the owner retains responsibility for its lifetime.

## Read the output

A flat section corresponds to a zero change. The final balance must equal the sum of the full input even when earlier balances fall. The marks show the independent Python reference at each position.

## Recorded output

```text
Runtime: Rust
Native stdout: 3 2 6 4 4 6
Largest absolute difference: 0
```

## Interpreting the result

A flat section corresponds to a zero change. The final balance must equal the sum of the full input even when earlier balances fall.

![Collections and prefix sums, worked result](figure.svg)

## Exercise

Insert a negative change at the start. Verify both the prefix values and the final-sum property.

## References

[The Rust Programming Language](https://doc.rust-lang.org/book/)
