import sqlite3
from faker import Faker

fake = Faker("de_AT")
conn = sqlite3.connect("names.db")
c = conn.cursor()

names = []
for i in range (1, 500001):
    vorname = fake.first_name()
    nachname = fake.last_name()
    names.append((i, vorname, nachname))


c.execute(
    """CREATE TABLE IF NOT EXISTS personen(
    id INTEGER PRIMARY KEY,
    vorname TEXT NOT NULL,
    nachname TEXT NOT NULL);
    """
    )

c.executemany(
    "INSERT INTO personen (id, vorname, nachname) VALUES (?, ?, ?)",
    names
    )

conn.commit()
print("Data inserted successfully")
conn.close()
