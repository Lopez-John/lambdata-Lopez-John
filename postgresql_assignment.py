"""Creates a new table of characters in PostGreSQL from a characters in 
a table in sqlite3"""

import sqlite3
import psycopg2

DBNAME = 'ytwptqxp'
USER = 'ytwptqxp'
PASSWORD = 'jDQN23vmEUoCbvVehUkGRmCm11QTuIup'
HOST = 'suleiman.db.elephantsql.com'

#Queries
create_character_table = """
    CREATE TABLE charactercreator_character (
        character_id SERIAL PRIMARY KEY,
        name VARCHAR(30),
        level INT,
        exp INT,
        hp INT,
        strength INT,
        intelligence INT,
        dexterity INT,
        wisdom INT
    );
    """

get_characters = """
    SELECT * FROM charactercreator_character;
"""


# Connects to PostGreSQL database
def connect_pg_db(DBNAME=DBNAME, USER=USER, PASSWORD=PASSWORD, HOST=HOST):
    pg_conn = psycopg2.connect(dbname = DBNAME, user = USER,
                                password=PASSWORD, host=HOST)
    pg_curs = pg_conn.cursor()
    return pg_conn, pg_curs

# Connects to sqlite3 database
def connect_sl_db(dbname='rpg_db.sqlite3'):
    sl_conn = sqlite3.connect(dbname)
    sl_curs = sl_conn.cursor()
    return sl_conn, sl_curs

# creates a character table in PostGRESQL
def generate_characters_table(pg_conn, pg_curs, sl_curs):
    pg_curs.execute(create_character_table)
    characters = sl_curs.execute(get_characters)
    for character in characters:
        insert_character = """
        INSERT INTO charactercreator_character
        (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
        VALUES {};
        """.format(character[1:])
        print (insert_character)
        pg_curs.execute(insert_character)
    pg_conn.commit()

if __name__ == '__main__':
    pg_conn, pg_curs = connect_pg_db()
    sl_conn, sl_curs = connect_sl_db()
    generate_characters_table(pg_conn, pg_curs, sl_curs)