def format_rs(amount: int) -> str:
    """Raqam ko 'Rs 1,500' ki shakal mein do."""
    return f"Rs {amount:,}"


def ask_expense() -> dict | None:
    """User se ek kharcha poocho. Khali naam par None."""
    item = input("Kharcha kis cheez ka? ").strip().title()
    if item == "":
        return None
    amount = int(input("Kitne rupay? "))
    category = input("Category? (khana/safar/bill) ").strip().lower()
    return {"item": item, "amount": amount, "category": category}


def total(expenses: list[dict]) -> int:
    """Saare kharchon ka total."""
    return sum(e["amount"] for e in expenses)


def print_report(expenses: list[dict]) -> None:
    """Saare kharche aur total print karo."""
    print("--- Aap ke kharche ---")
    for e in expenses:
        print(f"{e['item']}: {format_rs(e['amount'])}")
    print(f"Total: {format_rs(total(expenses))}")
