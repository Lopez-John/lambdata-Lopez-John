import sqlite3

#for connecting to Chinnok database
def connect_to_db(db_name='Chinnok_Sqlite.sqlite'):
        conn = sqlite3.connect(db_name)
        return conn

# for executing queries
def execute_query(cursor, query)
    cursor.execute(query)
    return cursor.fetchall()

# Queries



# Return all columns in Customer for the first 5 customers residing in the United States
QUERY2 = """
    SELECT *
    FROM Customer
    WHERE Country = 'USA'
    LIMIT 5
    """
# Which employee does not report to anyone?
Query3 = """
    SELECT *
    FROM Employee
    WHERE ReportsTo Is NULL
    """
# Find the number of unique composers
Query4 = """
    SELECT COUNT(name)
    FROM Artist
    """
# How many rows are in the Track table?​Joins
Query5 = """
    SELECT COUNT(TrackId)
    FROM Track
    """

# Get the name of all Black Sabbath tracks and the albums they came off of


if __name__='__main__':
    conn = connect_to_db()
    cursor = conn.cursor()
    question1 = execute_query(curs,)
