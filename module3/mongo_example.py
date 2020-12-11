"""pymongo example - SQLite to MongoDB Pipeline"""
import sqlite3
import pymongo


PASSWORD = "A2oU0l8VMXjYp2sh"
DBNAME ="test"

#Local SQLite DV
EXTRACTION_DB="rpg_db.sqlite3"

# Creating MongoDB connection
def create_mdb_connection(password=PASSWORD, dbname= DBNAME):
    # connects to existing database or creates a new database if Database name doesn't exist on MongoDB atlas
    client = pymongo.MongoClient(
        "mongodb+srv://WindowsOS-LopezJohn:{}@cluster00.3yt87.mongodb.net/{}?retryWrites=true&w=majority"
        .format(password, dbname)
        )
    return client

#creating SQLite connection
def create_sl_connection(extraction_db=EXTRACTION_DB):
    sl_conn = sqlite3.connect(extraction_db)
    return sl_conn

#creating character documents for MongoDB
def doc_creation(db, sl_curs, chararacter_table_query):
    characters = sl_curs.execute(chararacter_table_query)
    for character in characters:
        doc = {
            "name":character[1],
            'level': character[2],
            'exp': character[3],
            'hp' : character[4],
            'strength': character[5],
            'intelligence': character[6],
            'dexterity': character[7],
            'wisdom': character[8]
        }
        # insert character document
        db.insert_one(doc)



# Fucntion to show all documents in MongoDB
def show_all(db):
    #lists everything
    all_docs = list(db.find())
    return all_docs

# SQLite Queries

GET_CHARACTER_TABLE = """
    SELECT * 
    FROM charactercreator_character;
    """

if __name__ == '__main__':
    sl_conn = create_sl_connection()
    sl_curs = sl_conn.cursor()
    client = create_mdb_connection()
    db = client.test.test
    db.drop({})
    doc_creation(db, sl_curs, GET_CHARACTER_TABLE)
    print(show_all(db))


# Connects to the database 'test'
#db=client.test
