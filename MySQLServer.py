import mysql.connector
from mysql.connector import Error


def create_database():
    try:
        # Update these variables with your MySQL server credentials
        host = "localhost"
        user = "root"
        password = "Password@1"

        # Connect to MySQL server (not to a specific database)
        connection = mysql.connector.connect(host=host, user=user, password=password)

        if connection.is_connected():
            cursor = connection.cursor()
            try:
                cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
                print("Database 'alx_book_store' created successfully!")
            except Error as e:
                print(f"Error creating database: {e}")
            finally:
                cursor.close()
        else:
            print("Failed to connect to MySQL server.")
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL server: {e}")
    finally:
        if "connection" in locals() and connection.is_connected():
            connection.close()


if __name__ == "__main__":
    create_database()
