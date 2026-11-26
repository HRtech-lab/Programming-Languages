package main

import (
	"fmt"
)

type moments struct {
	count    int
	mean, m2 float64
}

func (s *moments) update(x float64) float64 {
	s.count++
	delta := x - s.mean
	s.mean += delta / float64(s.count)
	s.m2 += delta * (x - s.mean)
	return s.m2 / float64(s.count)
}

func main() {
	var s moments
	for _, offset := range []float64{1, 2, 4, 5} {
		fmt.Print(s.update(1e9+offset), " ")
	}
}
