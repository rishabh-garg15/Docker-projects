package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"os"
)

func handler(w http.ResponseWriter, r *http.Request) {
	info := map[string]string{
		"project":     "Minimal Go Docker App",
		"description": "A tiny web server to demonstrate minimal Docker setup in Go",
		"author":      "Rishabh Garg",
		"version":     "1.0.0",
		"status":      "Running",
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(info)
}

func main() {
	port := os.Getenv("APP_PORT")
	if port == "" {
		port = "8081"
	}
	http.HandleFunc("/", handler)
	fmt.Printf("Starting server on port %s...\n", port)
	http.ListenAndServe(":"+port, nil)
}

