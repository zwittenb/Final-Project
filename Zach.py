import unittest
import sqlite3
import json
import os
import matplotlib.pyplot as plt
import requests
def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn
def create_oppnents_table(cur, conn):
    opposing_team_list = [""]
    cur.execute(
            "CREATE TABLE IF NOT EXISTS all_data (id INTEGER PRIMARY KEY temperature INTEGER, Opponent TEXT)"
        )
def set_up_all_data_table(cur, conn):
    date_list = ["2021-10-09", "2023-09-30", "2019-10-12", "2017-11-18", "2019-09-21", "2021-10-02", "2017-09-23", "2017-09-02", "2016-11-12", "2022-10-01", "2015-11-21", "2017-10-21", "2019-10-19", "2021-11-13", "2023-11-11", "2015-11-14", "2017-10-14", "2019-11-23", "2020-11-07", "2022-10-08", "2015-10-31", "2020-10-24", "2023-10-07", "2015-09-03", "2015-10-03", "2017-11-11", "2019-11-02", "2021-11-20", "2023-11-18", "2014-11-29", "2016-11-26", "2018-11-24", "2022-11-26", "2014-11-08", "2018-09-29", "2014-10-25", "2016-10-29", "2018-10-20", "2021-10-30", "2023-10-21", "2014-10-04", "2016-10-08", "2018-11-10", "2020-11-21", "2022-11-05", "2014-09-06", "2018-09-01", "2014-08-30", "2014-09-13", "2014-09-20", "2014-09-27", "2014-10-11", "2014-11-01", "2014-11-22", "2015-09-12", "2015-09-19", "2015-09-26", "2015-10-10", "2015-10-17", "2015-11-07", "2015-11-28", "2016-09-03", "2016-09-10", "2016-09-17", "2016-09-24", "2016-10-01", "2016-10-22", "2016-11-05", "2016-11-19", "2017-09-09", "2017-09-16", "2017-10-07", "2017-10-28", "2017-11-04", "2017-11-25", "2018-09-08", "2018-09-15", "2018-09-22", "2018-10-06", "2018-10-13", "2018-11-03", "2018-11-17", "2019-08-31", "2019-09-07", "2019-09-28", "2019-10-05", "2019-10-26", "2019-11-16", "2019-11-30", "2020-10-31", "2020-11-14", "2020-11-28", "2021-09-04", "2021-09-11", "2021-09-18", "2021-09-25", "2021-10-23", "2021-11-06", "2021-11-27", "2022-09-17", "2022-09-03", "2022-09-10", "2022-09-24", "2022-10-15", "2022-10-29", "2022-11-12", "2022-11-19", "2023-09-02", "2023-09-09", "2023-09-16", "2023-09-23", "2023-10-14", "2023-11-04", "2023-11-25"]
    date_list2 = sorted(date_list)
    cur.execute(
            "CREATE TABLE IF NOT EXISTS all_data (id INTEGER PRIMARY KEY, date TEXT UNIQUE, temperature INTEGER, scoring INTEGER, ya INTEGER, Opponent TEXT)"
        )
    for date_id, date_value in enumerate(date_list2, start=1):
        cur.execute(
            "INSERT OR IGNORE INTO all_data (id, date) VALUES (?, ?)",
            (date_id, date_value)
        )
    conn.commit()
url = "http://api.weatherstack.com/historical"
access_key = "d2d987ae3fc3e98a513120c9c53d2504"
def find_all_home_weather(url,access_key, cur, conn):
   home_dates = ["2014-08-30", "2014-09-13", "2014-09-20", "2014-09-27", "2014-10-11", "2014-11-01", "2014-11-22", "2015-09-12", "2015-09-19", "2015-09-26", "2015-10-10", "2015-10-17", "2015-11-07", "2015-11-28", "2016-09-03", "2016-09-10", "2016-09-17", "2016-09-24", "2016-10-01", "2016-10-22", "2016-11-05", "2016-11-19", "2017-09-09", "2017-09-16",]
   dic = {}
   for date in home_dates:
       url = "http://api.weatherstack.com/historical"
       access_key = "d2d987ae3fc3e98a513120c9c53d2504"
       query = "Ann Arbor"
       params = {"access_key": access_key, "query": query, "historical_date": date,}
       response = requests.get(url, params=params)
       data = response.json()['historical'][date]['avgtemp']
       farenheit = (data * 1.8) + 32
       real_farenheit = round(farenheit, 2)
       cur.execute("SELECT date FROM all_data WHERE date=?", (date,))
       existing_date = cur.fetchone()
       if existing_date:
            # Update the existing row
            cur.execute("UPDATE all_data SET temperature=? WHERE date=?", (real_farenheit, date))
       else:
            # Insert a new row
            cur.execute("INSERT INTO all_data (date, temperature) VALUES (?, ?)", (date, real_farenheit))
