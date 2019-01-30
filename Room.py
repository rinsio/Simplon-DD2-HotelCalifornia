class Room:

  def __init__(self, id_hotel, num, name, surface):
    self.id_hotel = id_hotel
    self.num = num
    self.name = name
    self.surface = surface

  def create_table(conn):
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS room (
      id_hotel integer NOT NULL,
      num INTEGER NOT NULL,
      name TEXT NOT NULL,
      surface INTEGER NOT NULL,
      FOREIGN KEY(id_hotel) REFERENCES hotel(id),
      PRIMARY KEY (id_hotel, num)
    )""")

  def load(self, conn):
    cur = conn.cursor()
    cur.execute("INSERT INTO room (id_hotel, num, name, surface) VALUES(%s, %s, %s, %s)", (self.id_hotel, self.num, self.name, self.surface))
    
