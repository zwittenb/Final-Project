import sqlite3
import matplotlib.pyplot as plt

def analyze_and_visualize_michigan_home_scores(database_file):
    
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()
    cursor.execute('SELECT season, week, home_score FROM michigan_total_scores')
    rows = cursor.fetchall()

    # Perform calculations (modify as needed)
    total_home_scores = [row[2] for row in rows]

    # Visualize the results (modify as needed)
    plt.plot(total_home_scores)
    plt.xlabel('Games')
    plt.ylabel('Home Score (Michigan)')
    plt.title('Home Scores of Michigan Football Games Over Seasons')
    plt.show()
    conn.close()

# Example usage
analyze_and_visualize_michigan_home_scores('michigan_home_scores_database.db')