def find_all_home_weather2(url,access_key, cur, conn):
   home_dates = ["2017-10-07", "2017-10-28", "2017-11-04", "2017-11-25", "2018-09-08", "2018-09-15", "2018-09-22", "2018-10-06", "2018-10-13", "2018-11-03", "2018-11-17", "2019-08-31", "2019-09-07", "2019-09-28", "2019-10-05", "2019-10-26", "2019-11-16", "2019-11-30", "2020-10-31", "2020-11-14", "2020-11-28", "2021-09-04", "2021-09-11", "2021-09-18"]
   dic = {}
   for date in home_dates:
       url = "http://api.weatherstack.com/historical"
       access_key = "d2d987ae3fc3e98a513120c9c53d2504"
       query = "Ann Arbor"
       params = {"access_key": access_key, "query": query, "historical_date": date,}
       response = requests.get(url, params=params)
       data = response.json()['historical'][date]['avgtemp']
       farenheit = (data * 1.8) + 32
       real_farenheit = round(farenheit, 2)
       cur.execute("SELECT date FROM all_data WHERE date=?", (date,))
       existing_date = cur.fetchone()
       if existing_date:
            # Update the existing row
            cur.execute("UPDATE all_data SET temperature=? WHERE date=?", (real_farenheit, date))
       else:
            # Insert a new row
            cur.execute("INSERT INTO all_data (date, temperature) VALUES (?, ?)", (date, real_farenheit))
def find_all_home_weather3(url,access_key, cur, conn):
   home_dates = ["2021-09-25", "2021-10-23", "2021-11-06", "2021-11-27", "2022-09-17", "2022-09-03", "2022-09-10", "2022-09-24", "2022-10-15", "2022-10-29", "2022-11-12", "2022-11-19", "2023-09-02", "2023-09-09", "2023-09-16", "2023-09-23", "2023-10-14", "2023-11-04", "2023-11-25"]
   dic = {}
   for date in home_dates:
       url = "http://api.weatherstack.com/historical"
       access_key = "d2d987ae3fc3e98a513120c9c53d2504"
       query = "Ann Arbor"
       params = {"access_key": access_key, "query": query, "historical_date": date,}
       response = requests.get(url, params=params)
       data = response.json()['historical'][date]['avgtemp']
       farenheit = (data * 1.8) + 32
       real_farenheit = round(farenheit, 2)
       cur.execute("SELECT date FROM all_data WHERE date=?", (date,))
       existing_date = cur.fetchone()
       if existing_date:
            # Update the existing row
            cur.execute("UPDATE all_data SET temperature=? WHERE date=?", (real_farenheit, date))
       else:
            # Insert a new row
            cur.execute("INSERT INTO all_data (date, temperature) VALUES (?, ?)", (date, real_farenheit))
def nd_away_games(url,access_key, cur, conn):
  dic = {}
  nd_dates = ["2014-09-06", "2018-09-01"]
  for date in nd_dates:
       url = "http://api.weatherstack.com/historical"
       access_key = "d2d987ae3fc3e98a513120c9c53d2504"
       query = "South Bend"
       params = {"access_key": access_key, "query": query, "historical_date": date,}
       response = requests.get(url, params=params)
       data = response.json()['historical'][date]['avgtemp']
       farenheit = (data * 1.8) + 32
       real_farenheit = round(farenheit, 2)
       cur.execute("SELECT date FROM all_data WHERE date=?", (date,))
       existing_date = cur.fetchone()
       if existing_date:
            # Update the existing row
            cur.execute("UPDATE all_data SET temperature=? WHERE date=?", (real_farenheit, date))
       else:
            # Insert a new row
            cur.execute("INSERT INTO all_data (date, temperature) VALUES (?, ?)", (date, real_farenheit))
