package main

import (
	"log"
	"os"
)

func main() {
	mainWithLogger(log.New(os.Stderr, "git-remote-lafs", log.LstdFlags))
}

func mainWithLogger(logger *log.Logger) {
	logger.Println("Hello World!")
}
