import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect(host="localhost", port=5432, dbname="mydb", user="postgres")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
cur.execute("SELECT * FROM department")

# Retrieve query results
records = cur.fetchall()

print(records)

try:
    cur.execute("INSERT INTO department(dept_name, building, budget) VALUES(%s, %s, %s)",
    ('Marx', 'Watson', 80000.0))
    conn.commit()
except Exception as sqle:
    print("could not insert", sqle)
    conn.rollback()

## TODO: delete