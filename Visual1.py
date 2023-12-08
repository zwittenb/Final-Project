import sqlite3
import datetime

def get_day_of_week(date_str):
    return datetime.datetime.strptime(date_str, "%Y-%m-%d").strftime("%A")

def calculate_and_write_data(db_path, output_file):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    query = """
    SELECT 
        d.date, ya.yards_per_attempt
    FROM 
        dates d
    INNER JOIN 
        michigan_yards_per_attempt ya ON d.date = ya.date
    """

    cursor.execute(query)
    results = cursor.fetchall()

    # Calculate average yards per day of the week
    day_yards = {day: [] for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]}
    for date_str, yards in results:
        day = get_day_of_week(date_str)
        day_yards[day].append(yards)

    avg_yards_per_day = {day: sum(yards) / len(yards) if yards else 0 for day, yards in day_yards.items()}

    # Write to a file
    with open(output_file, 'w') as file:
        for day, avg_yards in avg_yards_per_day.items():
            file.write(f"{day}: {avg_yards:.2f} average yards per attempt\n")

    conn.close()

if __name__ == "__main__":
    db_path = "please4.db"  # Replace with your actual database file path
    output_file = "avg_yards_per_day.txt"
    calculate_and_write_data(db_path, output_file)

