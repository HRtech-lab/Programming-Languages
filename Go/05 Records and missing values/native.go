package main

import (
	"fmt"
)

type reading struct {
	id      string
	value   int
	present bool
}

func main() {
	rows := []reading{{"A", 3, true}, {"B", 8, true}, {"A", 5, true}, {"C", 2, true}, {"B", 0, false}}
	type group struct{ sum, count int }
	groups := map[string]group{}
	for _, r := range rows {
		if !r.present {
			continue
		}
		g := groups[r.id]
		g.sum += r.value
		g.count++
		groups[r.id] = g
	}
	for _, id := range []string{"A", "B", "C"} {
		g := groups[id]
		fmt.Print(float64(g.sum)/float64(g.count), " ")
	}
}