def rutgers_away_games(url,access_key, cur, conn):
   dic = {}
   rutger_dates = ["2014-10-04", "2016-10-08", "2018-11-10", "2020-11-21", "2022-11-05"]
   for date in rutger_dates:
       url = "http://api.weatherstack.com/historical"
       access_key = "d2d987ae3fc3e98a513120c9c53d2504"
       query = "New Jersey"
       params = {"access_key": access_key, "query": query, "historical_date": date,}
       response = requests.get(url, params=params)
       data = response.json()['historical'][date]['avgtemp']
       farenheit = (data * 1.8) + 32
       real_farenheit = round(farenheit, 2)
       dic[date] = real_farenheit
       cur.execute("SELECT date FROM all_data WHERE date=?", (date,))
       existing_date = cur.fetchone()
       if existing_date:
            # Update the existing row
            cur.execute("UPDATE all_data SET temperature=? WHERE date=?", (real_farenheit, date))
       else:
            # Insert a new row
            cur.execute("INSERT INTO all_data (date, temperature) VALUES (?, ?)", (date, real_farenheit))
def msu_away_games(url,access_key, cur, conn):
   dic = {}
   msu_dates = ["2014-10-25", "2016-10-29", "2018-10-20", "2021-10-30", "2023-10-21"]
   for date in msu_dates:
       url = "http://api.weatherstack.com/historical"
       access_key = "d2d987ae3fc3e98a513120c9c53d2504"
       query = "East Lansing"
       params = {"access_key": access_key, "query": query, "historical_date": date,}
       response = requests.get(url, params=params)
       data = response.json()['historical'][date]['avgtemp']
       farenheit = (data * 1.8) + 32
       real_farenheit = round(farenheit, 2)
       cur.execute("SELECT date FROM all_data WHERE date=?", (date,))
       existing_date = cur.fetchone()
       if existing_date:
            # Update the existing row
            cur.execute("UPDATE all_data SET temperature=? WHERE date=?", (real_farenheit, date))
       else:
            # Insert a new row
            cur.execute("INSERT INTO all_data (date, temperature) VALUES (?, ?)", (date, real_farenheit))
def nw_away_games(url,access_key, cur, conn):
   dic = {}
   nw_dates = ["2014-11-08", "2018-09-29"]
   for date in nw_dates:
       url = "http://api.weatherstack.com/historical"
       access_key = "d2d987ae3fc3e98a513120c9c53d2504"
       query = "Evanston"
       params = {"access_key": access_key, "query": query, "historical_date": date,}
       response = requests.get(url, params=params)
       data = response.json()['historical'][date]['avgtemp']
       farenheit = (data * 1.8) + 32
       real_farenheit = round(farenheit, 2)
       dic[date] = real_farenheit
       cur.execute("SELECT date FROM all_data WHERE date=?", (date,))
       existing_date = cur.fetchone()
       if existing_date:
            # Update the existing row
            cur.execute("UPDATE all_data SET temperature=? WHERE date=?", (real_farenheit, date))
       else:
            # Insert a new row
            cur.execute("INSERT INTO all_data (date, temperature) VALUES (?, ?)", (date, real_farenheit))
def osu_away_games(url,access_key, cur, conn):
   osu_dates = ["2014-11-29", "2016-11-26", "2018-11-24", "2022-11-26"]
   dic = {}
   for date in osu_dates:
       url = "http://api.weatherstack.com/historical"
       access_key = "d2d987ae3fc3e98a513120c9c53d2504"
       query = "Columbus"
       params = {"access_key": access_key, "query": query, "historical_date": date,}
       response = requests.get(url, params=params)
       data = response.json()['historical'][date]['avgtemp']
       farenheit = (data * 1.8) + 32
       real_farenheit = round(farenheit, 2)
       dic[date] = real_farenheit
       cur.execute("SELECT date FROM all_data WHERE date=?", (date,))
       existing_date = cur.fetchone()
       if existing_date:
            # Update the existing row
            cur.execute("UPDATE all_data SET temperature=? WHERE date=?", (real_farenheit, date))
       else:
            # Insert a new row
            cur.execute("INSERT INTO all_data (date, temperature) VALUES (?, ?)", (date, real_farenheit))
