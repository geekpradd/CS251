import sqlite3
c = sqlite3.connect("ipl.db")

cur = c.cursor()
cur.execute("SELECT player_id, player_name FROM PLAYER")

id_name = {}

rows = cur.fetchall()

for r in rows:
	if r[0] == "NULL" or r[0] == None:
		continue 
	id_name[r[0]] = r[1]

cur.execute("SELECT out_type, bowler FROM BALL_BY_BALL")

rows = cur.fetchall()

wickets = {}

for r in rows:
	if r[0] == "Not Applicable" or r[0] == "NULL" or r[0] == None:
		wick = 0
	else:
		wick = 1
	if r[1] == "NULL" or r[1] == None:
		continue 
	wickets[r[1]] = wickets.get(r[1], 0) + wick

data = []

for bowler, wicks in wickets.items():
	data.append([bowler,id_name[bowler],wicks])

data.sort(key=lambda x: (-x[2], x[1]))

for items in data[:20]:
	print(",".join(map(str, items)))


c.close()