import pymongo

PASSWORD = "A2oU0l8VMXjYp2sh"
DBNAME = "rpg_db"

# create MongoDb connection
def mdb_conn(password=PASSWORD, dbname=DBNAME):
    # connect to a new database, since rpg_db does not exist on MongoDB
    client = pymongo.MongoClient(
        "mongodb+srv://WindowsOS-LopezJohn:{}@cluster00.3yt87.mongodb.net/{}?retryWrites=true&w=majority"
        .format(password, dbname)
        )
    return client

def assignment_queries(db, client):
    mb_curs = client.cursor()
    

if __name__ == '__main__':
    client = mdb_conn()
    db = client.test.test

# How many total Characters are there?