def maryland_away_games(url,access_key, cur, conn):
   dic = {}
   maryland_dates = ["2015-10-03", "2017-11-11", "2019-11-02", "2021-11-20", "2023-11-18"]
   for date in maryland_dates:
       url = "http://api.weatherstack.com/historical"
       access_key = "d2d987ae3fc3e98a513120c9c53d2504"
       query = "College Park"
       params = {"access_key": access_key, "query": query, "historical_date": date,}
       response = requests.get(url, params=params)
       data = response.json()['historical'][date]['avgtemp']
       farenheit = (data * 1.8) + 32
       real_farenheit = round(farenheit, 2)
       cur.execute("SELECT date FROM all_data WHERE date=?", (date,))
       existing_date = cur.fetchone()
       if existing_date:
            # Update the existing row
            cur.execute("UPDATE all_data SET temperature=? WHERE date=?", (real_farenheit, date))
       else:
            # Insert a new row
            cur.execute("INSERT INTO all_data (date, temperature) VALUES (?, ?)", (date, real_farenheit))
def utah_away_games(url,access_key, cur, conn):
   dic = {}
   utah_dates = ["2015-09-03"]
   for date in utah_dates:
       url = "http://api.weatherstack.com/historical"
       access_key = "d2d987ae3fc3e98a513120c9c53d2504"
       query = "Salt Lake City"
       params = {"access_key": access_key, "query": query, "historical_date": date,}
       response = requests.get(url, params=params)
       data = response.json()['historical'][date]['avgtemp']
       farenheit = (data * 1.8) + 32
       real_farenheit = round(farenheit, 2)
       cur.execute("SELECT date FROM all_data WHERE date=?", (date,))
       existing_date = cur.fetchone()
       if existing_date:
            # Update the existing row
            cur.execute("UPDATE all_data SET temperature=? WHERE date=?", (real_farenheit, date))
       else:
            # Insert a new row
            cur.execute("INSERT INTO all_data (date, temperature) VALUES (?, ?)", (date, real_farenheit))
def minnesota_away_games(url,access_key, cur, conn):
   dic = {}
   minn_dates = ["2015-10-31", "2020-10-24", "2023-10-07"]
   for date in minn_dates:
       url = "http://api.weatherstack.com/historical"
       access_key = "d2d987ae3fc3e98a513120c9c53d2504"
       query = "Minneapolis"
       params = {"access_key": access_key, "query": query, "historical_date": date,}
       response = requests.get(url, params=params)
       data = response.json()['historical'][date]['avgtemp']
       farenheit = (data * 1.8) + 32
       real_farenheit = round(farenheit, 2)
       cur.execute("SELECT date FROM all_data WHERE date=?", (date,))
       existing_date = cur.fetchone()
       if existing_date:
            # Update the existing row
            cur.execute("UPDATE all_data SET temperature=? WHERE date=?", (real_farenheit, date))
       else:
            # Insert a new row
            cur.execute("INSERT INTO all_data (date, temperature) VALUES (?, ?)", (date, real_farenheit))
def indiana_away_game(url,access_key, cur, conn):
   dic = {}
   indiana_dates = ["2015-11-14", "2017-10-14", "2019-11-23", "2020-11-07", "2022-10-08"]
   for date in indiana_dates:
       url = "http://api.weatherstack.com/historical"
       access_key = "d2d987ae3fc3e98a513120c9c53d2504"
       query = "Bloomington"
       params = {"access_key": access_key, "query": query, "historical_date": date,}
       response = requests.get(url, params=params)
       data = response.json()['historical'][date]['avgtemp']
       farenheit = (data * 1.8) + 32
       real_farenheit = round(farenheit, 2)
       dic[date] = real_farenheit
       cur.execute("SELECT date FROM all_data WHERE date=?", (date,))
       existing_date = cur.fetchone()
       if existing_date:
            # Update the existing row
            cur.execute("UPDATE all_data SET temperature=? WHERE date=?", (real_farenheit, date))
       else:
            # Insert a new row
            cur.execute("INSERT INTO all_data (date, temperature) VALUES (?, ?)", (date, real_farenheit))
