# Values and numeric types

Convert five readings from Celsius to Fahrenheit and examine where arithmetic changes type.

The offset belongs after multiplication by the scale factor. Check the freezing point by hand, then inspect a value that would expose early integer division. All plotted points share the same transformation, so equal increments on the input scale must give equal increments on the output scale.

An array has a known extent where it is declared. sizeof on the actual array gives a byte count. The literal 9.0 promotes the calculation before division.

[Worked notebook](lesson.ipynb) · [Python script](lesson.py)

[native.c](native.c)

## Execute the native listing

An array has a known extent where it is declared. sizeof on the actual array gives a byte count. The literal 9.0 promotes the calculation before division. Track object lifetime, element count and representation separately. Bounds do not automatically travel with a pointer. Compiler warnings help expose conversions that deserve inspection.

## Read the output

A straight line is expected. The intercept is 32 and a ten-degree Celsius step adds 18 degrees Fahrenheit. The marks show the independent Python reference at each position.

## Recorded output

```text
Runtime: C
Native stdout: 14 32 50 68 86
Largest absolute difference: 0
```

## Interpreting the result

A straight line is expected. The intercept is 32 and a ten-degree Celsius step adds 18 degrees Fahrenheit.

![Values and numeric types, worked result](figure.svg)

## Exercise

Add −40 and a fractional Celsius reading. Describe any type change needed by the native programme.

## References

[C language reference and standard revisions](https://en.cppreference.com/w/c/language)
