import unittest
import sqlite3
import json
import os
import matplotlib.pyplot as plt
import requests

def find_all_home_weather(cur, conn):
    lst = []
    home_dates = ["2014-08-30", "2014-09-13", "2014-09-20", "2014-09-27", "2014-10-11", "2014-11-01", "2014-11-22", "2014-09-13", "2014-09-20", "2015-09-12", "2015-09-19", "2015-09-26", "2015-10-10", "2015-10-17", "2015-11-07", "2015-11-28", "2016-09-03", "2016-10-10", "2016-10-17", "2016-09-24", "2016-10-01", "2016-10-22", "2016-11-05", "2016-11-19" ,"2017-11-09", "2017-09-16", "2017-10-07", "2017-10-28", "2017-11-04", "2017-11-25", "2018-09-08", "2018-09-15", "2018-09-22", "2018-10-06", "2018-09-04", "2018-11-13", "2018-11-03", "2018-11-17", "2019-10-31", "2019-09-07", "2019-09-28", "2019-10-05", "2019-10-26", "2019-11-16", "2019-11-30", "2020-11-14", "2020-11-28", "2021-09-04", "2021-09-11", "2021-09-18", "2021-09-25", "2021-10-23", "2021-11-06", "2021-11-27", "2022-09-03", "2022-09-10", "2022-09-17", "2022-09-24", "2022-10-15", "2022-10-29", "2022-11-12", "2022-11-10", "2023-09-02", "2023-09-09", "2023-09-16", "2023-09-23", "2023-10-14", "2023-11-04", "2023-11-25"]
    for date in home_dates:
        url = "http://api.weatherstack.com/historical"
        access_key = "d2d987ae3fc3e98a513120c9c53d2504"
        query = "Ann Arbor"
        params = {
            "access_key": access_key,
            "query": query,
            "historical_date": date,
        }
        response = requests.get(url, params=params)
        data = response.json()['historical'][date]['avgtemp']
        farenheit = (data * 1.8) + 32
    lst.append(farenheit)
    dic = {}
   for item in lst:
       dic[home_dates] = item
   print(dic)
   return dic
  
   def nd_away_games():
       nd_dates = ["2014-09-06", "2014-09-01"]
       for date in nd_dates:
           url = "http://api.weatherstack.com/historical"
           access_key = "d2d987ae3fc3e98a513120c9c53d2504"
           query = "South Bend"
           params = {
               "access_key": access_key,
               "query": query,
               "historical_date": date,
           }
           response = requests.get(url, params=params)
           data = response.json()['historical'][date]['avgtemp']
           farenheit = (data * 1.8) + 32
       lst.append(farenheit)
       dic = {}
       for item in lst:
           dic[nd_dates] = item
       return dic
  
   def rutgers_away_games():
       rutger_dates = ["2014-04-10", "2016-01-08", "2018-11-10", "2020-11-21", "2022-11-05"]
       for date in rutger_dates:
           url = "http://api.weatherstack.com/historical"
           access_key = "d2d987ae3fc3e98a513120c9c53d2504"
           query = "New Jersey"
           params = {
               "access_key": access_key,
               "query": query,
               "historical_date": date,
           }
           response = requests.get(url, params=params)
           data = response.json()['historical'][date]['avgtemp']
           farenheit = (data * 1.8) + 32
       lst.append(farenheit)
       dic = {}
       for item in lst:
           dic[rutger_dates] = item
       return dic
      
   def msu_away_games():
       msu_dates = ["2014-10-25", "2016-10-29", "2018-10-20", "2020-10-30", "2023-10-21"]
       for date in msu_dates:
           url = "http://api.weatherstack.com/historical"
           access_key = "d2d987ae3fc3e98a513120c9c53d2504"
           query = "East Lansing"
           params = {
               "access_key": access_key,
               "query": query,
               "historical_date": date,
           }
           response = requests.get(url, params=params)
           data = response.json()['historical'][date]['avgtemp']
           farenheit = (data * 1.8) + 32
       lst.append(farenheit)
       dic = {}
       for item in lst:
           dic[msu_dates] = item
       return dic
  
   def nw_away_games():
       nw_dates = ["2014-11-08", "2018-10-29"]
       for date in nw_dates:
           url = "http://api.weatherstack.com/historical"
           access_key = "d2d987ae3fc3e98a513120c9c53d2504"
           query = "Evanston"
           params = {
               "access_key": access_key,
               "query": query,
               "historical_date": date,
           }
           response = requests.get(url, params=params)
           data = response.json()['historical'][date]['avgtemp']
           farenheit = (data * 1.8) + 32
       lst.append(farenheit)
       dic = {}
       for item in lst:
           dic[nw_dates] = item
       return dic
  
   def osu_away_games():
       osu_dates = ["2014-11-29", "2016-11-26", "2018-11-24", "2022-11-26"]
       for date in osu_dates:
           url = "http://api.weatherstack.com/historical"
           access_key = "d2d987ae3fc3e98a513120c9c53d2504"
           query = "Columbus"
           params = {
               "access_key": access_key,
               "query": query,
               "historical_date": date,
           }
           response = requests.get(url, params=params)
           data = response.json()['historical'][date]['avgtemp']
           farenheit = (data * 1.8) + 32
       lst.append(farenheit)
       dic = {}
       for item in lst:
           dic[osu_dates] = item
       return dic
  
   def maryland_away_games():
       maryland_dates = ["2015-10-03", "2017-11-11", "2019-11-02", "2021-11-20", "2023-11-18"]
       for date in maryland_dates:
           url = "http://api.weatherstack.com/historical"
           access_key = "d2d987ae3fc3e98a513120c9c53d2504"
           query = "College Park"
           params = {
               "access_key": access_key,
               "query": query,
               "historical_date": date,
           }
           response = requests.get(url, params=params)
           data = response.json()['historical'][date]['avgtemp']
           farenheit = (data * 1.8) + 32
       lst.append(farenheit)
       dic = {}
       for item in lst:
           dic[maryland_dates] = item
       return dic
  
  
   def utah_away_games():
       utah_dates = ["2015-09-03"]
       for date in utah_dates:
           url = "http://api.weatherstack.com/historical"
           access_key = "d2d987ae3fc3e98a513120c9c53d2504"
           query = "Salt Lake City"
           params = {
               "access_key": access_key,
               "query": query,
               "historical_date": date,
           }
           response = requests.get(url, params=params)
           data = response.json()['historical'][date]['avgtemp']
           farenheit = (data * 1.8) + 32
       lst.append(farenheit)
       dic = {}
       for item in lst:
           dic[utah_dates] = item
       return dic
   def minnesota_away_games():
       minn_dates = ["2015-10-31", "2020-10-24", "2023-10-07"]
       for date in minn_dates:
           url = "http://api.weatherstack.com/historical"
           access_key = "d2d987ae3fc3e98a513120c9c53d2504"
           query = "Minneapolis"
           params = {
               "access_key": access_key,
               "query": query,
               "historical_date": date,
           }
           response = requests.get(url, params=params)
           data = response.json()['historical'][date]['avgtemp']
           farenheit = (data * 1.8) + 32
       lst.append(farenheit)
       dic = {}
       for item in lst:
           dic[minn_dates] = item
       return dic
  
  
   def indiana_away_game():
       indiana_dates = ["2015-11-14", "2017-10-14", "2019-11-23", "2020-11-07", "2022-10-08"]
       for date in indiana_dates:
           url = "http://api.weatherstack.com/historical"
           access_key = "d2d987ae3fc3e98a513120c9c53d2504"
           query = "Bloomington"
           params = {
               "access_key": access_key,
               "query": query,
               "historical_date": date,
           }
           response = requests.get(url, params=params)
           data = response.json()['historical'][date]['avgtemp']
           farenheit = (data * 1.8) + 32
       lst.append(farenheit)
       dic = {}
       for item in lst:
           dic[indiana_dates] = item
       return dic
  
  
   def psu_away_games():
       PSU_dates = ["2015-11-15", "2017-10-21", "2019-10-19", "2021-11-13", "2023-11-11"]
       for date in PSU_dates:
           url = "http://api.weatherstack.com/historical"
           access_key = "d2d987ae3fc3e98a513120c9c53d2504"
           query = "State College"
           params = {
               "access_key": access_key,
               "query": query,
               "historical_date": date,
           }
           response = requests.get(url, params=params)
           data = response.json()['historical'][date]['avgtemp']
           farenheit = (data * 1.8) + 32
       lst.append(farenheit)
       dic = {}
       for item in lst:
           dic[PSU_dates] = item
       return dic
  
   def iowa_away_games():
       iowa_dates = ["2016-11-12", "2020-10-01"]
       for date in iowa_dates:
           url = "http://api.weatherstack.com/historical"
           access_key = "d2d987ae3fc3e98a513120c9c53d2504"
           query = "Iowa City"
           params = {
               "access_key": access_key,
               "query": query,
               "historical_date": date,
           }
           response = requests.get(url, params=params)
           data = response.json()['historical'][date]['avgtemp']
           farenheit = (data * 1.8) + 32
  
   def purdue_away_games():
       purdue_dates = ["2017-09-23"]
       for date in purdue_dates:
           url = "http://api.weatherstack.com/historical"
           access_key = "d2d987ae3fc3e98a513120c9c53d2504"
           query = "East Lafayette"
           params = {
               "access_key": access_key,
               "query": query,
               "historical_date": date,
           }
           response = requests.get(url, params=params)
           data = response.json()['historical'][date]['avgtemp']
           farenheit = (data * 1.8) + 32
       lst.append(farenheit)
       dic = {}
       for item in lst:
           dic[purdue_dates] = item
       return dic
  
   def wisco_away_games():  
       wisco_dates = ["2017-11-18", "2019-09-21", "2021-10-02"]
       for date in wisco_dates:
           url = "http://api.weatherstack.com/historical"
           access_key = "d2d987ae3fc3e98a513120c9c53d2504"
           query = "Madison"
           params = {
               "access_key": access_key,
               "query": query,
               "historical_date": date,
           }
           response = requests.get(url, params=params)
           data = response.json()['historical'][date]['avgtemp']
           farenheit = (data * 1.8) + 32
  
   def illinois_away_games():
       illinois_dates = ["2019-10-12"]
       for date in illinois_dates:
           url = "http://api.weatherstack.com/historical"
           access_key = "d2d987ae3fc3e98a513120c9c53d2504"
           query = "Champiagne"
           params = {
               "access_key": access_key,
               "query": query,
               "historical_date": date,
           }
           response = requests.get(url, params=params)
           data = response.json()['historical'][date]['avgtemp']
           farenheit = (data * 1.8) + 32
       lst.append(farenheit)
       dic = {}
       for item in lst:
           dic[illinois_dates] = item
       return dic
  
   def nebraska_away_games():
  
       neb_dates = ["2021-10-09", "2023-09-30"]
       for date in neb_dates:
           url = "http://api.weatherstack.com/historical"
           access_key = "d2d987ae3fc3e98a513120c9c53d2504"
           query = "Lincoln"
           params = {
               "access_key": access_key,
               "query": query,
               "historical_date": date,
           }
           response = requests.get(url, params=params)
           data = response.json()['historical'][date]['avgtemp']
           farenheit = (data * 1.8) + 32


       lst.append(farenheit)
       dic = {}
       for item in lst:
           dic[neb_dates] = item
       return dic









