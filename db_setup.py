import csv
import sqlite3

DB_FILE = "KOHVIKUD.db"
CSV_FILE = "Kohvikud.csv"

def db_connect():
    return sqlite3.connect(DB_FILE)

def create_db_table():
    try:
        conn = db_connect()
        cursor = conn.cursor()

        cursor.execute("DROP TABLE IF EXISTS SOOKLA")

        cursor.execute("""
        CREATE TABLE SOOKLA(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NAME TEXT NOT NULL,
            LOCATION TEXT NOT NULL,
            PROVIDER TEXT NOT NULL,
            time_open TEXT NOT NULL,
            time_closed TEXT NOT NULL
        )""")

        conn.commit()
        print("Andmebaas ja tabel 'SOOKLA' loodud.")
    except sqlite3.Error as e:
        print(f"Tabeli loomine ebaõnnestus: {e}")
    finally:
        conn.close()

def insert_data_from_csv():
    try:
        conn = db_connect()
        cursor = conn.cursor()

        with open(CSV_FILE, mode="r", encoding="utf-8") as file:
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
