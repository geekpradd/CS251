import sqlite3
c = sqlite3.connect("ipl.db")

cur = c.cursor()
cur.execute("SELECT player_id, player_name FROM PLAYER")

id_name = {}

rows = cur.fetchall()

for r in rows:
	id_name[r[0]] = r[1]

cur.execute("SELECT runs_scored, striker FROM BALL_BY_BALL")

rows = cur.fetchall()

scores = {}

for r in rows:
	scores[r[1]] = scores.get(r[1], 0) + r[0]

data = []

for striker, runs in scores.items():
	data.append([striker,id_name[striker],runs])

data.sort(key=lambda x: (-x[2], x[1]))

for items in data[:20]:
	print(",".join(map(str, items)))

c.close()