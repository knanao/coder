package main

import (
	"fmt"
	"strconv"
)

func main() {
	fmt.Printf("ex.1: %v\n", countBits(2))
	fmt.Printf("ex.2: %v\n", countBits(5))
}

func countBits(n int) []int {
	ret := make([]int, n+1)
	for i := 0; i <= n; i++ {
		b := strconv.FormatInt(int64(i), 2)
		d, _ := strconv.Atoi(b)
		ret[i] = sumDigits(d)
	}
	return ret
}

func sumDigits(n int) int {
	var sum int
	for n != 0 {
		d := n % 10
		sum += d
		n /= 10
	}
	return sum
}
