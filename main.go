package main

import (
	"flag"
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
	flag.Parse()
	repo := flag.Arg(0)
	url := flag.Arg(1)

	logger.Printf("Hello World! repo: %v; url %v\n", repo, url)
}
