from __future__ import annotations
import sqlite3
from typing import List, Dict, Any

def transform_orders(rows: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Example transformation:
    - input: [{order_id, amount, status}, ...]
    - output: only PAID orders with a computed tax and total
    """
    con = sqlite3.connect(":memory:")
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE orders (
            order_id TEXT,
            amount REAL,
            status TEXT
        );
    """)

    cur.executemany(
        "INSERT INTO orders (order_id, amount, status) VALUES (?, ?, ?);",
        [(r["order_id"], float(r["amount"]), r["status"]) for r in rows]
    )

    cur.execute("""
        SELECT
            order_id,
            amount,
            ROUND(amount * 0.08, 2) AS tax,
            ROUND(amount * 1.08, 2) AS total
        FROM orders
        WHERE status = 'PAID'
        ORDER BY order_id;
    """)
    result = cur.fetchall()
    con.close()

    return [
        {"order_id": r[0], "amount": r[1], "tax": r[2], "total": r[3]}
        for r in result
    ]
