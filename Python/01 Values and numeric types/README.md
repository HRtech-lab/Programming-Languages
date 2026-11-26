# Values and numeric types

Convert five readings from Celsius to Fahrenheit and examine where arithmetic changes type.

The offset belongs after multiplication by the scale factor. Check the freezing point by hand, then inspect a value that would expose early integer division. All plotted points share the same transformation, so equal increments on the input scale must give equal increments on the output scale.

Lists and comprehensions preserve iteration order. True division returns a float.

[Worked notebook](lesson.ipynb) · [Python script](lesson.py)

[native.py](native.py)

## Execute the native listing

Lists and comprehensions preserve iteration order. True division returns a float. Python evaluates the iterator when the caller asks for its next item. Put the break point inside the loop when inspecting a lazy calculation.

## Read the output

A straight line is expected. The intercept is 32 and a ten-degree Celsius step adds 18 degrees Fahrenheit. The marks show the independent Python reference at each position.

## Recorded output

```text
Runtime: Python
Native stdout: 14.0 32.0 50.0 68.0 86.0
Largest absolute difference: 0
```

## Interpreting the result

A straight line is expected. The intercept is 32 and a ten-degree Celsius step adds 18 degrees Fahrenheit.

![Values and numeric types, worked result](figure.svg)

## Exercise

Add −40 and a fractional Celsius reading. Describe any type change needed by the native programme.

## References

[Python language tutorial](https://docs.python.org/3/tutorial/)
