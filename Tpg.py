import requests
import sqlite3
import json
import os


def fetch_and_store_michigan_home_scores(api_key, cursor, conn):
    games_url = "https://api.collegefootballdata.com/games"
    headers = {"Authorization": f"Bearer {api_key}"}
    years = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
    total_data = {}

    for year in years:
        response = requests.get(games_url, params={"team": "Michigan", "year": year}, headers=headers)
        games_data_for_each_year = json.loads(response.text)
        for game in games_data_for_each_year:
            total_data[game['id']] = game
    return total_data


def create_table(cursor, conn, total_data):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS test_table(
            id INTEGER PRIMARY KEY,
            points INTEGER
        )
    ''')
    conn.commit()
    cursor.execute("SELECT COUNT(*) FROM test_table")
    existing_rows = cursor.fetchone()[0]
    counter = 0
    for key, value in total_data.items():
        counter += 1
        if counter >= existing_rows and counter <= existing_rows + 25:
            game = total_data[key]
            
            if game.get('home_team') == 'Michigan':
                cursor.execute('''
                    INSERT OR IGNORE INTO test_table (points)
                    VALUES (?)
                ''', (game.get('home_points', None),))
                conn.commit()
            if game.get('away_team') == 'Michigan':
                cursor.execute('''
                    INSERT OR IGNORE INTO test_table (points)
                    VALUES (?)
                ''', (game.get("away_points", None),))
                conn.commit()
    existing_rows += 25
    
    conn.commit()
                

def main():   
    
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path + "/" + 'michigan_scores_database')
    cursor = conn.cursor()
    api_key = "zb9nGRo1d1bXtCQGHAsnLwMuJXfnhmMvRQukhexB2KSZpm/G5GQke21V/fQ4qGmq"
    data = fetch_and_store_michigan_home_scores(api_key,cursor, conn)
    create_table(cursor, conn, data)
    
    conn.close()
         
if __name__ == "__main__":
    main()
    


