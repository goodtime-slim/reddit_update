import sqlite3

conn = sqlite3.connect('G:/data/reddit_update/db.db')

c = conn.cursor()
c.execute("""create table if not exists main
(link_id text, comment_id text, insert_date timestamp)
""")
conn.close()