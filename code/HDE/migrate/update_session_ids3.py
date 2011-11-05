import MySQLdb
import MySQLdb.cursors

db=MySQLdb.connect(host="localhost",user="root", passwd="root",db="unweb_iub" )
cursor=db.cursor()
cursor.execute("SELECT S_ID FROM hde")
db.commit()
x=0
z=1
rows=cursor.fetchall()
for row in rows:
	if row[0] == 1:
		x += 1
	cursor.execute("UPDATE hde SET SES_ID='%d' WHERE E_ID='%d' " %(x,z))
	db.commit()
	z += 1			
cursor.close()	
db.close()		

