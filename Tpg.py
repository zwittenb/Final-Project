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
            #print(game)
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
    



    cursor.execute("SELECT COUNT(*) FROM Teams")
    def create_cfbd_table(cursor,conn,data):
   
    # Create Teams table3
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Teams (
            cityID INTEGER PRIMARY KEY,
            name TEXT,
            wins INTEGER,
            losses INTEGER,
            elo INTEGER)
    ''')
    conn.commit()
   
    count_25 = 0
    cursor.execute("SELECT COUNT(*) FROM Teams")
    id = cursor.fetchone()[0]
    if id == 0:
        id = 1
    #print(id)
    while count_25 < 25 and id <= len(data):
        cfbd = data[(id)]
        cursor.execute('''
            INSERT OR IGNORE INTO Teams (cityID, name, wins, losses, elo)
            VALUES (?, ?, ?, ?, ?)
            ''', (id, cfbd["name"], cfbd["wins"], cfbd["losses"], cfbd["elo"]))
        id += 1
        count_25 += 1
    
    conn.commit()
    conn.close()

    def fetch_and_store_michigan_home_scores(api_key, cursor, conn):
    games_url = "https://api.collegefootballdata.com/games"
    headers = {"Authorization": f"Bearer {api_key}"}
    years = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
    total_data = {}
    for year in years:
        response = requests.get(games_url, params={"team": "Michigan", "year": year}, headers=headers)
        games_data_for_each_year = json.loads(response.text)
        for game in games_data_for_each_year:
            #print(game)
            total_data[game['id']] = game
    return total_data
def enter_other_team_and_score_2014_15(cur,conn, total_data):
     for game in total_data:
         if game['season'] == 2014:
             game_date = game["start_date"][0-10]
             cur.execute("SELECT date FROM all_data WHERE date=?", (game_date,))
             existing_date = cur.fetchone()
             if existing_date:
                 cur.execute("UPDATE all_data2 SET score=? WHERE date=?", (game["score"], game_date))