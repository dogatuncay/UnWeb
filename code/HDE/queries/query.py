
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

sql="""select S_ID FROM url_crawler , hde WHERE url_crawler.url= hde.URL AND hde.SES_ID=%d""" %sid
cursor.execute(sql)
rows=cursor.fetchall()

#we dont need this right now
#sql2="""select id FROM createt, url_crawler WHERE createt.URL= url_crawler.url"""
#cursor.execute(sql2)
#idss=cursor.fetchall()

x=[]
m=[]
c=0
print "-------------------all consecutive pairs-----------------------"
for consecutive in rows:
	a=consecutive[0]
	x.append(a)

for i in range(1,len(x)):
	#print x[i]
	if x[i-1]==x[i]-1:
		a=x[i]
		b=x[i-1]
		print b,a 
		c+=1
		m.append([c,b,a])
#os.system("clear")
print "----------------------------------------------------------------"
print "You will be asked which consecutive you want to analyze. \nYou can only enter one of these consecutive pairs \nPick one number and enter"
for l in range(len(m)):
	print m[l][0]

pid=input("ENTER A PAIR NUMBER: ")
for l in range(len(m)):
	if pid == m[l][0]:
		c1=m[l][1]
		c2=m[l][2]
print "----------------------------------------------------------------"
#print "=======last consecutive pair is====" 
#print b,a

cons_crw="""select DISTINCT id FROM url_crawler , hde WHERE (url_crawler.url= hde.URL AND hde.S_ID=%d) OR (url_crawler.url= hde.URL AND hde.S_ID=%d)""" % (c1,c2)

cursor.execute(cons_crw)
ready_to_link=cursor.fetchall()
arr_count=0
a=[]
b=[]
for r in ready_to_link:
	arr_count+=1
	print "--- 1- found the consecutive in the url crawler table" 
	print r[0]
	print "--- 2- found the first level of childs of the consecutive urls in the link table" 
	rw="""SELECT id_1 FROM Link WHERE Link.id_2=%d""" % r[0]
	cursor.execute(rw)
	lists=cursor.fetchall()
	if arr_count==1:
		for ls in lists:
			a.append(ls[0])
		print a
	elif arr_count==2:
		for ls in lists:
			b.append(ls[0])
		print b
for k in range(len(a)-1):
	for m in range(len(a)-1):
		if a[k]==b[m]:
			print "we have common!"
			print a[k], "=" , b[m]
			l1=a[k]
			print "the info about this url (url, secured, tld, indexed, http_access):" 
			info="""SELECT url, secured, tld, indexed, http_access FROM url_crawler, Link WHERE id_1 = %d AND id_2= %d AND  url_crawler.id=Link.id_1 """ %(l1, r[0]) 
			cursor.execute(info)
			print cursor.fetchall()
		
			
cursor.close()
db.close()




	

