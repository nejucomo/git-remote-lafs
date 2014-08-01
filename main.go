package main

import (
	"log"
	"os"
)

const (
	logPrefix = "[git-remote-lafs] "
	logFlags  = log.LstdFlags
)

func main() {
	mainWithLogger(log.New(os.Stderr, logPrefix, logFlags))
}

func mainWithLogger(logger *log.Logger) {
	logger.Println("Hello World!")
}
