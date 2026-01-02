from __future__ import annotations
from typing import Any, Dict
from src.etl import transform_orders
from src.db import write_results_to_duckdb

def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Expected event shape:
    {
      "orders": [
        {"order_id": "A1", "amount": 100, "status": "PAID"},
        ...
      ]
    }
    """
    orders = event.get("orders", [])
    results = transform_orders(orders)
    written = write_results_to_duckdb(results)

    return {
        "statusCode": 200,
        "body": {
            "input_count": len(orders),
            "output_count": len(results),
            "rows_written": written
        }
    }
