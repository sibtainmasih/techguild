import logging
import sqlite3
from sqlite3 import Error

from contactbook.settings import STORAGE_FILE

logger = logging.getLogger(__name__)

__CLIENT_CONTACT_QUERYS = {
    "create_table": """
    CREATE TABLE IF NOT EXISTS ClientContact (
        id integer PRIMARY KEY,
        name text NOT NULL UNIQUE,
        address text NOT NULL,
        city text NOT NULL,
        phone text NOT NULL,
        email text NOT NULL,
        create_date text NOT NULL,
        last_modified_date text NOT NULL,
        notes text,
        is_active integer NOT NULL
    );
    """,
    "insert": """
    INSERT INTO ClientContact 
    (name, address, city, phone, email, create_date, last_modified_date, is_active)
    VALUES
    ('{name}', '{address}', '{city}', '{phone}', '{email}', datetime('now'), datetime('now'), 1)
    """,
    "select": """
    SELECT name, address, city, phone, email
    FROM ClientContact
    WHERE {filer_column_name}='{filter_column_value}' AND is_active=1
    """,
    "update": """
    UPDATE ClientContact 
    SET {update_column_name}='{new_value}' 
    WHERE {filer_column_name}='{filter_column_value}'
    """,
    "soft_delete": """
    UPDATE ClientContact
    SET is_active=0
    WHERE {filer_column_name}='{filter_column_value}'
    """,
    "delete": """
    DELETE FROM ClientContact 
    WHERE {filer_column_name}='{filter_column_value}'
    """,
}


def __get_connection(db_file=STORAGE_FILE):
    """ 
    create a database connection to the SQLite database specified by the db_file.
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error:
        logger.exception(f"Database connection failed for {db_file}")

    return conn


def setup_database():
    """
    Creats client_contact table in database
    """
    try:
        conn = __get_connection()
        cur = conn.cursor()
        cur.execute(__CLIENT_CONTACT_QUERYS["create_table"])
    except Error:
        logger.exception("Unable to create client_contact table.")


def save_contact(name, address, city, phone, email):
    insert_sql = __CLIENT_CONTACT_QUERYS["insert"].format(
        name=name, address=address, city=city, phone=phone, email=email
    )
    conn = __get_connection()
    cur = conn.cursor()
    cur.execute(insert_sql)
    conn.commit()
    return cur.lastrowid


def update_contact(filter_column_name, filter_column_value):
    pass


def get_contacts(filter_column_name, filter_column_value):
    conn = __get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")

    rows = cur.fetchall()

    for row in rows:
        print(row)
