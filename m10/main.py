import os

from dotenv import load_dotenv

from expenses import (
    ask_expense,
    current_month,
    format_rs,
    load_expenses,
    month_total,
    print_report,
    print_usd,
    save_expenses,
    total,
)

load_dotenv()
MONTHLY_LIMIT = int(os.getenv("MONTHLY_LIMIT", "50000"))

MENU = """
1. Kharcha add karo
2. Saare kharche
3. Is mahine ka total
4. Band karo"""


def main():
    expenses = load_expenses()
    print(f"Expense Tracker! Pehle se {len(expenses)} kharche.")

    while True:
        print(MENU)
        choice = input("Kya karna hai? (1-4) ").strip()

        if choice == "1":
            expense = ask_expense()
            if expense is not None:
                expenses.append(expense)
                save_expenses(expenses)
                print(f"Add hua: {expense.label()}")
        elif choice == "2":
            print_report(expenses)
            print_usd(total(expenses))
        elif choice == "3":
            month = current_month()
            amount = month_total(expenses, month)
            print(f"{month} ka total: {format_rs(amount)} (limit {format_rs(MONTHLY_LIMIT)})")
            if amount > MONTHLY_LIMIT:
                print("Bhai, is mahine ki limit cross ho gayi! Kal thora sambhal ke.")
        elif choice == "4":
            print("Allah Hafiz! Kharche save hain.")
            break
        else:
            print("Sirf 1, 2, 3 ya 4 likho.")


if __name__ == "__main__":
    main()
