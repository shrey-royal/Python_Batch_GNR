import mysql.connector
from mysql.connector import Error
from mysql.connector.connection import MySQLConnection

def connect_db() -> MySQLConnection:
    """Establish connection with MySQL"""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database="test"
        )

        if connection.is_connected():
            version_info = connection.get_server_info()
            print(f"Successfully connected to MySQL Server Version {version_info}")
            return connection
        
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None

def create_user(name: str, email: str, age: int, country: str) -> None:
    conn = connect_db()
    if conn is None:
        return "Connection failed!"

    try:
        cursor = conn.cursor()
        query = "INSERT INTO users (name, email, age, country) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (name, email, age, country))
        conn.commit()
        print(f"User {name} added successfully!")
    except Error as e:
        print(f"Failed to add user {name}: {e}")
        conn.rollback()
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def main():
    while True:
        print("\n-- CRUD Menu ---")
        print("1. Create User")
        print("2. Read All User")
        print("3. Update User")
        print("4. Delete User")
        print("5. GetUserById")
        print("6. Exit")

        choice = int(input("Enter your choice (1-6): "))

        match choice:
            case 1:
                name = input("Enter name: ")
                email = input("Enter email: ")
                try:
                    age = int(input("Enter age: "))
                except ValueError:
                    print("Invalid age! Please enter a valid number.")
                    continue
                country = input("Enter country: ")
                create_user(name, email, age, country)

            case 2:
                print("\nAll Users:")
                # read_users()

            case 3:
                try:
                    user_id = int(input("Enter user ID to update: "))
                    name = input("Enter a new name or press '-' to skip: ")
                    email = input("Enter a new email or press '-' to skip: ")
                    age = input("Enter a new age or press '-' to skip: ")
                    country = input("Enter a new country or press '-' to skip: ")
                except ValueError:
                    print("Invalid Data! Please enter valid data.")
                    continue

                if name == '-':
                    name = None
                if email == '-':
                    email = None
                if age == '-':
                    age = None
                if country == '-':
                    country = None

                # update_user(user_id, name, email, age, country)

            case 4:
                try:
                    user_id = int(input("Enter user ID to delete: "))
                except ValueError:
                    print("Invalid user ID! Please enter a valid number.")
                    continue

                # delete_user(user_id)

            case 5:
                try:
                    user_id = int(input("Enter user ID to get the user details: "))
                except ValueError:
                    print("Invalid user ID! Please enter a valid number.")
                    continue

                # get_user_by_id(user_id)

            case 6:
                print("Exiting the program...")
                break

            case _:
                print("Invalid choice. Please enter a number betwee 1 and 6.")


if __name__ == "__main__":
    main()



"""
Task:
make a table on anything with minimum of 5 attrs (1 bool compulsory).
make crud on that table.
"""