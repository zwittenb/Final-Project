import requests
import sqlite3
import json
import os
from bs4 import BeautifulSoup



# Global variables for weather data
weather_url = "http://api.weatherstack.com/historical"
weather_access_key = "d2d987ae3fc3e98a513120c9c53d2504"




# Global variables for football scores
games_url = "https://api.collegefootballdata.com/games"
api_key = "zb9nGRo1d1bXtCQGHAsnLwMuJXfnhmMvRQukhexB2KSZpm/G5GQke21V/fQ4qGmq"




# Function definitions for weather data
def get_weather_data(url, access_key, query, date):
  params = {
      "access_key": access_key,
      "query": query,
      "historical_date": date,
  }
  response = requests.get(url, params=params)
  data = response.json()['historical'][date]['avgtemp']
  fahrenheit = (data * 1.8) + 32
  return round(fahrenheit, 2)
def get_team_data(url, access_key, team, dates):
  team_data = {}
  for date in dates:
      temperature = get_weather_data(url, access_key, team, date)
      team_data[date] = temperature
  return team_data




def clean_up_temp_data():
  teams = {
      "home": {
          "Ann Arbor": ["2014-08-30", "2014-09-13", "2014-09-20", "2014-09-27", "2014-10-11", "2014-11-01",
                        "2014-11-22",
                        "2015-09-12", "2015-09-19", "2015-09-26", "2015-10-10", "2015-10-17", "2015-11-07",
                        "2015-11-28", "2016-09-03", "2016-09-10", "2016-09-17", "2016-09-24", "2016-10-01",
                        "2016-10-22", "2016-11-05", "2016-11-19", "2017-09-09", "2017-09-16", "2017-10-07",
                        "2017-10-28", "2017-11-04", "2017-11-25", "2018-09-08", "2018-09-15", "2018-09-22",
                        "2018-10-06", "2018-10-13", "2018-11-03", "2018-11-17", "2019-08-31", "2019-09-07",
                        "2019-09-28", "2019-10-05", "2019-10-26", "2019-11-16", "2019-11-30", "2020-10-31",
                        "2020-11-14", "2020-11-28", "2021-09-04", "2021-09-11", "2021-09-18", "2021-09-25",
                        "2021-10-23", "2021-11-06", "2021-11-27", "2022-09-17", "2022-09-03", "2022-09-10",
                        "2022-09-24", "2022-10-15", "2022-10-29", "2022-11-12", "2022-11-19", "2023-09-02",
                        "2023-09-09", "2023-09-16", "2023-09-23", "2023-10-14", "2023-11-04", "2023-11-25"]
      },
      "away": {
          "South Bend": ["2014-09-06", "2018-09-01"],
          "New Jersey": ["2014-10-04", "2016-10-08", "2018-11-10", "2020-11-21", "2022-11-05"],
          "East Lansing": ["2014-10-25", "2016-10-29", "2018-10-20", "2021-10-30", "2023-10-21"],
          "Evanston": ["2014-11-08", "2018-09-29"],
          "Columbus": ["2014-11-29", "2016-11-26", "2018-11-24", "2022-11-26"],
          "College Park": ["2015-10-03", "2017-11-11", "2019-11-02", "2021-11-20", "2023-11-18"],
          "Salt Lake City": ["2015-09-03"],
          "Minneapolis": ["2015-10-31", "2020-10-24", "2023-10-07"],
          "Bloomington": ["2015-11-14", "2017-10-14", "2019-11-23", "2020-11-07", "2022-10-08"],
          "State College": ["2015-11-21", "2017-10-21", "2019-10-19", "2021-11-13", "2023-11-11"],
          "Iowa City": ["2016-11-12", "2022-10-01"],
          "Arlington": ["2017-09-02"],
          "East Lafayette": ["2017-09-23"],
          "Madison": ["2017-11-18", "2019-09-21", "2021-10-02"],
          "Champaign": ["2019-10-12"],
          "Lincoln": ["2021-10-09", "2023-09-30"]
      }
  }




  all_data = {}




  for team, locations in teams.items():
      for location, dates in locations.items():
          team_data = get_team_data(weather_url, weather_access_key, location, dates)
          all_data.update(team_data)




  # Sort the final result by date
  sorted_all_data = {date: all_data[date] for date in sorted(all_data.keys())}
  return sorted_all_data




# Function definitions for football scores
def fetch_and_store_michigan_home_scores(api_key, cursor, conn):
   games_url = "https://api.collegefootballdata.com/games"
   headers = {"Authorization": f"Bearer {api_key}"}
   years = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
   total_data = {}


    conn.commit()
    conn.close()

main()











    








  existing_rows += 25
  conn.commit()
def main():
    try:
        print("Current Working Directory:", os.getcwd())
        cursor, conn = create_database()
    
        # Process weather data
        sorted_all_data = clean_up_temp_data()
        create_weather_table(cursor, conn, sorted_all_data)
    
        # Process football scores
        football_data = fetch_and_store_michigan_home_scores(api_key, cursor, conn)
        create_football_scores_table(cursor, conn, football_data)
        
        create_dates_table(cursor, conn)
  
        all_years_data = {}
        for year in range(2014, 2023):
            year_data = get_yards_per_attempt(year)
            all_years_data.update(year_data)
     
        create_ya_table(cursor, conn, all_years_data)
    
        conn.close()
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()








import matplotlib.pyplot as plt
import sqlite3

def create_visualization(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    query = """
    SELECT 
        AVG(CASE WHEN temp >= 50 THEN yards_per_attempt ELSE NULL END) as avg_yards_above_50,
        AVG(CASE WHEN temp < 50 THEN yards_per_attempt ELSE NULL END) as avg_yards_below_50
    FROM 
        weather 
    INNER JOIN 
        michigan_yards_per_attempt 
    ON 
        weather.date = michigan_yards_per_attempt.date
    """

    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()

    avg_yards_above_50, avg_yards_below_50 = result

    # Visualization
    plt.bar(['Avg Yards (Temp >= 50°F)', 'Avg Yards (Temp < 50°F)'], [avg_yards_above_50, avg_yards_below_50])
    plt.ylabel('Average Yards Per Attempt')
    plt.title('Average Yards Per Attempt by Temperature')
    plt.show()

create_visualization("please4.db")
