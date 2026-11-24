# Expense Tracker (Python CLI)

Track your daily expenses from the terminal. See the total in rupees and US dollars (live rate), and get a warning when you cross your monthly limit.

## Features

- Add an expense: item, amount, category (khana / safar / bill)
- Expenses are saved in `expenses.json`, so nothing is lost when the program closes
- Live USD rate from [open.er-api.com](https://open.er-api.com) (no API key needed)
- Menu: add, list, this month's total
- Monthly limit from a `.env` file, with a warning
- Wrong input (like `abc` for the amount) is handled, no crash

## How to run

1. Install [uv](https://docs.astral.sh/uv/getting-started/installation/)
2. Clone and open the project:
   ```
   git clone https://github.com/USERNAME/expense-tracker.git
   cd expense-tracker
   ```
3. Copy `.env.example` to `.env` and set your limit
4. Run:
   ```
   uv run main.py
   ```

## What I learned

Python basics for AI engineering: strings, lists, dicts, functions, type hints, files, JSON, `.env`, errors, dataclasses, HTTP with httpx, and async.
