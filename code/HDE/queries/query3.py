from Tkinter import *
import os, MySQLdb
import tkMessageBox
db=MySQLdb.connect(host="localhost",user="root", passwd="root",db="unweb_iub")
cu=db.cursor()

class Quitter(Frame): # subclass our GUI
	def __init__(self, parent=None): # constructor method
		Frame.__init__(self, parent)
		self.pack()
		widget = Button(self, text='Quit', command=self.quit)
		widget.pack(side=LEFT)
	def quit(self):
		Frame.quit(self)

def fetch():
	print 'Input => "%s"' % ent.get() # get text
	x=int(ent.get())
	cu.execute("SELECT COUNT(INDEXED) FROM hde WHERE INDEXED=1 AND SES_ID=%s",x)
	d=cu.fetchall()
	cu.execute("SELECT COUNT(INDEXED) FROM hde WHERE INDEXED=0 AND SES_ID=%s",x)
	e=cu.fetchall()
	print e
	tkMessageBox.showinfo("# of Indexed" , d)
	tkMessageBox.showinfo("# of Unindexed", e)
	#root=Tk()
	#root.title('# of Indexed & Unindexed')
	#Message(root,e)
	#Message(root,d)
	#root.mainloop()

cu.execute("SELECT COUNT(DISTINCT SES_ID) FROM hde")
d=cu.fetchall()	

root = Tk()
root.option_add("*Dialog.msg.wrapLength", "40i")
ent = Entry(root)
ent.insert(0, 'Select a session id 1-%d' %d[0]) # set text
ent.pack(side=TOP, fill=X) # grow horiz

ent.focus() # save a click
ent.bind('<Return>', (lambda event: fetch())) # on enter key
btn = Button(root, text='Fetch', command=fetch) # and on button
btn.pack(side=LEFT)
Quitter(root).pack(side=RIGHT)
root.mainloop() 
