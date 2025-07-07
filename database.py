import mysql.connector
from mysql.connector import Error

def init_db():
    try:
        # Connect to MySQL (update with your credentials)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Replace with your MySQL username
            password=""  # Replace with your root password
        )
        cursor = connection.cursor()

        # Create database
        cursor.execute("CREATE DATABASE IF NOT EXISTS travel_itinerary")
        cursor.execute("USE travel_itinerary")

        # Create itineraries table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS itineraries (
                thread_id VARCHAR(255) PRIMARY KEY,
                destination VARCHAR(255) NOT NULL,
                budget FLOAT NOT NULL,
                duration INT NOT NULL,
                itinerary TEXT
            )
        """)
        connection.commit()
        print("Database and table created successfully")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    init_db()