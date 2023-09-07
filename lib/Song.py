from config import CONN, CURSOR

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


    def save(self):
        sql = """
                insert into songs(name, album) values (? , ?)
            """
        
        CURSOR.execute(sql, (self.name, self.album))
        self.id = CURSOR.execute("SELECT last_insert_rowid() FROM songs").fetchone()[0]

    @classmethod
    def create(cls, name, album):
        instance_song = Song(name, album)
        instance_song.save()
        return instance_song