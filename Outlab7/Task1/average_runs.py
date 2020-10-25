import sqlite3
c = sqlite3.connect("ipl.db")

cur = c.cursor()
cur.execute("SELECT match_id, venue_name FROM MATCH")

rows = cur.fetchall()

id_to_venue = {}
match_count = {}
for r in rows:
	id_code, venue = r 
	if id_code == "NULL":
		continue
	if venue=="NULL":
		continue
	id_to_venue[id_code] = venue
	match_count[venue] = match_count.get(venue, 0) + 1

runs = {}
cur.execute("SELECT runs_scored, extra_runs, match_id FROM BALL_BY_BALL")

rows = cur.fetchall()

for r in rows:
	run, extra_runs, match_id = r 
	if match_id=="NULL":
		continue 
	if run == "NULL":
		run = 0 
	if extra_runs == "NULL":
		extra_runs = 0
	runs[match_id] = runs.get(match_id, 0) + run + extra_runs

total_runs = {}

for match, run in runs.items():
	total_runs[id_to_venue[match]] = total_runs.get(id_to_venue[match], 0) + run

data = []

for venue, total in total_runs.items():
	data.append((venue, total/match_count[venue]))

data.sort(key=lambda x: (-x[1], x[0]))

for ven, av in data:
	print (ven, av, sep=",")

c.close()