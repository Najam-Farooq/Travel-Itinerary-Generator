import mysql.connector
from mysql.connector import Error
import uuid

def init_db():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="travel_itinerary"
        )
        cursor = connection.cursor()
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
        print("Database and table initialized successfully")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

def save_itinerary(destination, budget, duration, itinerary):
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="travel_itinerary"
        )
        cursor = connection.cursor()
        thread_id = str(uuid.uuid4())
        query = """
            INSERT INTO itineraries (thread_id, destination, budget, duration, itinerary)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (thread_id, destination, budget, duration, itinerary))
        connection.commit()
        print(f"Itinerary saved with thread_id: {thread_id}")
        return thread_id
    except Error as e:
        print(f"Error: {e}")
        return None
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

def get_itinerary(thread_id):
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="travel_itinerary"
        )
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM itineraries WHERE thread_id = %s"
        cursor.execute(query, (thread_id,))
        result = cursor.fetchone()
        if result:
            print(f"Itinerary retrieved for thread_id: {thread_id}")
            return result
        else:
            print(f"No itinerary found for thread_id: {thread_id}")
            return None
    except Error as e:
        print(f"Error: {e}")
        return None
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    init_db()
    test_thread_id = "629fce12-86d7-4a22-adf1-10adbeacfd2d"
    result = get_itinerary(test_thread_id)
    print(f"Test result: {result}")