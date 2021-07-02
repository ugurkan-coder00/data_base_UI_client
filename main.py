from tkinter import *  
import pymongo
import os

class screen:
	def __init__(self,title = "DataBaseClient",geometry = "524x",y=212,color = "black"):
		self.title = title
		self.geometry = geometry
		self.color = color
		self.y = y

	"""def database(self):
		#self.client = pymongo.MongoClient("mongodb://localhost:27017/")
		#self.mydb = self.client["YOUR CLİENT NAME"]
		#self.col = self.mydb["YOUR CLİENT COLLESCİON"]"""

	def mainroot(self):
		self.root = Tk()
		self.root.title(self.title)
		self.root.resizable(0,0)
		self.root.iconphoto(False,PhotoImage(file = "icon.png"))
		self.root.geometry(self.geometry+str(self.y))
		self.root.configure(bg = self.color)

	def servicecommadstart(self):
		if os.name == "nt":
			self.partition_one_button.configure(text = "Windows Bad")
		else:
			os.system("service mongod start")
			self.root.after(200,lambda:self.partition_one_button.configure(text = "Starting!"))
			self.partition_one_button2.configure(text = "Stop Service")
	
	def servicecommandstop(self):
		if os.name == "nt":
			self.partition_one_button2.configure(text = "Windows Bad")
		else:
			os.system("service mongod stop")
			self.root.after(200,lambda:self.partition_one_button2.configure(text = "Stopping!"))
			self.partition_one_button.configure(text = "Start Service")
   
	def getdatacommand(self):
		dosya = open("getdata.txt","wb")
		# Write Data!!
		l = Label(self.root,borderwidth=0,highlightthickness=0,bg = "light blue",fg = "gray15",text = "Data İs Printed!")
		l.pack(side=BOTTOM)
		self.root.after(1000,lambda:l.configure(text = ""))

	def deletedatacommand(self):
		#self.col.drop()
		l = Label(self.root,borderwidth=0,highlightthickness=0,bg = "light blue",fg = "gray15",text = "Data İs Deleted!")
		l.pack(side=BOTTOM)
		self.root.after(1000,lambda:l.configure(text = ""))

	def back(self):
		self.partition_two.configure(text = "Your App's")
		self.partition_two_button.place(x = 212,y = 35,width=100)

		self.clientbutton.place(x = 10000)
		self.clientbutton2.place(x = 10000)
		self.client_Back_button.place(x = 100000)
		

	def clientopencommand(self):
		self.partition_two.configure(text = "Data")
		self.partition_two_button.place(x = 100000)
		
		self.clientbutton = Button(self.root,borderwidth=0,highlightthickness=0,bg = "light blue",fg = "gray15",text = "Get Data",command=self.getdatacommand)
		self.clientbutton.pack()
		self.clientbutton.place(x =212,y = 35,width=100)
		
		self.clientbutton2 = Button(self.root,borderwidth=0,highlightthickness=0,bg = "light blue",fg = "gray15",text = "Delete Data",command=self.deletedatacommand)
		self.clientbutton2.pack()
		self.clientbutton2.place(x =212,y = 75,width=100)

		self.client_Back_button = Button(self.root,borderwidth=0,highlightthickness=0,bg = "gold",fg = "gray15",text = "Back",command=self.back)
		self.client_Back_button.pack()
		self.client_Back_button.place(x = 389,y = 75,width=100)

	def buttons(self):
		#region partition_one
		self.partition_one_button = Button(self.root,borderwidth=0,highlightthickness=0,bg = "gray20",fg = "white",text = "Start Service",command=self.servicecommadstart)
		self.partition_one_button.pack()
		self.partition_one_button.place(x = 38,y = 35,width=100)

		self.partition_one_button2 = Button(self.root,borderwidth=0,highlightthickness=0,bg = "gray20",fg = "white",text = "Stop Service",command=self.servicecommandstop)
		self.partition_one_button2.pack()
		self.partition_one_button2.place(x = 38,y = 80,width=100)
		#endregion
		#region partition_two
		self.partition_two_button = Button(self.root,borderwidth=0,highlightthickness=0,bg = "light blue",fg = "gray15",text = "App",font = ("Arial",9,"italic"),command=self.clientopencommand)
		self.partition_two_button.pack()
		self.partition_two_button.place(x = 212,y = 35,width=100)
		#endregion
		#region partition_three
		self.partition_three_button = Button(self.root,borderwidth=0,highlightthickness=0,bg = "gold",fg = "gray15",text = "Quit",command=self.root.quit)
		self.partition_three_button.pack()
		self.partition_three_button.place(x = 389,y = 35,width=100)
		#endregion
	def labels(self):
		self.partition_one = Label(self.root,bg = "gray20",text = "Service",fg = "white",font = ("Arial",10,"bold"),anchor="n")
		self.partition_one.pack()
		self.partition_one.place(x = 0,y = 0,height=self.y,width=175)

		self.partition_two = Label(self.root,bg = "light blue",text = "Your App's",fg = "gray15",font = ("Arial",10,"bold"),anchor="n")
		self.partition_two.pack()
		self.partition_two.place(x = 175,y = 0,height=self.y,width=175)

		self.partition_three = Label(self.root,bg = "gold",text = "Command",fg = "gray15",font = ("Arial",10,"bold"),anchor="n")
		self.partition_three.pack()
		self.partition_three.place(x = 350,y = 0,height=self.y,width=175)

	def loop(self):
		self.root.mainloop()

scren = screen()
#scren.database()
scren.mainroot()
scren.labels()
scren.buttons()
scren.loop()
