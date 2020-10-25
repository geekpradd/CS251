import sqlite3

conn = sqlite3.connect("univ.db")
def exec_scripts(name):
    buffer = ""
    with open(name) as f:
        for cmd in f.readlines():
            buffer+=cmd
            if sqlite3.complete_statement(buffer):
                try:
                    c.executescript(buffer)
                except:
                    pass
                buffer = ""

with conn:
    c = conn.cursor()
    exec_scripts("University Schema")
    exec_scripts("smallRelationsInsertFile.sql")
conn.commit()
conn.close()
