package main

import (
	"fmt"
)

func main() {
	inputs := []int{-1, 0, 2, 5}
	type result struct{ index, value int }
	ch := make(chan result, len(inputs))
	for i, x := range inputs {
		go func(i, x int) { ch <- result{i, 3*x + 2} }(i, x)
	}
	output := make([]int, len(inputs))
	for range inputs {
		r := <-ch
		output[r.index] = r.value
	}
	for _, v := range output {
		fmt.Print(v, " ")
	}
}
