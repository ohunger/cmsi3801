package main

import (
	"fmt"
	"io"
	"net/http"
	"os"
	"sync"
)

func main() {
	if len(os.Args) != 2 {
		fmt.Println("Usage: go run main.go <URL>")
		os.Exit(1)
	}

	// Get the URL
	url := os.Args[1]

	// Create a WaitGroup to wait for all Goroutines to finish
	var wg sync.WaitGroup

	// Create a channel to communicate between Goroutines
	ch := make(chan string)

	// Launch multiple Goroutines to download the page
	for i := 0; i < 3; i++ { // You can adjust the number of Goroutines as needed
		wg.Add(1)
		go downloadPage(url, &wg, ch)
	}

	// Close the channel once all Goroutines are done
	go func() {
		wg.Wait()
		close(ch)
	}()

	// Collect results from the channel and print them
	for bodyString := range ch {
		fmt.Println(bodyString)
	}
}

func downloadPage(url string, wg *sync.WaitGroup, ch chan<- string) {
	defer wg.Done()

	// Download page
	resp, err := http.Get(url)
	if err != nil {
		fmt.Println("Error:", err)
		return
	}
	defer resp.Body.Close()

	// Read body
	bodyBytes, err := io.ReadAll(resp.Body)
	if err != nil {
		fmt.Println("Error in reading:", err)
		return
	}
	bodyString := string(bodyBytes)

	// Send the result to the channel
	ch <- bodyString
}