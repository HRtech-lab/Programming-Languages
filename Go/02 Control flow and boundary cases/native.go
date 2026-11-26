package main

import (
	"fmt"
)

func main() {
	var counts [3]int
	for _, n := range []int{-4, 0, 5, 12, 18, 25, 31} {
		switch {
		case n <= 0:
			counts[0]++
		case n < 20:
			counts[1]++
		default:
			counts[2]++
		}
	}
	for _, count := range counts {
		fmt.Print(count, " ")
	}
}
