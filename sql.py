import sqlite3
import datetime


def insert_comment_ids(thread_id, comment_ids):
    conn = sqlite3.connect('G:/data/reddit_update/db.db')
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    values = [(thread_id, now, x) for x in comment_ids]
    conn.executemany('insert into main values (?, ?, ?)', values)
    conn.commit()
    conn.close()
