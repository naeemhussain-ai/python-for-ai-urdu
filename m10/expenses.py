import json
from dataclasses import asdict, dataclass, field
from datetime import date
from pathlib import Path

import httpx

DATA_FILE = Path("expenses.json")
RATE_URL = "https://open.er-api.com/v6/latest/USD"


def today() -> str:
    """Aaj ki date, jaise '2026-11-20'."""
    return date.today().isoformat()


def current_month() -> str:
    """Is mahine ka naam, jaise '2026-11'."""
    return date.today().strftime("%Y-%m")


def format_rs(amount: int) -> str:
    """Raqam ko 'Rs 1,500' ki shakal mein do."""
    return f"Rs {amount:,}"


@dataclass
class Expense:
    item: str
    amount: int
    category: str
    day: str = field(default_factory=today)

    def label(self) -> str:
        """Ek line: '2026-11-20 | Chai Paratha, Rs 1,500 [KHANA]'."""
        return f"{self.day} | {self.item}, {format_rs(self.amount)} [{self.category.upper()}]"


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


def month_total(expenses: list[Expense], month: str) -> int:
    """Ek mahine ke kharchon ka total. month jaise '2026-11'."""
    return sum(e.amount for e in expenses if e.day.startswith(month))


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


def get_usd_rate() -> float | None:
    """1 dollar kitne rupay ka hai (live). Internet na ho to None."""
    try:
        response = httpx.get(RATE_URL, timeout=10)
        response.raise_for_status()
    except httpx.HTTPError:
        return None
    return response.json()["rates"]["PKR"]


def print_usd(amount: int) -> None:
    """Raqam dollar mein dikhao (live rate)."""
    rate = get_usd_rate()
    if rate is None:
        print("Dollar rate nahi mila. Internet check karo.")
    else:
        print(f"Dollar mein: ${amount / rate:,.2f} (1 USD = Rs {rate:.2f})")
