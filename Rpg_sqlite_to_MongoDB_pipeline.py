"""SQLite to MongoDB Pipeline for Rpg_db"""
import sqlite3
import pymongo

PASSWORD = "A2oU0l8VMXjYp2sh"
DBNAME = "rpg_db"

# Local SQLITE DB
extraction_db = 'rpg_db.sqlite3'


# create MongoDb connection
def mdb_conn(password=PASSWORD, dbname=DBNAME):
    # connect to a new database, since rpg_db does not exist on MongoDB
    client = pymongo.MongoClient(
        "mongodb+srv://WindowsOS-LopezJohn:{}@cluster00.3yt87.mongodb.net/{}?retryWrites=true&w=majority"
        .format(password, dbname)
        )
    return client


# create SQLite connection to rpg_db
def sl_conn(extraction_db=extraction_db):
    sl_conn = sqlite3.connect(extraction_db)
    return sl_conn


# create Character documents for MongoDB
def character_creation(db, sl_curs, character_table_query):
    characters = sl_curs.execute(character_table_query).fetchall()
    armory = sl_curs.execute(armory_item_table).fetchall()
    weapon_armory = sl_curs.execute(armory_weapon_table).fetchall()
    for character in characters:
        character_items = []
        character_weapons = []
        for item in armory:
            if character[0] == item[1]:
                character_items.append(item[4])
                for weapon in weapon_armory:
                    if item[2] == weapon[0]:
                        character_weapons.append(item[4])
        doc = {
            "name": character[1],
            "level": character[2],
            "exp": character[3],
            "hp": character[4],
            "strength": character[5],
            "intelligence": character[6],
            "dexterity": character[7],
            "wisdom": character[8],
            'items': [character_items],
            'weapons': [character_weapons]
        }

        # insert character document
        db.insert_one(doc)


# function to show all documents in MongoDB
def show_all(db):
    # lists everything
    all_docs = list(db.find())
    return all_docs

# SQLite Queries

character_table = """
    SELECT *
    FROM charactercreator_character;
    """

armory_item_table = """
    SELECT *
    FROM charactercreator_character_inventory
    LEFT JOIN armory_item
    ON charactercreator_character_inventory.item_id=armory_item.item_id;
    """

armory_weapon_table = """
    SELECT *
    FROM armory_item
    INNER JOIN armory_weapon
    ON armory_item.item_id=armory_weapon.item_ptr_id;
    """

if __name__ == '__main__':
    sl_conn = sl_conn()
    sl_curs = sl_conn.cursor()
    client = mdb_conn()
    db = client.test.test
    db.drop({})
    character_creation(db, sl_curs, character_table)
    print(show_all(db))
