package main

import (
	"bufio"
	"flag"
	"fmt"
	"io"
	"log"
	"os"
	"strings"
)

const (
	logPrefix = "[git-remote-lafs] "
	logFlags  = log.LstdFlags
)

type OutputFormatter func(format string, v ...interface{})

func main() {
	err := run(
		makeDebugFunc(os.Stderr),
		bufio.NewReader(os.Stdin),
		bufio.NewWriter(os.Stdout))

	if err == nil {
		os.Exit(0)
	} else {
		fmt.Fprintf(os.Stderr, "Error: %s\n", err)
		os.Exit(1)
	}
}

func run(debug OutputFormatter, in *bufio.Reader, out *bufio.Writer) error {
	repo, url, err := parseArgs()
	if err != nil {
		return err
	}

	debug("repo %#v; url %#v", repo, url)

	cap, err := parseLafsUrl(url)
	if err != nil {
		return err
	}

	debug("cap %#v", cap)

	return processCommands(debug, cap, in, out)
}

func parseArgs() (repo, url string, err error) {
	flag.Parse()
	args := flag.Args()

	if len(args) == 2 {
		repo = args[0]
		url = args[1]
	} else {
		err = fmt.Errorf("Wrong number of arguments: %#v", args)
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

func processCommands(debug OutputFormatter, cap string, in *bufio.Reader, out *bufio.Writer) (err error) {
	for err == nil {
		line, err2 := in.ReadString('\n')
		err = err2
		if err == nil || err == io.EOF {
			err = processCommand(debug, cap, line[:len(line)-1], out)
		}
	}
	return
}

func processCommand(debug OutputFormatter, cap, command string, out *bufio.Writer) (err error) {
	debug("executing command: %#v", command)

	defer out.Flush()

	if command == "" {
		// Hangup:
		err = io.EOF
	} else if command == "capabilities" {
		out.WriteString("push\n\n")
	} else if command == "list for-push" {
		out.WriteString("\n")
	} else {
		err = fmt.Errorf("Unknown command: %#v", command)
	}

	return
}

func makeDebugFunc(w io.Writer) OutputFormatter {
	logger := log.New(w, logPrefix, logFlags)

	return func(format string, v ...interface{}) {
		fullformat := fmt.Sprintf("[DEBUG] %s\n", format)
		logger.Printf(fullformat, v...)
	}
}
