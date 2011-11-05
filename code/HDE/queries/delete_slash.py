import MySQLdb
import struct, os
db=MySQLdb.connect(host="localhost",user="root", passwd="root",db="unweb_iub")
cursor=db.cursor()

slash_control="""select URL FROM hde"""
cursor.execute(slash_control)
slash_rows=cursor.fetchall()
for slrows in slash_rows:
	a=slrows[0]
	if a[-1]== '/':
		b=a[:-1]
		print b
		print a
		slash_sql="""UPDATE hde SET URL=%s WHERE URL=%s""" %(b,a)
		#slash_sql="""SELECT URL FROM hde WHERE URL=%s""" %a
		cursor.execute(slash_sql)
		print cursor.fetchall()
