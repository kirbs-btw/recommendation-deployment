import sqlite3
import pandas as pd

def main():
    # params
    CSV_PATH = "setup/data/songs.csv"
    DB_PATH = "db/db.db"

    # loading from the csv
    df = pd.read_csv(CSV_PATH)

    # creating the sqlite file
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # creating table in the db
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS songs (
            track_and_artist TEXT PRIMARY KEY,
            trackname TEXT,
            artistname TEXT
        )
    ''')
    
    # inserting data into db
    for _, row in df.iterrows():
        cursor.execute('''
            INSERT OR IGNORE INTO songs (track_and_artist, trackname, artistname) 
            VALUES (?, ?, ?)
        ''', (row['track_and_artist'], row['trackname'], row['artistname']))
    
    # creating an index for the data i guess
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_artistname ON songs(artistname)')

    conn.commit()
    conn.close()
    print("---FINISHED---")
    
if __name__ == '__main__':
    main()