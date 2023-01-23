# sql
# субд система управлениями базданных
import sqlite3

db = sqlite3.connect('26_3.db')

c = db.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS user (
name text,
title text,
view integer,
nick text
) ''')
#
# c.execute("INSERT INTO user VALUES ('BEKAAA','АAГАЙ',2200,'ogilI')")
# c.execute("INSERT INTO user VALUES ('элдияр','газета',499,'Кактус')")
# c.execute("SELECT rowid FROM user")
c.execute("UPDATE user SET name = 'максим' WHERE rowid = 1 ")
# c.execute("DELETE FROM user WHERE nick <> 'O'  ")
c.execute("SELECT rowid,* FROM user ORDER BY rowid  ")
# print(c.fetchall())
# print(c.fetchmany(2))
# print(c.fetchone())
#
item = c.fetchall()
for el in item:
    print(el)

db.commit()
db.close()