def psu_away_games(url,access_key, cur, conn):
   dic = {}
   psu_dates = ["2015-11-21", "2017-10-21", "2019-10-19", "2021-11-13", "2023-11-11"]
   for date in psu_dates:
       url = "http://api.weatherstack.com/historical"
       access_key = "d2d987ae3fc3e98a513120c9c53d2504"
       query = "State College"
       params = {"access_key": access_key, "query": query, "historical_date": date,}
       response = requests.get(url, params=params)
       data = response.json()['historical'][date]['avgtemp']
       farenheit = (data * 1.8) + 32
       real_farenheit = round(farenheit, 2)
       cur.execute("SELECT date FROM all_data WHERE date=?", (date,))
       existing_date = cur.fetchone()
       if existing_date:
            # Update the existing row
            cur.execute("UPDATE all_data SET temperature=? WHERE date=?", (real_farenheit, date))
       else:
            # Insert a new row
            cur.execute("INSERT INTO all_data (date, temperature) VALUES (?, ?)", (date, real_farenheit))
def iowa_away_games(url,access_key, cur, conn):
   dic = {}
   iowa_dates = ["2016-11-12", "2022-10-01"]
   for date in iowa_dates:
       url = "http://api.weatherstack.com/historical"
       access_key = "d2d987ae3fc3e98a513120c9c53d2504"
       query = "Iowa City"
       params = {"access_key": access_key, "query": query, "historical_date": date,}
       response = requests.get(url, params=params)
       data = response.json()['historical'][date]['avgtemp']
       farenheit = (data * 1.8) + 32
       real_farenheit = round(farenheit, 2)
       cur.execute("SELECT date FROM all_data WHERE date=?", (date,))
       existing_date = cur.fetchone()
       if existing_date:
            # Update the existing row
            cur.execute("UPDATE all_data SET temperature=? WHERE date=?", (real_farenheit, date))
       else:
            # Insert a new row
            cur.execute("INSERT INTO all_data (date, temperature) VALUES (?, ?)", (date, real_farenheit))
def neutral_away_games(url,access_key, cur, conn):
   dic = {}
   neutral_dates = ["2017-09-02"]
   for date in neutral_dates:
       url = "http://api.weatherstack.com/historical"
       access_key = "d2d987ae3fc3e98a513120c9c53d2504"
       query = "Arlington"
       params = {"access_key": access_key, "query": query, "historical_date": date,}
       response = requests.get(url, params=params)
       data = response.json()['historical'][date]['avgtemp']
       farenheit = (data * 1.8) + 32
       real_farenheit = round(farenheit, 2)
       cur.execute("SELECT date FROM all_data WHERE date=?", (date,))
       existing_date = cur.fetchone()
       if existing_date:
            # Update the existing row
            cur.execute("UPDATE all_data SET temperature=? WHERE date=?", (real_farenheit, date))
       else:
            # Insert a new row
            cur.execute("INSERT INTO all_data (date, temperature) VALUES (?, ?)", (date, real_farenheit))
def purdue_away_games(url,access_key, cur, conn):
   dic = {}
   purdue_dates = ["2017-09-23"]
   for date in purdue_dates:
       url = "http://api.weatherstack.com/historical"
       access_key = "d2d987ae3fc3e98a513120c9c53d2504"
       query = "East Lafayette"
       params = {"access_key": access_key, "query": query, "historical_date": date,}
       response = requests.get(url, params=params)
       data = response.json()['historical'][date]['avgtemp']
       farenheit = (data * 1.8) + 32
       real_farenheit = round(farenheit, 2)
       cur.execute("SELECT date FROM all_data WHERE date=?", (date,))
       existing_date = cur.fetchone()
       if existing_date:
            # Update the existing row
            cur.execute("UPDATE all_data SET temperature=? WHERE date=?", (real_farenheit, date))
       else:
            # Insert a new row
            cur.execute("INSERT INTO all_data (date, temperature) VALUES (?, ?)", (date, real_farenheit))
