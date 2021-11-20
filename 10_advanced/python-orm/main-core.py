from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://postgres:@localhost:5432/mydb", future=True)

print('---start of raw sql---')
# raw sql
from sqlalchemy import text
with engine.connect() as conn:
    result = conn.execute(text("select * from department"))
    print(result.all())
print('---end of raw sql---')
# core
# 1. working with database metadata
from sqlalchemy import MetaData
metadata_obj = MetaData()
# register a table
from sqlalchemy import Table, Column, Float, String
dept_table = Table(
    "department",
    metadata_obj,
    Column('dept_name', String, primary_key=True),
    Column('building', String),
    Column('budget', Float)
)
# select
print('---start of core select---')
from sqlalchemy import select
stmt = select(dept_table).where(dept_table.c.building == 'Watson')
with engine.connect() as conn:
    for row in conn.execute(stmt):
        print(row)
print('---enf of core select---')
# insert
# from sqlalchemy import insert
# stmt = insert(dept_table).values(dept_name='Marx', building='Wastson', budget=80000.0)
# with engine.connect() as conn:
#     result = conn.execute(stmt)
#     conn.commit()
# delete
# from sqlalchemy import delete
# stmt = delete(dept_table).where(dept_table.c.dept_name == 'Marx')
# with engine.connect() as conn:
#     result = conn.execute(stmt)
#     conn.commit()