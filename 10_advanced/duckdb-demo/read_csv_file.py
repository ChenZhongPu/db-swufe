from __future__ import annotations

from pathlib import Path

import duckdb


CSV_PATH = Path(__file__).resolve().parent / "customers.csv"


def run() -> None:
    print("\n=== CSV file ===")
    csv_path = "'" + str(CSV_PATH).replace("'", "''") + "'"

    with duckdb.connect() as con:
        print("Preview:")
        print(
            con.sql(
                f"""
                SELECT *
                FROM read_csv_auto({csv_path}, header = true)
                ORDER BY customer_id
                LIMIT 5
                """
            )
        )

        print("Aggregated by city:")
        print(
            con.sql(
                f"""
                SELECT
                    city,
                    count(*) AS customer_count,
                    round(avg(lifetime_value), 2) AS avg_lifetime_value
                FROM read_csv_auto({csv_path}, header = true)
                GROUP BY city
                ORDER BY customer_count DESC, city
                """
            )
        )


if __name__ == "__main__":
    run()
