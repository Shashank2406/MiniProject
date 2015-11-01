from Tkinter import *
def fun():
	root = Tk() #Blank window
	thelable = Label(root,text = "MiniProject Aplha 1")  #creates label window
	thelable.pack()
	root.mainloop()
def fun1():
	root = Tk()
	topframe = Frame(root)
	topframe.pack()	
	bottomframe = Frame(root)
	bottomframe.pack(side=BOTTOM)
	b=Button(topframe,text="Search",fg="black")
	b1=Button(topframe,text="Search 1",fg="black")
	b2=Button(topframe,text="Search 2",fg="black")
	b3=Button(bottomframe,text="Search 3",fg="black")
	b.pack(side=LEFT)
	b1.pack(side=LEFT)
	b2.pack(side=LEFT)
	b3.pack(side=BOTTOM)
	root.mainloop()

def fun2():	
	root = Tk() #Blank window
	lable_1 = Label(root,text = "Name")  
	lable_2 = Label(root,text = "MiniProject Aplha 2")
	entry_1= Entry(root)
	entry_2= Entry(root)
	lable_1.grid(row=0,column=0,sticky=E) #default column is zero;
	lable_2.grid(row=1,column=0)
	entry_1.grid(row=0,column=1)
	entry_2.grid(row=1,column=1)
	root.mainloop()

def fun4():
	root = Tk()
	frame= Frame(root,width=100, height=50)
	thelable = Label(root,text = "MiniProject Aplha 1")  #creates label window
	button_1 = Button(root,text="Top Names?", command=fun2)
	button_2 = Button(root,text="Exit", command=root.quit)
	thelable.pack()
	button_1.pack()
	button_2.pack()
	frame.pack()
	root.mainloop()
#fun()	
#fun1()
#fun2()
fun4()
