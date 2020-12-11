"""Basic example for sprint 2 module 1"""
import sqlite3

# for connecting to our database
def connect_to_db(db_name='rpg_db.sqlite3'):
    conn = sqlite3.connect(db_name)
    return conn

# for executing READ queries
def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()

#Query
GET_CHARACTERS = """
    SELECT *
    FROM charactercreator_character;
    """


if __name__ == '__main__':
    conn = connect_to_db()
    curs = conn.cursor()
    results = execute_query(curs, GET_CHARACTERS)
    print(results[:5])
    print(len(results))
