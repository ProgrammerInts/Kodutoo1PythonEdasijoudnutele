import csv
import sqlite3
from flask import Flask

app = Flask(__name__)

def get_db_connection():
    connection = sqlite3.connect('KOHVIKUD.db')
    return connection

def create_db_table():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        drop_table = "DROP TABLE IF EXISTS SOOKLA"

        create_table = """
        CREATE TABLE SOOKLA(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME TEXT NOT NULL,
        LOCATION TEXT NOT NULL,
        PROVIDER TEXT NOT NULL,
        time_open TEXT NOT NULL,
        time_closed TEXT NOT NULL);"""

        cursor.execute(drop_table)
        cursor.execute(create_table)
        conn.commit()
        print("DB KOHVIKUD ja tabel 'SOOKLA' loodud.")

    except sqlite3.Error as e:
        print(f"Tabeli loomine ebaõnnestus: {e}")

    finally:
        conn.close()

def insert_data_from_csv():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        csv_file = "Kohvikud.csv"

        with open(csv_file, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)

            for row in reader:
                name, location, provider, time_open, time_closed = row

                cursor.execute("""
                    INSERT INTO SOOKLA (NAME, LOCATION, PROVIDER, time_open, time_closed) 
                    VALUES (?, ?, ?, ?, ?)""", (name, location, provider, time_open, time_closed))

        conn.commit()
        print("CSV andmed lisatud tabelisse SOOKLA!")

    except sqlite3.Error as e:
        print(f"Viga andmete lisamisel: {e}")

    finally:
        conn.close()

if __name__ == '__main__':
    create_db_table()
    insert_data_from_csv()
