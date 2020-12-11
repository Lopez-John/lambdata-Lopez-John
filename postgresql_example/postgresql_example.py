"""Module 2 example with PostGreSQL"""

import sqlite3
import psycopg2
from queries_sql import CREATE_TABLE, INSERT_STATEMENT, CREATE_CHARACTER_TABLE, GET_CHARACTERS


# PostGre Details - User & Default database
DBNAME = "ytwptqxp"
# PostGre Details - User & Default database
USER = "ytwptqxp"
# PostGre Details - Password
PASSWORD = "jDQN23vmEUoCbvVehUkGRmCm11QTuIup"
# PostGre Details - Server
HOST = "suleiman.db.elephantsql.com"

# Connects to PostGreSQL
def connect_db(DBNAME = DBNAME, USER=USER, PASSWORD=PASSWORD, HOST=HOST):
    # using psycogp2, connects to the PostGreSQL
    pg_conn = psycopg2.connect(dbname = DBNAME, user=USER, 
                            password=PASSWORD, host=HOST)
    #creates a PostGreSQL cursor
    pg_curs = pg_conn.cursor()
    return pg_conn, pg_curs

# connects to RPG sql database
def connect_sl_db(dbname='rpg_db.sqlite3'):
    # connects to the RPG database
    sl_conn = sqlite3.connect(dbname)
    # creates a sqlite3 cursor
    sl_curs = sl_conn.cursor()
    return sl_conn, sl_curs

# fetaches all the rows from the charactercreator_character table in the rpg_db.sqlite3
def execute_query(curs, query='SELECT * FROM charactercreator_character:'):
    #executes the passed through query
    curs.execute(query)
    # fetches all rows of a query result set
    return curs.fetchall()


def generate_characters_table(pg_conn, pg_curs, sl_curs):
    #create a new charactercreator_character table in the PostGreSQL
    pg_curs.execute(CREATE_CHARACTER_TABLE)
    # grabs all the rows from charactercreator_character table in sqlite3
    characters = sl_curs.execute(GET_CHARACTERS)
    # creates a new character value in the table charactercreator_character in PostSql from
    # the characters in charactercreator_character table in sqlite3
    for character in characters:
        # insert query for a new character with values from sqlite3
        insert_character = """
            INSERT INTO charactercreator_character
            (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
            VALUES {};
        """.format(character[1:])
        # prints the details of the character
        print(insert_character)
        # executes query and adds character's traits in PostGreSQL
        pg_curs.execute(insert_character)
    #commits the change made into PostGreSQL
    pg_conn.commit()


if __name__ == '__main__':
    pg_conn, pg_curs = connect_db()
    #execute_query(pg_curs, CREATE_TABLE)
    #execute_query(pg_curs, INSERT_STATEMENT)
    #pg_conn.commit()
    sl_conn, sl_curs = connect_sl_db()
    generate_characters_table(pg_conn, pg_curs, sl_curs)
    execute_query(curs=pg_curs)
