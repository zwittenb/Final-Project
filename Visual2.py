import sqlite3
import matplotlib.pyplot as plt
import numpy as np
def connect_db(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    return cursor, conn

def calculate_temp_and_score(db_path, output_file):
    cursor, conn = connect_db(db_path)

    query = """
    SELECT 
        weather.temp, michigans_total_football_score.home_points
    FROM 
        weather
    INNER JOIN 
        michigans_total_football_score ON weather.id = michigans_total_football_score.id
    """

    cursor.execute(query)
    results = cursor.fetchall()

    # Initialize variables for calculation
    scores_25_35 = []
    scores_35_45 = []
    scores_45_55 = []
    scores_55_65 = []

    # Categorize scores based on temperature
    for temp, score in results:
        if 25 <= temp < 35:
            scores_25_35.append(score)
        elif 35 <= temp < 45:
            scores_35_45.append(score)
        elif 45 <= temp < 55:
            scores_45_55.append(score)
        elif 55 <= temp < 65:
            scores_55_65.append(score)

    # Calculate averages
    avg_scores_25_35 = sum(scores_25_35) / len(scores_25_35) if scores_25_35 else 0
    avg_scores_35_45 = sum(scores_35_45) / len(scores_35_45) if scores_35_45 else 0
    avg_scores_45_55 = sum(scores_45_55) / len(scores_45_55) if scores_25_35 else 0
    avg_scores_55_65 = sum(scores_55_65) / len(scores_55_65) if scores_35_45 else 0

    # Write results to the output file
    with open(output_file, 'w') as file:
        file.write(f"Average scores for 25-35 degrees: {avg_scores_25_35}\n")
        file.write(f"Average scores for 35-45 degrees: {avg_scores_35_45}\n")
        file.write(f"Average scores for 45-55 degrees: {avg_scores_45_55}\n")
        file.write(f"Average scores for 55-65 degrees: {avg_scores_55_65}\n")
    
    conn.close()

    return avg_scores_25_35, avg_scores_35_45, avg_scores_45_55, avg_scores_55_65

def create_bar_chart(avg_scores_25_35, avg_scores_35_45, avg_scores_45_55, avg_scores_55_65):
    categories = ['25-35°F', '35-45°F','45-55°F', '55-65°F']
    scores = [avg_scores_25_35, avg_scores_35_45, avg_scores_45_55, avg_scores_55_65]

    plt.figure(figsize=(8, 6))
    plt.bar(categories, scores, color=['blue', 'black', 'skyblue', 'yellow'])
    plt.xlabel('Temperature Ranges')
    plt.ylabel('Average Scores')
    plt.title('Average Football Scores by Temperature Range')
    plt.show()
def calculate_yards_per_attempt(db_path, output_file):
    cursor, conn = connect_db(db_path)

    # Modify this query based on your actual table and column names
    query = """
    SELECT 
        weather.temp, michigan_yards_per_attempt.yards_per_attempt
    FROM 
        weather
    INNER JOIN 
        michigan_yards_per_attempt ON weather.id = michigan_yards_per_attempt.id
    """

    cursor.execute(query)
    results = cursor.fetchall()

    # Initialize variables for calculation
    yards_25_35 = []
    yards_35_45 = []
    yards_45_55 = []
    yards_55_65 = []

    # Categorize yards per attempt based on temperature
    for temp, yards in results:
        if 25 <= temp < 35:
            yards_25_35.append(yards)
        elif 35 <= temp < 45:
            yards_35_45.append(yards)
        elif 45 <= temp < 55:
            yards_45_55.append(yards)
        elif 55 <= temp < 65:
            yards_55_65.append(yards)

    # Calculate averages
    avg_yards_25_35 = sum(yards_25_35) / len(yards_25_35) if yards_25_35 else 0
    avg_yards_35_45 = sum(yards_35_45) / len(yards_35_45) if yards_35_45 else 0
    avg_yards_45_55 = sum(yards_45_55) / len(yards_45_55) if yards_45_55 else 0
    avg_yards_55_65 = sum(yards_55_65) / len(yards_55_65) if yards_55_65 else 0


    return avg_yards_25_35, avg_yards_35_45, avg_yards_45_55, avg_yards_55_65

def create_bar_chart_for_yards(avg_yards_25_35, avg_yards_35_45, avg_yards_45_55, avg_yards_55_65):
    categories = ['25-35°F', '35-45°F', '45-55°F', '55-65°F']
    yards = [avg_yards_25_35, avg_yards_35_45, avg_yards_45_55, avg_yards_55_65]

    plt.figure(figsize=(8, 6))
    plt.bar(categories, yards, color=['blue', 'green', 'red', 'orange'])
    plt.xlabel('Temperature Ranges')
    plt.ylabel('Average Yards per Attempt')
    plt.title('Average Yards per Attempt by Temperature Range')
    plt.show()



def fetch_data_for_scatter_plot(db_path):
    cursor, conn = connect_db(db_path)

    # Modify this query to fetch Michigan's score and yards per attempt
    query = """
    SELECT 
        michigans_total_football_score.home_points + michigans_total_football_score.away_points AS total_points,
        michigan_yards_per_attempt.yards_per_attempt
    FROM 
        michigans_total_football_score
    INNER JOIN 
        michigan_yards_per_attempt ON michigans_total_football_score.id = michigan_yards_per_attempt.id
    """

    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()

    return results

def create_scatter_plot(data):
    total_scores = [item[0] for item in data]
    yards_per_attempt = [item[1] for item in data]

    plt.figure(figsize=(10, 6))
    plt.scatter(yards_per_attempt, total_scores, color='blue')

    # Adding a line of best fit
    m, b = np.polyfit(yards_per_attempt, total_scores, 1)
    plt.plot(yards_per_attempt, m*np.array(yards_per_attempt) + b, color='red')

    plt.xlabel('Yards per Attempt')
    plt.ylabel('Total Score')
    plt.title('Total Michigan Football Scores vs Yards per Attempt')
    plt.grid(True)
    plt.show()


def calculate_correlation(data):
    total_scores = [item[0] for item in data]
    yards_per_attempt = [item[1] for item in data]

    correlation_matrix = np.corrcoef(yards_per_attempt, total_scores)
    correlation_coefficient = correlation_matrix[0, 1]
    print(correlation_coefficient)
    return correlation_coefficient




def fetch_data_for_scatter_plot(db_path):
    cursor, conn = connect_db(db_path)

    query = """
    SELECT 
        michigans_total_football_score.home_points + michigans_total_football_score.away_points AS total_points,
        michigan_yards_per_attempt.yards_per_attempt
    FROM 
        michigans_total_football_score
    INNER JOIN 
        michigan_yards_per_attempt ON michigans_total_football_score.id = michigan_yards_per_attempt.id
    """

    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()

    return results

def group_data_by_season(data):
    season_data = {}
    season = 2014  # Start from the 2014 season
    games_per_season = 12
    game_count = 0

    for total_points, ya in data:
        if season > 2022:  # Stop at the 2022 season
            break

        if season not in season_data:
            season_data[season] = {'total_ya': 0, 'total_points': 0, 'games': 0}

        season_data[season]['total_ya'] += ya
        season_data[season]['total_points'] += total_points
        season_data[season]['games'] += 1

        game_count += 1
        # Adjust for the 2020 season
        if game_count == 6 and season == 2020:
            season += 1
            game_count = 0
        elif game_count == games_per_season:
            season += 1
            game_count = 0

    return season_data

def calculate_seasonal_averages(seasonal_data):
    seasonal_averages = {
        season: {
            'avg_ya': data['total_ya'] / data['games'],
            'avg_points_per_game': data['total_points'] / data['games']  # Average points per game
        }
        for season, data in seasonal_data.items()
    }

    return seasonal_averages

def create_seasonal_bar_charts(seasonal_averages):
    seasons = list(seasonal_averages.keys())
    avg_ya = [seasonal_averages[season]['avg_ya'] for season in seasons]
    avg_points_per_game = [seasonal_averages[season]['avg_points_per_game'] for season in seasons]

    # Bar chart for average yards per attempt
    plt.figure(figsize=(12, 6))
    plt.bar(seasons, avg_ya, color='brown')
    plt.xlabel('Season')
    plt.ylabel('Average Yards per Attempt')
    plt.title('Average Yards per Attempt per Season')
    plt.xticks(seasons)  # Ensure each season is labeled
    plt.show()

    # Bar chart for average total points per game
    plt.figure(figsize=(12, 6))
    plt.bar(seasons, avg_points_per_game, color='skyblue')
    plt.xlabel('Season')
    plt.ylabel('Average Total Points per Game')
    plt.title('Average Total Points per Game per Season')
    plt.xticks(seasons)  # Ensure each season is labeled
    plt.show()
if __name__ == "__main__":
    db_path = "final10.db"  # Replace with your actual database file path
    output_file = "avg_scores_by_temperature_range.txt"
    avg_scores_25_35, avg_scores_35_45, avg_scores_45_55, avg_scores_55_65 = calculate_temp_and_score(db_path, output_file)
    create_bar_chart(avg_scores_25_35, avg_scores_35_45, avg_scores_45_55, avg_scores_55_65)
    avg_yards_25_35, avg_yards_35_45, avg_yards_45_55, avg_yards_55_65 = calculate_yards_per_attempt(db_path, output_file)
    create_bar_chart_for_yards(avg_yards_25_35, avg_yards_35_45, avg_yards_45_55, avg_yards_55_65)
    data = fetch_data_for_scatter_plot(db_path)
    create_scatter_plot(data)
    game_data = fetch_data_for_scatter_plot(db_path)
    seasonal_data = group_data_by_season(game_data)
    seasonal_averages = calculate_seasonal_averages(seasonal_data)
    create_seasonal_bar_charts(seasonal_averages)
