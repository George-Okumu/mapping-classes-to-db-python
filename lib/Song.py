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
    
    #mapping the data from db
    @classmethod
    def new_from_db(cls, row):
        song = cls(row[1], row[2])
        song.id = row[0]
        return song
    
    
    #getting all items from db
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM songs
        """

        all = CURSOR.execute(sql).fetchall()
        mine = [cls.new_from_db(row) for row in all]
        return [mine.__dict__ for mine in mine] #returning the objects as objects
    
    #Less convinient method
    # @classmethod
    # def find_music_by_name(cls, name):
    #     all_things = cls.get_all()
    #     for i in all_things:
    #         if(i['name'] == name):
    #             return i
    #         else:
    #             return "Name not found"

    @classmethod
    def find_music_by_name(cls, name):
        sql = """
            select * from songs where name = ? LIMIT 1
            """
        song_found = CURSOR.execute(sql, (name,)).fetchone()
        """
        Bound parameters must be passed to the execute statement as a 
        sequence data type. This is typically performed with tuples to match the 
        format that results are returned in. A tuple containing only one element must 
        have a comma after that element, otherwise it is interpreted as a grouped statement 
        The fetchone() method returns the first element from fetchall().
        
        """
        return cls.new_from_db(song_found)
    
    
    @classmethod
    def drop_table(cls):
        sql = """
                drop table if exists songs
            """
        
        CURSOR.execute(sql)