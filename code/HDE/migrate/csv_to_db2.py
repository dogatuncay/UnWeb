import os
import MySQLdb, csv

db=MySQLdb.connect(host="localhost",user="root", passwd="root",db="unweb_iub")
cursor=db.cursor()
path="/home/doga/Desktop/migrate/"
dirList=os.listdir(path)
count=1
for fname in dirList:
	print fname.split(".")[1]
	if fname.split(".")[1] == "csv":
		data_path="/home/doga/Desktop/migrate/"+fname
		csv_data=csv.reader(file(data_path, 'rb'))
		headerline=csv_data.next()
		for row in csv_data:

			count +=1
			print count
			cursor.execute("INSERT INTO hde (S_ID, URL, Process, Host, IP, Content) VALUES (%s, %s, %s, %s, %s, %s)",row) 	
		db.commit()
cursor.close()
db.close()


