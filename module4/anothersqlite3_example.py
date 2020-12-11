"""creating and inserting data with sqlite"""
import sqlite3



def create_table(conn):
    curs = conn.cursor()
    create_table = '''
        CREATE TABLE students(
            id INTEGER PRIMARY KEY AUTOINCREMENT
            name CHAR(20)
            favorite_number INTEGER
            leaste_favorite_number INTEGER 
            );
        '''
    curs.execute(create_table)
    curs.close()
    conn.commit()

def insert_date(conn, data):
    curs = conn.cursor()
    for date_point in data:
        insert_data = '''
            INSERT INTO students
            VALUES (
                {}
            )
        '''.format(data_point)
        curs.execute(insert_data)
    curs.close()
    conn.commit()

def show_all(conn):
    curs = conn.cursor()
    curs.execute('SELECT * FROM students')
    info = curs.fetchall()
    curs.close()
    return curs

if __name__ == '__main__':
    data = [
        ('Nick', 77, 13),
        ('John', 101, 1010)
    ]
    conn = sqlite3.connect('example_db.sqlite3')
    create_table(conn)
    insert_data(conn, data)
    show_all(conn)
