from . import CONN, CURSOR

class Song:
    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album

    @classmethod
    def create_table(self):
        sql = """
                create table if not exists songs(
                    id integer primary key,
                    name varchar,
                    album varcahr
                    )
            """
        CURSOR.execute(sql)