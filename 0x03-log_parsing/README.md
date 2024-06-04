# 0x03. Log Parsing

This project is about parsing and processing data streams in real-time using Python. The main task is to read from standard input (stdin), handle data in a specific format, and perform calculations based on the input data.

## Concepts Needed:

- File I/O in Python: Understand how to read from sys.stdin line by line.
- Signal Handling in Python: Handling keyboard interruption (CTRL + C) using signal handling in Python.
- Data Processing: Parsing strings to extract specific data points. Aggregating data to compute summaries.
- Regular Expressions: Using regular expressions to validate the format of each line.
- Dictionaries in Python: Using dictionaries to count occurrences of status codes and accumulate file sizes.
- Exception Handling: Handling possible exceptions that may arise during file reading and data processing.

## Requirements

- Allowed editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style (version 1.7.x)
- All your files must be executable
- The length of your files will be tested using wc

## Task

### 0. Log parsing

Write a script that reads stdin line by line and computes metrics:

- Input format: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>` (if the format is not this one, the line must be skipped)
- After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:
  - Total file size: File size: `<total size>`
  - where `<total size>` is the sum of all previous `<file size>` (see input format above)
  - Number of lines by status code:
    - possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
    - if a status code doesn’t appear or is not an integer, don’t print anything for this status code
    - format: `<status code>: <number>`
    - status codes should be printed in ascending order

## Repository

- GitHub repository: alx-interview
- Directory: 0x03-log_parsing
- File: 0-stats.py
