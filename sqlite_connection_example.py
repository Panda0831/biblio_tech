
import sqlite3

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)

    return conn

def main():
    database = r"/home/panda831/Documents/manjaka/S3/python/tkinker/biblio/pythonsqlite.db"

    # create a database connection
    conn = create_connection(database)

    if conn:
        print("Connection to SQLite DB successful")
        conn.close()
    else:
        print("Error! Cannot create the database connection.")


if __name__ == '__main__':
    main()
