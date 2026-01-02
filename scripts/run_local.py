from pathlib import Path
import sys

# Add repo root to Python path so "src" imports work when running from scripts/
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.handler import lambda_handler  # noqa: E402

if __name__ == "__main__":
    event = {
        "orders": [
            {"order_id": "A1", "amount": 100, "status": "PAID"},
            {"order_id": "A2", "amount": 50, "status": "PENDING"},
            {"order_id": "A3", "amount": 12.5, "status": "PAID"},
        ]
    }
    print(lambda_handler(event, None))
