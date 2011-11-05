import csv, os, MySQLdb
db=MySQLdb.connect(host="localhost",user="root", passwd="root",db="unweb_iub")
cu=db.cursor()
path="/home/doga/Desktop/scraper_data"
dirList=os.listdir(path)
cu.execute("SELECT E_ID FROM hde")
row=0
count=0
for fname in dirList:
	if fname.split(".")[1] == "csv":
		data_path="/home/doga/Desktop/scraper_data/"+fname
		csv_data=csv.reader(file(data_path, 'rb'))
		#headerline=csv_data.next()
		#r=len(list(csv_data))-1
		for row in csv_data:
			#cu.execute("UPDATE hde SET INDEXED ='0' WHERE E_ID =%d" %(count))
			count+=1
			#db.commit()
			if row[0].startswith("https"):
				if row[1] == "true":
					cu.execute("UPDATE hde SET INDEXED ='1' WHERE URL =%s", row[0])
					db.commit()
			else:	
				#print 'http://'+row[0]
				r=row[0].replace(row[0],"http://"+row[0])
				if row[1] == "true":
					cu.execute("UPDATE hde SET INDEXED ='1' WHERE URL =%s", r)	
					db.commit()

			#if row[1] == "true":
				#print row[1]
				#cu.execute("UPDATE hde SET INDEXED ='1' WHERE E_ID =%d" %(count))
				#cu.execute("UPDATE hde SET INDEXED ='1' WHERE URL =%s", row[0])
				#cu.execute("INSERT INTO test_index(INDEXED) VALUES('1') WHERE URL='%s'",row[0])
				#cu.execute("UPDATE test_index SET INDEXED ='0'")
				#cu.execute("INSERT INTO test_index(INDEXED) VALUES('1')")	
			#db.commit()
			
cu.close()
db.close()
	
