package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	f, err := os.Open("readings.csv")
	if err != nil {
		panic(err)
	}
	defer f.Close()
	scan := bufio.NewScanner(f)
	if !scan.Scan() {
		panic("missing header")
	}
	count, sum, lo, hi, rejected := 0, 0, 0, 0, 0
	for scan.Scan() {
		v, err := strconv.Atoi(strings.TrimSpace(scan.Text()))
		if err != nil {
			rejected++
			continue
		}
		if count == 0 || v < lo {
			lo = v
		}
		if count == 0 || v > hi {
			hi = v
		}
		sum += v
		count++
	}
	if err := scan.Err(); err != nil {
		panic(err)
	}
	if count == 0 {
		panic("no numeric rows")
	}
	fmt.Println(count, sum, lo, hi, rejected)
}
