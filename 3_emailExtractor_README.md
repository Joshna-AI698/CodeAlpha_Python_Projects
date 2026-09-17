# Email Address Extractor

## Description

Email Address Extractor is a simple Python automation project that reads a text file, identifies email addresses from the text, and saves the extracted email addresses into a separate text file.

## Features

- Reads text from a `.txt` file
- Finds email addresses automatically
- Extracts multiple email addresses
- Saves the extracted emails into a separate file
- Displays the extracted email addresses in the console

## Technologies Used

- Python
- `re` module
- File handling

## How It Works

1. The program reads `sample_text.txt`.
2. A regular expression is used to find email addresses.
3. The extracted email addresses are stored in a list.
4. The program saves them into `extracted_emails.txt`.
5. The extracted emails are also displayed in the console.

## Files

- `email_extractor.py` — Python source code
- `sample_text.txt` — Input text file containing email addresses
- `extracted_emails.txt` — Output file containing the extracted email addresses

## How to Run

Make sure Python is installed, then run:

```bash
python email_extractor.py
```

## Concepts Used

- Regular Expressions
- File Handling
- Lists
- Loops
- Input and Output

## Internship

This project was developed as part of the CodeAlpha Python Internship.
