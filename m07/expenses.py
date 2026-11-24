import json
from dataclasses import asdict, dataclass
from pathlib import Path

DATA_FILE = Path("expenses.json")


def format_rs(amount: int) -> str:
    """Raqam ko 'Rs 1,500' ki shakal mein do."""
    return f"Rs {amount:,}"


@dataclass
class Expense:
    item: str
    amount: int
    category: str

    def label(self) -> str:
        """Ek line: 'Chai Paratha, Rs 1,500 [KHANA]'."""
        return f"{self.item}, {format_rs(self.amount)} [{self.category.upper()}]"


def ask_amount() -> int:
    """Raqam poocho, jab tak sahi number na mile."""
    while True:
        text = input("Kitne rupay? ")
        try:
            amount = int(text)
        except ValueError:
            print("Sirf number likho, jaise 1500.")
            continue
        if amount <= 0:
            print("Raqam zero se zyada honi chahiye.")
            continue
        return amount


def ask_expense() -> Expense | None:
    """User se ek kharcha poocho. Khali naam par None."""
    item = input("Kharcha kis cheez ka? ").strip().title()
    if item == "":
        return None
    amount = ask_amount()
    category = input("Category? (khana/safar/bill) ").strip().lower()
    return Expense(item, amount, category)


def total(expenses: list[Expense]) -> int:
    """Saare kharchon ka total."""
    return sum(e.amount for e in expenses)


def print_report(expenses: list[Expense]) -> None:
    """Saare kharche aur total print karo."""
    print("--- Aap ke kharche ---")
    for e in expenses:
        print(e.label())
    print(f"Total: {format_rs(total(expenses))}")


def load_expenses() -> list[Expense]:
    """File se kharche lao. File na ho to khali list."""
    if not DATA_FILE.exists():
        return []
    try:
        data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        raise SystemExit(f"{DATA_FILE} kharab hai. Comma ya bracket check karo.")
    return [Expense(**d) for d in data]


def save_expenses(expenses: list[Expense]) -> None:
    """Saare kharche file mein save karo."""
    data = [asdict(e) for e in expenses]
    text = json.dumps(data, indent=2, ensure_ascii=False)
    DATA_FILE.write_text(text, encoding="utf-8")
