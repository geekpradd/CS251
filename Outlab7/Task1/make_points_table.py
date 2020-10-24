import sqlite3

c = sqlite3.connect('ipl.db')

c.execute('''CREATE TABLE IF NOT EXISTS POINTS_TABLE  
         (team_id INT PRIMARY KEY     NOT NULL,
         team_name           TEXT,
         points              INT DEFAULT 0,
         nrr                 DECIMAL DEFAULT 0);''')
c.commit()

cur = c.cursor()
cur.execute("SELECT team_id, team_name FROM TEAM")

rows = cur.fetchall()

for r in rows:
	c.execute("INSERT INTO POINTS_TABLE(team_id, team_name) VALUES({0}, '{1}');".format(r[0], r[1]))
	
c.commit()
cur.execute("SELECT team1, team2, match_winner, win_type, win_margin FROM MATCH")

points = {}
nrr = {}
rows = cur.fetchall()

for r in rows:
	if r[3].lower() == "tie" or r[2]=="NULL" or r[2] is None:
		print(r[0])
		points[r[0]] = points.get(r[0], 0) + 1
		points[r[1]] = points.get(r[1], 0) + 1
	else:
		points[r[2]] = points.get(r[2], 0) + 2

		if r[3] == "runs":
			value = r[4]/20.0 
		else:
			value = r[4]/10.0
		if r[0] == r[2]:
			loser = r[1]
		else:
			loser = r[0]

		nrr[r[2]] = nrr.get(r[2], 0) + value 
		nrr[loser] = nrr.get(loser, 0) - value


for team, pts in points.items():
	c.execute("UPDATE POINTS_TABLE SET points = {0} WHERE team_id = {1}".format(pts, team)) 
	

for team, nrr in nrr.items():
	c.execute("UPDATE POINTS_TABLE SET nrr = {0} WHERE team_id = {1}".format(nrr, team)) 

c.commit()
cur.execute("SELECT * FROM POINTS_TABLE")

rows = cur.fetchall()
rows.sort(key=lambda x: (-x[2], -x[3]))
for data in rows:
	print(",".join(map(str,data)))

c.close()