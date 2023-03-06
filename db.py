import sqlite3

create_table_command = """
CREATE TABLE IF NOT EXISTS feed_item (
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


def create_table(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute(create_table_command)
    conn.commit()
    conn.close()


def add_feed(db_file, feed_item):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM feed_item WHERE url = ?", (feed_item["link"],))
    item_exists = cursor.fetchone()
    if not item_exists:
        cursor.execute(
            "INSERT INTO feed_item (base_url, feed_url, url, title, author, date, tag, content, language, unread, rtl) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                feed_item["base_url"],
                feed_item["feed_url"],
                feed_item["link"],
                feed_item["title"],
                feed_item["author"],
                feed_item["date"],
                feed_item["tag"],
                feed_item["content"],
                feed_item["language"],
                feed_item["unread"],
                feed_item["rtl"],
            ),
        )

        print(f"Added {feed_item['title']} to the database")
        conn.commit()
        conn.close()
    else:
        print(f"Feed item {feed_item['title']} is already in the database")
