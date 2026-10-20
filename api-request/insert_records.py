import psycopg2
from api_request import mock_fetch_data,fetch_data

def connect_to_db():
    print("Connecting to the PostgreSQL database...")
    try:
        conn = psycopg2.connect(
            host="db",
            port=5432,
            dbname="db",
            user="db_user",
            password="db_password"
        )
        return conn
    
    except psycopg2.Error as e:
        print(f"Database connection Failed: {e}")
        raise

def create_table(conn):
    print("Creating table if not exist...")
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE SCHEMA IF NOT EXISTS weather_data;
            CREATE TABLE IF NOT EXISTS weather_data.weather_records (
                id SERIAL PRIMARY KEY,
                city TEXT,
                temperature FLOAT,
                weather_description TEXT,
                wind_speed FLOAT,
                time TIMESTAMP,
                inserted_at TIMESTAMP DEFAULT NOW(),
                utc_offset TEXT
                );
        """)
        conn.commit()
        print("Table created successfully!")
    except psycopg2.Error as e:
        print(f"Faild to create the table: {e}")
        raise


def insert_records(conn,data):
    print("Inserting records into the database...")
    try:
        weather = data['current']
        location = data['location']

        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO weather_data.weather_records (
                city,
                temperature,
                weather_description,
                wind_speed,
                time,
                inserted_at,
                utc_offset
            ) VALUES (%s, %s, %s, %s, %s, NOW(), %s)
        """,(
            location['name'],
            weather['temperature'],
            weather['weather_descriptions'][0],
            weather['wind_speed'],
            location['localtime'], 
            location['utc_offset']
        ))
        conn.commit()
        print("Records inserted successfully!")

    except psycopg2.Error as e:
        print(f"Failed to insert records: {e}")
        raise


def main():
    try:
        data = mock_fetch_data()
        #data = fetch_data()
        conn = connect_to_db()
        create_table(conn)
        insert_records(conn, data)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if 'conn' in locals():
            conn.close()
            print("Database connection closed.")    

main()
    
