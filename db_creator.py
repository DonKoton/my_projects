import csv
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import insert

engine = create_engine('sqlite:///passwords.sqlite')
connection = engine.connect()

metadata = MetaData()
passwords = Table(
    'passwords',
    metadata,
    Column('service', String(64)),
    Column('login', String(64)),
    Column('password', String(64))
)

metadata.create_all(engine)

fixtures = []

with open('passes.csv') as csv_file:
    reader = csv.reader(csv_file)
    for item in reader:
        fixtures.append(
            {'service': item[0],
             'login': item[1],
             'password': item[2]})

stmt = insert(passwords)
results = connection.execute(stmt, fixtures)
print(results.rowcount)