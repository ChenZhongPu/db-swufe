from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://postgres:@localhost:5432/mydb", future=True)

from sqlalchemy.orm import registry, session
mapper_registry = registry()
Base = mapper_registry.generate_base()

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

class Department(Base):
    __table__ = dept_table

    def __repr__(self):
        return f"Department({self.dept_name!r}"



from sqlalchemy.orm import Session

# select
from sqlalchemy import select
stmt = select(Department).where(dept_table.c.building == 'Watson')
with Session(engine) as session:
    for row in session.execute(stmt):
        print(row)

# insert
marx = Department(dept_name='Marx', building='Wastson', budget=80000.0)
session = Session(engine)
session.add(marx)
session.flush()
session.commit()