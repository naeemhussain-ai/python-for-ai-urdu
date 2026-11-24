# Module 8: HTTP aur async (httpx)

Ab total rupay ke saath US dollar mein bhi aata hai. Dollar ka live rate internet se aata hai ([open.er-api.com](https://open.er-api.com), API key ki zaroorat nahi).

- `expenses.py`: `get_usd_rate()` httpx se rate laata hai
- `async_demo.py`: teen rates (USD, SAR, AED) pehle ek ek karke, phir async se ek saath, aur dono ka time

## Chalane ka tareeqa

1. `.env.example` ki copy banao aur naam `.env` rakho
2. Chalao:
   ```
   uv run main.py
   ```
3. Async demo:
   ```
   uv run async_demo.py
   ```

Internet na ho to total sirf rupay mein aata hai, aur program bata deta hai ke dollar rate nahi mila.
