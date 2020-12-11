"""Holds my PostGreSQL example queries"""

#POSTGRESQL QUERIES
# SQL CREATE TABLE QUERY
CREATE_TABLE = """
    CREATE TABLE test_table (
        id SERIAL PRIMARY KEY, 
        name VARCHAR(40) NOT NULL,
        data JSONB
    );
"""

CREATE_CHARACTER_TABLE = 
#creates a a table called charactercreator_character
"""
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

# SQL INSERT VALUE QUERY
INSERT_STATEMENT = """
    INSERT INTO test_table(name, data) VALUES
    (
        'A Row',
        null
    ),
    (
        'Another Row, with Json',
        '{"a":1, "b": ["leaves", "more leaves", "even more leave"]}'::JSONB
    );
"""


#SQLITE QUERIES
GET_CHARACTERS = # selects all the rows from the charactercreator_character table
"""
    SELECT * FROM charactercreator_character;
"""

