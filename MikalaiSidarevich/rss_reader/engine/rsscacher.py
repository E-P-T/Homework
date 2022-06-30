"""
RssCacher - SQLite3 database handler, work with cached RSS entries.
"""

import sqlite3
import threading

# Define the lock globally
lock = threading.Lock()


class StorageError(Exception):
    """
    Cache storage exception.
    """
    pass


class QueryError(Exception):
    """
    Database query exception.
    """
    pass


class RssCacher:
    """SQLite3 database handler, work with cached RSS entries."""

    def __init__(self, dbname, verbose=False):
        """
        Initialize database name and verbosity.
        """
        self._dbname = dbname
        self._verbose = verbose

    def __enter__(self):
        """
        Context manager entry point.
        Create tables if they're not exist.
        """
        self._connect()
        self._create_tables()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Context manager exit point.
        """
        if exc_type:
            raise
        self._close()

    def _connect(self):
        """
        Connect to database & set the cursor.
        """
        try:
            self._conn = sqlite3.connect(self._dbname, check_same_thread=False)
            self._conn.row_factory = sqlite3.Row
            self._cur = self._conn.cursor()
        except Exception:
            raise StorageError(f"Unable to open '{self._dbname}' database")

    def _close(self):
        """
        Close database connection.
        """
        self._conn.close()

    def _create_tables(self):
        """
        Create tables to store RSS data in local storage.
        """
        try:
            query = """CREATE TABLE IF NOT EXISTS channels (
                        id INTEGER PRIMARY KEY,
                        channel TEXT,
                        url TEXT)"""
            self._cur.execute(query)

            query = """CREATE TABLE IF NOT EXISTS entries (
                        id INTEGER PRIMARY KEY,
                        title TEXT,
                        link TEXT,
                        date TEXT,
                        date_fmt TEXT,
                        description TEXT,
                        image_link TEXT,
                        image_data BLOB,
                        channel_id INTEGER,
                        FOREIGN KEY (channel_id) REFERENCES channels (id))"""
            self._cur.execute(query)
        except Exception as e:
            raise StorageError(f"Unable to create tables in '{self._dbname}' database ({e})")

    def store_channel(self, feed):
        """
        Save RSS channel data into the `channels` table.
        """
        try:
            # Check channel duplicate
            query = ("SELECT id FROM channels WHERE url=?")
            self._cur.execute(query, (feed['url'],))
            row = self._cur.fetchone()

            # Store channel data
            if row:
                query = "UPDATE channels SET channel=? WHERE url=?"
            else:
                query = "INSERT INTO channels (channel, url) VALUES (?,?)"

            self._cur.execute(query, (feed['channel'], feed['url']))
            self._conn.commit()
        except Exception as e:
            raise StorageError(f"Unable to store channel data into '{self._dbname}' ({e})")

    def store_entry(self, entry, channel_id):
        """
        Save RSS entry info into the `entries` table.
        """
        try:
            lock.acquire(True)

            # Check entry duplicate
            query = ("SELECT id FROM entries WHERE `link`=?")
            self._cur.execute(query, (entry['link'],))
            row = self._cur.fetchone()

            values = [entry['title'],
                      entry['link'],
                      entry['date'],
                      entry['date_fmt'],
                      entry['description'],
                      entry['image_link'],
                      entry['image_data'],
                      channel_id]

            # Store entry
            if row:
                query = """UPDATE entries SET
                            title=?,
                            link=?,
                            date=?,
                            date_fmt=?,
                            description=?,
                            image_link=?,
                            image_data=?,
                            channel_id=? WHERE link=?"""
                values += (entry['link'],)
            else:
                query = """INSERT INTO entries (
                            title,
                            link,
                            date,
                            date_fmt,
                            description,
                            image_link,
                            image_data,
                            channel_id
                            ) VALUES (?,?,?,?,?,?,?,?)"""

            self._cur.execute(query, values)
            self._conn.commit()
        except Exception as e:
            raise StorageError(f"Unable to store entry data into '{self._dbname}' ({e})")
        finally:
            lock.release()

    def get_channel_id(self, url):
        """
        Get channel id by channel `url`.
        """
        query = ("SELECT id FROM channels WHERE url=?")
        self._cur.execute(query, (url,))
        return self._cur.fetchone()['id']

    def feed(self, url, limit, date):
        """
        Get list of RSS feeds from storage.
        `url` sets RSS channel,
        `limit` sets total number of entries,
        `date` sets entries date filter.
        """
        query = """SELECT
                        entries.title as title,
                        entries.link as link,
                        entries.date as date,
                        entries.date_fmt as date_fmt,
                        entries.description as description,
                        entries.image_link as image_link,
                        entries.image_data as image_data,
                        channels.channel as channel,
                        channels.url as url
                    FROM entries JOIN channels ON entries.channel_id=channels.id
                    WHERE entries.date_fmt=?"""

        # Set url filter
        if url is not None:
            url = url.lower().rstrip('/')
            query += f" AND channels.url='{url}'"

        # Set limit filter
        if limit is not None:
            query += f" LIMIT {limit}"

        self._cur.execute(query, (date, ))
        db_entries_list = self._cur.fetchall()

        # Create feed list
        if db_entries_list:
            feed_list = []

            # Place entries by channels
            for db_entry in db_entries_list:
                entry = {'title': db_entry['title'],
                         'link': db_entry['link'],
                         'date': db_entry['date'],
                         'date_fmt': db_entry['date_fmt'],
                         'description': db_entry['description'],
                         'image_link': db_entry['image_link'],
                         'image_data': db_entry['image_data']}

                for feed in feed_list:
                    # Add entry to its channel
                    if db_entry['channel'] in feed.values():
                        feed['entries'].append(entry)
                        break
                else:
                    # Set channel at first occurence
                    feed = {'channel': db_entry['channel'],
                            'url': db_entry['url'],
                            'entries': [entry]}

                    # Add new feed structure into the result list
                    feed_list.append(feed)
        else:
            raise QueryError(f"There are no entries for the date '{date}'")

        return feed_list
