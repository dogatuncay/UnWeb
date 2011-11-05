import MySQLdb
import MySQLdb.cursors

db=MySQLdb.connect(host="localhost",user="root", passwd="root",db="unweb_iub" )
cursor=db.cursor()
cursor.execute("SELECT URL FROM hde")

rows=cursor.fetchall()
f=open('URL.txt','w')
for row in rows:
	f.write(row[0])
	f.write('\n')

f.close()		
cursor.close()	
db.close()
