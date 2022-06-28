import sqlite3
import time
import os
import logging as log
import json

data_base = "news_data.db"

class DataBaseHandler:

    """Class that handles with sqlite3 database. With that class you can:
     adress to your DB through context manager, create table, input data to table,
     get data from table by date, souce, check emtyness of the table."""

    def __init__(self, base_path):
        log.info("Initialization of object complieted.")
        self.path = base_path

    def __enter__(self):
        log.info("Connection to database esteblished.")
        self.conn = sqlite3.connect(self.path)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        log.info("Connection closed")
        if exc_type is None:
            self.conn.close()

    def create_table(self):

        """Metod that help us to create table in our database if it doesn't exist.
        Table contains next fields: date TEXT,
                                    source TEXT,
                                    title TEXT,
                                    url TEXT,
                                    full_date TEXT,
                                    description TEXT"""

        with DataBaseHandler(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS news_data (
                           date TEXT,
                           source TEXT,
                           title TEXT,
                           url TEXT,
                           full_date TEXT,
                           description TEXT)""")
            conn.commit()
            log.info("Now news_data table exists in out database.")


    def emptiness_checker(self):

        """This metod check our database and return boolean result.
            If it is empty - return True, else return - False"""

        log.info("Cheking table for emptiness...")
        with DataBaseHandler(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute("""SELECT COUNT(*) FROM news_data""")
            result = cursor.fetchone()
        if result[0] == 0:
            log.info("Table is empty!")
            return True
        else:
            log.info("There is data in the table!")
            return False

    def add_data(self, source, *args):

        """This method add information to news_data table,
        also this method creates information to date field."""

        converted_date = time.strptime(args[2], "%a, %d %b %Y %H:%M:%S %z")
        date = time.strftime("%Y%m%d", converted_date)
        with DataBaseHandler(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute("""INSERT INTO news_data (date, source, title, url, full_date, description) 
                            VALUES (?, ?, ?, ?, ?, ?)""", (date, source, args[0], args[1], args[2], args[3]))
            conn.commit()
            log.info("Data added to the news_data table.")

    def retrieve_data(self, date, source=None, num=None):

        """If num parameter specified, takes numered quantity of data,
        from database especially by date, and by source if it specified."""

        with DataBaseHandler(self.path) as conn:
            cursor = conn.cursor()
            if source is None:
                cursor.execute("""SELECT title, url, full_date, description FROM news_data WHERE date=?""", (date,))
            else:
                cursor.execute("""SELECT title, url, full_date, description 
                                 FROM news_data WHERE date=? AND source=?""", (date, source))
            conn.commit()
            data = cursor.fetchall()
        if len(data) == 0:
            log.info("There is no such data in the table.")
            raise ValueError
        if num is None:
            self.data = data
            log.info("Provided amount of data retrieved from the table.")
        else:
            self.data = data[:num]
            log.info("Provided amount of data retrieved from the table.")
        return self.data

    def data_to_json(self, date):

        """Returns retrieved data from database in json format"""

        log.info("Collecting data in json!")
        self.json_data = {date:[]}
        for i in self.data:
            fact_dict = {"Title": i[0],
                        "Link": i[1],
                        "Date": i[2],
                        "Description": i[3],
                        }
            self.json_data[date].append(fact_dict)
        return json.dumps(self.json_data, ensure_ascii=False, indent=4)


    def data_to_print(self, date):

        """Prints retrieved data from database to console."""
        log.info("Printing data from database.")
        print(f"News on {date}!\n")
        for i in self.data:
            print(f"Title: {i[0]}")
            print(f"Date: {i[2]}")
            print(f"Link: {i[1]}")
            print(f"Description: {i[3]}", end="\n")
            print('\n')





