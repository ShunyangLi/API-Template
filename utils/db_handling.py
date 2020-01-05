import sqlite3
import os

# get the path of database
sqlite_database = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.sqlite")


def query_db(query, args=(), one=False):
    """
    execute the database query language and return the query result.
    :param query: the query sql language
    :param args: the args in query language
    :param one: whether only one result
    :return: the list tuple of result
    """
    conn = sqlite3.connect(sqlite_database)
    c = conn.cursor()
    curs = c.execute(query, args)
    res = [dict((curs.description[idx][0], value)
               for idx, value in enumerate(row)) for row in curs.fetchall()]

    conn.commit()
    conn.close()
    return (res[0] if res else None) if one else res