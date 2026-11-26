# Values and numeric types

Convert five readings from Celsius to Fahrenheit and examine where arithmetic changes type.

The offset belongs after multiplication by the scale factor. Check the freezing point by hand, then inspect a value that would expose early integer division. All plotted points share the same transformation, so equal increments on the input scale must give equal increments on the output scale.

A constexpr std::array has fixed size. Type deduction gives integer elements, and the floating constant determines the arithmetic type.

[Worked notebook](lesson.ipynb) · [Python script](lesson.py)

[native.cpp](native.cpp)

## Execute the native listing

A constexpr std::array has fixed size. Type deduction gives integer elements, and the floating constant determines the arithmetic type. Look at the lifetime of each object and the owner of its storage. Passing a const reference permits observation without copying the container. Algorithms operate on half-open iterator ranges.

## Read the output

A straight line is expected. The intercept is 32 and a ten-degree Celsius step adds 18 degrees Fahrenheit. The marks show the independent Python reference at each position.

## Recorded output

```text
Runtime: C++
Native stdout: 14 32 50 68 86
Largest absolute difference: 0
```

## Interpreting the result

A straight line is expected. The intercept is 32 and a ten-degree Celsius step adds 18 degrees Fahrenheit.

![Values and numeric types, worked result](figure.svg)

## Exercise

Add −40 and a fractional Celsius reading. Describe any type change needed by the native programme.

## References

[C++ language and standard library reference](https://en.cppreference.com/w/cpp)
