import sys
import sqlite3
conn = sqlite3.connect("univ.db")
c = conn.cursor()
# conn.set_trace_callback(print)

isinjectable = False
if int(sys.argv[1].strip())==0:
    isinjectable = True
table = sys.argv[2]
column = sys.argv[3]
condition = sys.argv[4]

if isinjectable:
    query = "SELECT * FROM {} WHERE {} = '{}'".format(table,column,condition)
    try:
        c.execute(query)
        for items in c.fetchall():
        	print(",".join(map(str, items)))
    except:
        pass
else:
    query = "SELECT * FROM {} WHERE {} = ?".format(table,column)
    try:
        c.execute(query,(condition,))
        for items in c.fetchall():
        	print(",".join(map(str, items)))
    except:
        pass
    
# conn.commit()
conn.close()