
import unittest
import sqlite3
import json
import os
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
all_years_data = {}

def get_yards_per_attempt(year):
    # URL to scrape
    url = f'https://www.sports-reference.com/cfb/schools/michigan/{year}/gamelog/'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    # Make the request
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table rows
    table = soup.find('table', attrs={'id': 'offense'})
    table_rows = table.find_all('tr') if table else []

    # Initialize a dictionary to hold the data
    yards_per_attempt = {}
    game_counter = 0
    # Loop through each row to get the data
    for row in table_rows:
        cells = row.find_all('td')
        if cells:
            date = cells[0].get_text()
            ### Skip rows that summarize the yearly average at the end of the season 
            if "Games" in date:
                continue
            pass_att = cells[5].get_text() # Adjust index as needed
            pass_yds = cells[7].get_text() # Adjust index as needed

            # Check if pass_att is a number and not zero to avoid division by zero
            if pass_att.replace('.', '', 1).isdigit() and int(float(pass_att)) != 0:
                y_a = round(float(pass_yds) / int(float(pass_att)), 2)
                all_years_data[date] = y_a
                game_counter += 1
        if game_counter == 12:
            break
    return all_years_data




# Loop through the years and get data
for year in range(2014, 2023):
    get_yards_per_attempt(year)


print(all_years_data)
print(len(all_years_data.keys()))