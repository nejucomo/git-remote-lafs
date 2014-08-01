package main

import (
	"io"
	"log"
)

func main() {
	mainWithLogger(log.New(io.Stderr, "git-remote-lafs", log.LstdFlags))
}

func mainWithLogger(logger *log.Logger) {
	logger.Println("Hello World!")
}
