# Birthday Wisher Automation Script

This Python script reads an Excel file and sends birthday wishing emails based on due dates.

## Features
- Reads `.xlsx` file using `openpyxl`
- Checks if the due date has passed
- Sends automated emails using `smtplib`

## Tech Stack
- Python
- openpyxl
- smtplib

## How to Use
1. Put your Excel file in the project directory.
2. Update your email credentials in `config.py`.
3. Run the script:
```bash
python main.py
