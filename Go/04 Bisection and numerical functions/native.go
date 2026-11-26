package main

import (
	"errors"
	"fmt"
	"math"
)

func root(n float64) (float64, error) {
	if n < 0 {
		return 0, errors.New("negative radicand")
	}
	if n == 0 {
		return 0, nil
	}
	lo, hi := 0.0, math.Max(1, n)
	for i := 0; i < 55; i++ {
		mid := (lo + hi) / 2
		if mid*mid < n {
			lo = mid
		} else {
			hi = mid
		}
	}
	return (lo + hi) / 2, nil
}

func main() {
	for _, n := range []float64{0, .5, 2, 10, 25} {
		value, err := root(n)
		if err != nil {
			panic(err)
		}
		fmt.Print(value, " ")
	}
}
