"""Creates a new table of passengers of in PostGreSQL from passengers
in a table in sqlite3"""

import sqlite3
import psycopg2

DBNAME = 'ytwptqxp'
USER = 'ytwptqxp'
PASSWORD = 'jDQN23vmEUoCbvVehUkGRmCm11QTuIup'
HOST = 'suleiman.db.elephantsql.com'

create_titanic_table = """ CREATE TABLE titanic_passengers
    (
        id SERIAL PRIMARY KEY,
        Survived INT,
        Pclass INT,
        Name VARCHAR(90),
        Sex VARCHAR(10),
        AGE FLOAT,
        Siblings_Spouses_Aboard INT,
        Parents_Children_Aboard INT,
        Fare FLOAT
    );
    """
get_passengers = """
    SELECT * FROM titanic;
    """

def connect_pg_db(DBNAME=DBNAME, USER=USER, PASSWORD=PASSWORD, HOST=HOST):
    pg_conn = psycopg2.connect(dbname = DBNAME, user = USER,
                                password=PASSWORD, host=HOST)
    pg_curs = pg_conn.cursor()
    return pg_conn, pg_curs

# Connects to sqlite3 database
def connect_sl_db(dbname='Titanic.sqlite3'):
    sl_conn = sqlite3.connect(dbname)
    sl_curs = sl_conn.cursor()
    return sl_conn, sl_curs

def generate_passengers_table(pg_conn, pg_curs, sl_curs):
    pg_curs.execute(create_titanic_table)
    passengers = sl_curs.execute(get_passengers)
    for passenger in passengers:
        insert_passenger = """
        INSERT INTO titanic_passengers
        (Survived, Pclass, Name, Sex, AGE, Siblings_Spouses_Aboard, Parents_Children_Aboard, Fare)
        VALUES {};
        """.format(passenger)
        pg_curs.execute(insert_passenger)
    pg_conn.commit()

if __name__ == "__main__":
    pg_conn, pg_curs = connect_pg_db()
    sl_conn, sl_curs = connect_sl_db()
    generate_passengers_table(pg_conn, pg_curs, sl_curs)