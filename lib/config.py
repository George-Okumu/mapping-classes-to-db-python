import sqlite3

CONN = sqlite3.connect('db/music.db') # sets connection
CURSOR = CONN.cursor() # allows us to interact with the db