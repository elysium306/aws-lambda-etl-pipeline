from __future__ import annotations
import sqlite3
from pathlib import Path
from typing import List, Dict, Any

def write_results_to_sqlite(results: List[Dict[str, Any]], db_path: str = "data/results.sqlite") -> int:
    Path(db_path).parent.mkdir(parents=True, exist_ok=True)

    con = sqlite3.connect(db_path)
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS transformed_orders (
            order_id TEXT,
            amount REAL,
            tax REAL,
            total REAL
        );
    """)
    cur.execute("DELETE FROM transformed_orders;")

    cur.executemany(
        "INSERT INTO transformed_orders (order_id, amount, tax, total) VALUES (?, ?, ?, ?);",
        [(r["order_id"], r["amount"], r["tax"], r["total"]) for r in results]
    )

    con.commit()
    cur.execute("SELECT COUNT(*) FROM transformed_orders;")
    count = cur.fetchone()[0]
    con.close()

    return int(count)
