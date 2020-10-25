import sqlite3
c = sqlite3.connect("ipl.db")

cur = c.cursor()
cur.execute("SELECT player_id, player_name FROM PLAYER")

id_name = {}

rows = cur.fetchall()

for r in rows:
	if r[0] == "NULL":
		continue 
	id_name[r[0]] = r[1]

cur.execute("SELECT runs_scored, striker FROM BALL_BY_BALL")

rows = cur.fetchall()

sixes = {}
total = {}
for r in rows:
	if r[1] == "NULL":
		continue
	if r[0] == "NULL":
		continue
	sixes[r[1]] = sixes.get(r[1], 0) + (1 if r[0]==6 else 0)
	total[r[1]] = total.get(r[1],0) + 1

data = []

for striker, sixs in sixes.items():
	data.append([striker,id_name[striker],sixs, total[striker], (sixs*1.0)/total[striker]])

data.sort(key=lambda x: (-x[4], x[1]))

for items in data:
	print(",".join(map(str, items)))

c.close()