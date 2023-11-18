package main

import "fmt"

func fibonacciGenerator() func() int {
	a, b := 0, 1
	return func() int {
		result := a
		a, b = b, a+b
		return result
	}
}

func main() {
	fibonacci := fibonacciGenerator()
	for i := 0; i < 10; i++ {
		fmt.Println(fibonacci())
	}
}