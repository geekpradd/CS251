import csv
import sqlite3

c = sqlite3.connect('ipl.db')

def operate(f, table):
	with open(f) as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		line = 0
		base = ""
		for row in reader:
			if not line:
				base = (", ".join(row))
				line += 1	
			else:
				query = """INSERT INTO {0}({1}) VALUES({2});""".format(table, base, ("'"+"', '".join(row) + "'"))
				query = query.replace("'NULL'", "NULL")
				c.execute(query)
				line += 1

data = [("team.csv", "TEAM"), ("match.csv", "MATCH"), ("player.csv", "PLAYER"), ("player_match.csv", "PLAYER_MATCH"), ("ball_by_ball.csv", "BALL_BY_BALL")]

for a, b in data:
	operate(a, b)

c.commit()
c.close()