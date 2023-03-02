import sqlite3

create_table_command = """
CREATE TABLE feed_item (
    id INTEGER PRIMARY KEY,
    base_url VARCHAR(1024),
    feed_url VARCHAR(1024),
    url VARCHAR(1024),
    title VARCHAR(1024),
    author VARCHAR(1024),
    date DATE,
    tag VARCHAR(255),
    content VARCHAR(65535),
    language VARCHAR(32),
    unread INTEGER(1),
    rtl INTEGER(1)
);
"""


def create_table(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute(create_table_command)
    conn.commit()
    conn.close()
