from src.etl import transform_orders

def test_transform_orders_filters_and_calculates():
    rows = [
        {"order_id": "A2", "amount": 50, "status": "PENDING"},
        {"order_id": "A1", "amount": 100, "status": "PAID"},
        {"order_id": "A3", "amount": 12.5, "status": "PAID"},
    ]

    out = transform_orders(rows)

    assert len(out) == 2
    assert out[0]["order_id"] == "A1"
    assert out[0]["tax"] == 8.00
    assert out[0]["total"] == 108.00
    assert out[1]["order_id"] == "A3"
    assert out[1]["tax"] == 1.00
    assert out[1]["total"] == 13.50
