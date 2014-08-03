package main

import (
	"flag"
	"fmt"
	"log"
	"os"
	"strings"
)

const (
	logPrefix = "[git-remote-lafs] "
	logFlags  = log.LstdFlags
)

func main() {
	logger := log.New(os.Stderr, logPrefix, logFlags)

	err := run(logger)

	if err == nil {
		os.Exit(0)
	} else {
		logger.Printf("Error: %s\n", err)
		os.Exit(1)
	}
}

func run(logger *log.Logger) error {
	repo, url, err := parseArgs()
	if err != nil {
		return err
	}

	logger.Printf("repo %#v; url %#v\n", repo, url)

	cap, err := parseLafsUrl(url)
	if err != nil {
		return err
	}

	logger.Printf("cap %#v\n", cap)

	return nil
}

func parseArgs() (repo, url string, err error) {
	flag.Parse()
	args := flag.Args()

	if len(args) == 2 {
		repo = args[0]
		url = args[1]
	} else {
		err = fmt.Errorf("Wrong number of arguments: %#v\n", args)
	}
	return
}

func parseLafsUrl(url string) (cap string, err error) {
	cap = url

	if strings.HasPrefix(cap, "lafs://") {
		cap = cap[7:]
	}

	return
}