def wisco_away_games(url,access_key, cur, conn):
   dic = {}
   wisco_dates = ["2017-11-18", "2019-09-21", "2021-10-02"]
   for date in wisco_dates:
       url = "http://api.weatherstack.com/historical"
       access_key = "d2d987ae3fc3e98a513120c9c53d2504"
       query = "Madison"
       params = {"access_key": access_key, "query": query, "historical_date": date,}
       response = requests.get(url, params=params)
       data = response.json()['historical'][date]['avgtemp']
       farenheit = (data * 1.8) + 32
       real_farenheit = round(farenheit, 2)
       cur.execute("SELECT date FROM all_data WHERE date=?", (date,))
       existing_date = cur.fetchone()
       if existing_date:
            # Update the existing row
            cur.execute("UPDATE all_data SET temperature=? WHERE date=?", (real_farenheit, date))
       else:
            # Insert a new row
            cur.execute("INSERT INTO all_data (date, temperature) VALUES (?, ?)", (date, real_farenheit))
def illinois_away_games(url,access_key, cur, conn):
   dic = {}
   illinois_dates = ["2019-10-12"]
   for date in illinois_dates:
       url = "http://api.weatherstack.com/historical"
       access_key = "d2d987ae3fc3e98a513120c9c53d2504"
       query = "Champaign"
       params = {"access_key": access_key, "query": query, "historical_date": date,}
       response = requests.get(url, params=params)
       data = response.json()['historical'][date]['avgtemp']
       farenheit = (data * 1.8) + 32
       real_farenheit = round(farenheit, 2)
       cur.execute("SELECT date FROM all_data WHERE date=?", (date,))
       existing_date = cur.fetchone()
       if existing_date:
            # Update the existing row
            cur.execute("UPDATE all_data SET temperature=? WHERE date=?", (real_farenheit, date))
       else:
            # Insert a new row
            cur.execute("INSERT INTO all_data (date, temperature) VALUES (?, ?)", (date, real_farenheit))
def nebraska_away_games(url,access_key, cur, conn):
   dic = {}
   neb_dates = ["2021-10-09", "2023-09-30"]
   for date in neb_dates:
       url = "http://api.weatherstack.com/historical"
       access_key = "d2d987ae3fc3e98a513120c9c53d2504"
       query = "Lincoln"
       params = {"access_key": access_key, "query": query, "historical_date": date,}
       response = requests.get(url, params=params)
       data = response.json()['historical'][date]['avgtemp']
       farenheit = (data * 1.8) + 32
       real_farenheit = round(farenheit, 2)
       cur.execute("SELECT date FROM all_data WHERE date=?", (date,))
       existing_date = cur.fetchone()
       if existing_date:
            # Update the existing row
            cur.execute("UPDATE all_data SET temperature=? WHERE date=?", (real_farenheit, date))
       else:
            # Insert a new row
            cur.execute("INSERT INTO all_data (date, temperature) VALUES (?, ?)", (date, real_farenheit))
def main():
    cur, conn = setUpDatabase('Final_Project.db')
    set_up_all_data_table(cur,conn)
    find_all_home_weather(url, access_key, cur, conn)
    find_all_home_weather2(access_key, url, cur, conn)
    find_all_home_weather3(access_key, url, cur, conn)
    nd_away_games(access_key, url, cur, conn)
    rutgers_away_games(access_key, url, cur, conn)
    msu_away_games(access_key, url, cur, conn)
    nw_away_games(access_key, url, cur, conn)
    osu_away_games(access_key, url, cur, conn)
    maryland_away_games(access_key, url, cur, conn)
    utah_away_games(access_key, url, cur, conn)
    minnesota_away_games(access_key, url, cur, conn)
    indiana_away_game(access_key, url, cur, conn)
    psu_away_games(access_key, url, cur, conn)
    iowa_away_games(access_key, url, cur, conn)
    neutral_away_games(access_key, url, cur, conn)
    purdue_away_games(access_key, url, cur, conn)
    wisco_away_games(access_key, url, cur, conn)
    illinois_away_games(access_key, url, cur, conn)
    nebraska_away_games(access_key, url, cur, conn)


    conn.commit()
    conn.close()

main()











    








