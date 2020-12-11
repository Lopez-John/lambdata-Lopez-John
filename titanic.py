import sqlite3
import pandas as pd

titanic = pd.read_csv('titanic.csv')
titanic['Name'] = titanic['Name'].replace("\'", " ", regex=True)
conn = sqlite3.connect('Titanic.sqlite3')
curs = conn.cursor()
curs.execute(""" CREATE TABLE titanic
    (
        id SERIAL PRIMARY KEY,
        Survived INT,
        Pclass INT,
        Name VARCHAR(90),
        Sex VARCHAR(10),
        AGE FLOAT,
        Siblings_Spouses_Aboard INT,
        Parents_Children_Aboard INT,
        Fare FLOAT
    );
    """)
conn.commit()
titanic.to_sql('titanic', conn, if_exists='replace', index=False)
curs.execute("""
    SELECT * FROM titanic;
    """)
conn.commit()
