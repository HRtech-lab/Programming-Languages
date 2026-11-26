package main

import (
	"fmt"
)

func main() {
	for _, c := range []int{-10, 0, 10, 20, 30} {
		fmt.Print(float64(c)*9/5+32, " ")
	}
}
