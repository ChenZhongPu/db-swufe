from __future__ import annotations

from pathlib import Path

import duckdb


DB_PATH = Path(__file__).resolve().parent / "mydb.db"


def run() -> None:
    print("\n=== DuckDB database file ===")

    with duckdb.connect(str(DB_PATH), read_only=True) as con:
        print("Tables:")
        print(con.sql("SHOW TABLES"))

        print("Top students by total credits:")
        print(
            con.sql(
                """
                SELECT ID, name, dept_name, tot_cred
                FROM student
                ORDER BY tot_cred DESC, ID
                LIMIT 5
                """
            )
        )

        print("Student count by department:")
        print(
            con.sql(
                """
                SELECT
                    dept_name,
                    count(*) AS student_count,
                    round(avg(tot_cred), 2) AS avg_total_credits
                FROM student
                GROUP BY dept_name
                ORDER BY student_count DESC, dept_name
                """
            )
        )


if __name__ == "__main__":
    run()
