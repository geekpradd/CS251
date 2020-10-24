import sqlite3, sys

c = sqlite3.connect('ipl.db')
c.set_trace_callback(print)

case = int(sys.argv[1]) - 1
names = ["TEAM", "PLAYER", "MATCH", "PLAYER_MATCH", "BALL_BY_BALL"]

def get_col(table):
    cur = c.execute("Select * from {}".format(table))
    nam = list(map(lambda x: x[0],cur.description))
    return len(nam)

def get_query(table): 
    return "INSERT INTO {0} VALUES({1}?);".format(table, '?,'*(get_col(table)-1))

query = get_query(names[case])
print(query)
c.execute(query,tuple(sys.argv[2:]))

c.commit()
c.close()