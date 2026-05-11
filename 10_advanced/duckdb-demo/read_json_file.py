from __future__ import annotations

from pathlib import Path

import duckdb


JSON_PATH = Path(__file__).resolve().parent / "orders.json"


def run() -> None:
    print("\n=== JSON file ===")
    json_path = "'" + str(JSON_PATH).replace("'", "''") + "'"

    with duckdb.connect() as con:
        print("Orders preview:")
        print(
            con.sql(
                f"""
                SELECT order_id, customer_id, order_date, status, len(items) AS item_count
                FROM read_json_auto({json_path})
                ORDER BY order_id
                """
            )
        )

        print("Revenue by product from nested JSON items:")
        print(
            con.sql(
                f"""
                WITH line_items AS (
                    SELECT
                        orders.order_id,
                        orders.customer_id,
                        item.product AS product,
                        item.quantity AS quantity,
                        item.price AS price
                    FROM read_json_auto({json_path}) AS orders,
                    UNNEST(orders.items) AS item(item)
                )
                SELECT
                    product,
                    sum(quantity) AS units,
                    round(sum(quantity * price), 2) AS revenue
                FROM line_items
                GROUP BY product
                ORDER BY revenue DESC, product
                """
            )
        )


if __name__ == "__main__":
    run()
