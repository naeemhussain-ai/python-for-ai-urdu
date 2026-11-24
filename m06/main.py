import os

from dotenv import load_dotenv

from expenses import ask_expense, format_rs, load_expenses, print_report, save_expenses, total

load_dotenv()
DAILY_LIMIT = int(os.getenv("DAILY_LIMIT", "5000"))


def main():
    expenses = load_expenses()
    print(f"Expense Tracker shuru! Pehle se {len(expenses)} kharche. (khali Enter = band)")

    while True:
        expense = ask_expense()
        if expense is None:
            break
        expenses.append(expense)
        save_expenses(expenses)
        print(f"Add hua: {expense['item']}, {format_rs(expense['amount'])} [{expense['category'].upper()}]")

    print_report(expenses)
    if total(expenses) > DAILY_LIMIT:
        print(f"Bhai, kharcha {format_rs(DAILY_LIMIT)} ki limit se zyada ho gaya!")


if __name__ == "__main__":
    main()
