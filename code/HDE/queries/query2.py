
import MySQLdb
import struct, os
db=MySQLdb.connect(host="localhost",user="root", passwd="root",db="unweb_iub")
cursor=db.cursor()

sql_ses="""select DISTINCT SES_ID FROM hde"""
cursor.execute(sql_ses)
ses_rows=cursor.fetchall()
for srows in ses_rows:
	print srows[0]
sid=input("PICK A SESSION ID FROM THE LIST: ")

sql="""select DISTINCT id, url_crawler.url FROM url_crawler , hde WHERE url_crawler.url= hde.URL AND hde.SES_ID=%d AND hde.INDEXED=1; """ %sid
x=[]
m=[]
c=0
cursor.execute(sql)
rows=cursor.fetchall()
print "these URLs are indexed and crawled"
for row in rows:
	print row
	a=row[0]
	b=row[1]
	x.append([a,b])
	c+=1
print "lists of childs in first level and their information (only unindexed ones)"
for l in range(0,c):
	rw="""SELECT id_1 FROM Link WHERE Link.id_2=%d""" % x[l][0]
	cursor.execute(rw)
	childs=cursor.fetchall()
	print "----set-----"
	print childs 
	print "----info-----"
	for c in childs :
		info="""SELECT url, secured, tld, indexed, http_access FROM url_crawler, Link WHERE id_1 = %d AND  url_crawler.id=Link.id_1 AND url_crawler.indexed=0 """ % c[0] 
		cursor.execute(info)
		inform=cursor.fetchall()
		for inn in inform:
			print inn
					
cursor.close()
db.close()




	

