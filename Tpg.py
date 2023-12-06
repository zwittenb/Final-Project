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
    
def create_table(cursor, conn):

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS michigan_total_scores (
            id INTEGER PRIMARY KEY,
            season INTEGER,
            week INTEGER,
            home_points INTEGER,
            away_points INTEGER,
            UNIQUE(season, week)
        )
    ''')
    conn.commit()

def fetch_data(total_data, conn, cursor):

    for game in total_data.values():
        if game['home_team'] == 'Michigan' and game['week'] > 0 and game['week'] < 15:
            
            cursor.execute('''
                INSERT OR IGNORE INTO michigan_total_scores (id, season, week, home_points)
                VALUES (?, ?, ?, ?)
            ''', (game['id'],game['season'], game['week'], game['home_points']))

        if game['away_team'] == 'Michigan' and game['week'] > 0 and game['week'] < 15:
            
            cursor.execute('''
                INSERT OR IGNORE INTO michigan_total_scores (id, season, week, away_points)
                VALUES (?, ?, ?, ?)
            ''', (game['id'],game['season'], game['week'], game['away_points']))

    conn.commit()
    

def main():   
    
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path + "/" + 'michigan_scores_database')
    cursor = conn.cursor()
    api_key = "zb9nGRo1d1bXtCQGHAsnLwMuJXfnhmMvRQukhexB2KSZpm/G5GQke21V/fQ4qGmq"
    data = fetch_and_store_michigan_home_scores(api_key,cursor, conn)
   
    create_table(cursor, conn)
    fetch_data(data,conn, cursor)
    conn.close()
         
if __name__ == "__main__":
    main()
    


