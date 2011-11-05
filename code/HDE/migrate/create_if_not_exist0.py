
import MySQLdb
db=MySQLdb.connect(host="localhost",user="root", passwd="root",db="unweb_iub")
cursor=db.cursor()

sql="""CREATE TABLE IF NOT EXISTS `hde`(
  `E_ID` int(11) NOT NULL AUTO_INCREMENT, 
  `S_ID` int(11) DEFAULT NULL, 
  `URL` text,
  `Process` varchar(45) DEFAULT NULL,
  `Host` varchar(45) DEFAULT NULL,
  `IP` varchar(45) DEFAULT NULL,
  `Content` varchar(45) DEFAULT NULL,
  `SES_ID` int(11) DEFAULT NULL,
  `INDEXED` varchar(2) DEFAULT '0',
  PRIMARY KEY (`E_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1"""
cursor.execute(sql)
db.commit()

