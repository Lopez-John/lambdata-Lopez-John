import sqlite3
import queries

def connect_to_db(db_name = 'rpg_db.sqlite3'):
    conn = sqlite3.connect(db_name)
    return conn

def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()


if __name__ == '__main__':
    conn = connect_to_db()
    curs = conn.cursor()
    results = execute_query(curs, queries.QUERY_1)
    print(results)
    results = execute_query(curs, queries.QUERY_2)
    print(results)
    results = execute_query(curs, queries.QUERY_3)
    print(results)
    results = execute_query(curs, queries.QUERY_4)
    print(results)
    results = execute_query(curs, queries.QUERY_5)
    print(results)

