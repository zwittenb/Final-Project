import sqlite3
import matplotlib.pyplot as plt
def calculate_and_write_data(db_path, output_file):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

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
    print(results)
    # Initialize variables for calculation
    yards_below_50 = []
    yards_above_50 = []

    # Categorize yards per attempt based on temperature
    for temp, yards in results:
        if temp < 30:
            yards_below_50.append(yards)
        else:
            yards_above_50.append(yards)

    # Calculate averages
    avg_yards_below_50 = sum(yards_below_50) / len(yards_below_50) if yards_below_50 else 0
    avg_yards_above_50 = sum(yards_above_50) / len(yards_above_50) if yards_above_50 else 0

    # Write to a file
    with open(output_file, 'w') as file:
        file.write(f"Average Yards Per Attempt (Temp < 50°F): {avg_yards_below_50:.2f}\n")
        file.write(f"Average Yards Per Attempt (Temp >= 50°F): {avg_yards_above_50:.2f}\n")

    conn.close()
    

# Replace 'your_database_path_here.db' with your actual database file path

if __name__ == "__main__":
    db_path = "please4.db"  # Replace with your actual database file path
    output_file = "avg_yards_by_temperature.txt"
    calculate_and_write_data(db_path, output_file)

