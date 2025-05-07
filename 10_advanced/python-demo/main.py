import psycopg

with psycopg.connect("dbname=mydb user=postgres port=5432 password=") as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM department")
        records = cur.fetchall()
        print(records)
