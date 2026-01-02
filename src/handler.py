from __future__ import annotations
from typing import Any, Dict

from src.etl import transform_orders
from src.db import write_results_to_sqlite

def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    orders = event.get("orders", [])
    results = transform_orders(orders)
    written = write_results_to_sqlite(results)

    return {
        "statusCode": 200,
        "body": {
            "input_count": len(orders),
            "output_count": len(results),
            "rows_written": written,
        },
    }
