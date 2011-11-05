
import MySQLdb
import string
import re

db=MySQLdb.connect(host="localhost",user="root", passwd="root",db="unweb_iub")
cu=db.cursor()

cu.execute("SELECT DISTINCT SES_ID FROM hde")
ses=cu.fetchall()
sarray=[]	
for s in ses:
	a=s[0]
	sarray.append(a)

for i in range(len(sarray)):
	print 'the number of indexed URLs in the %d th session #', sarray[i]
	cu.execute("SELECT COUNT(INDEXED) FROM hde WHERE INDEXED=1 AND SES_ID=%s",sarray[i])
	d=cu.fetchall()
	print d
	print 'the number of unindexed URLs in the %d th session #' ,sarray[i]
	cu.execute("SELECT COUNT(INDEXED) FROM hde WHERE INDEXED=0 AND SES_ID=%s",sarray[i])
	e=cu.fetchall()
	print e
	print 'info of the root url of %d th session', sarray[i]
	cu.execute("SELECT Host FROM hde WHERE S_ID='1' AND SES_ID=%s",sarray[i])
	de=cu.fetchall()
	print de[0][0]
	se=de[0][0]
	if re.search("[google|bing|yahoo]", se):
		print "root is a search engine"
	

	print '-----------------------------------------------------------'
