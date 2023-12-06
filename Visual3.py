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
