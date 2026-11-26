package main

import (
	"fmt"
)

func prefix(changes []int) []int {
	result := make([]int, len(changes))
	total := 0
	for i, change := range changes {
		total += change
		result[i] = total
	}
	return result
}

func main() {
	changes := []int{3, -1, 4, -2, 0, 2}
	for _, v := range prefix(changes) {
		fmt.Print(v, " ")
	}
}
