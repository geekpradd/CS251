import sqlite3, sys

c = sqlite3.connect('ipl.db')

case = int(sys.argv[1]) - 1

names = ["TEAM", "PLAYER", "MATCH", "PLAYER_MATCH", "BALL_BY_BALL"]

total = [2, 6, 15, 7, 11]


data = "'" + "', '".join(sys.argv[2:2+total[case]]) + "'"

query = "INSERT INTO {0} VALUES({1});".format(names[case], data)
c.execute(query)

c.commit()
c.close()