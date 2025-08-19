import sqlite3

conn = sqlite3.connect("people.sqlite")
c = conn.cursor()

query = """
INSERT INTO friends (f_name, l_name, email)
VALUES ('Lucas ', 'Graham', 'lgraham@gmail.com');
"""

c.execute(query)
conn.commit()
conn.close()
