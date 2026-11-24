from expenses import ask_expense, format_rs, print_report, total


def main():
    print("Expense Tracker shuru! (khali Enter = band)")
    expenses = []

    while True:
        expense = ask_expense()
        if expense is None:
            break
        expenses.append(expense)
        print(f"Add hua: {expense['item']}, {format_rs(expense['amount'])} [{expense['category'].upper()}]")

    print_report(expenses)
    if total(expenses) > 5000:
        print("Bhai, aaj kharcha zyada ho gaya!")


if __name__ == "__main__":
    main()
