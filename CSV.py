from matplotlib import pyplot as plt
from Tkinter import *
import csv
import numpy as np

def Graph():
	f = open('data.txt', 'w')
	i = 0
	year = e2.get()
	mylist = [10]
	y = [10]
	year = int (year)
	mylist[0] = year
	r = 2014 - year
	for i in range(0,int(r)):
		mylist= int(year + i)
		s = str(mylist)
		f.write(s)
		f.write('\n')
	f.close()

	f1 = open('data1.txt','w')
	while(year <= 2013):
		x=e3.get() + '_cy' + str(year) + '_top.csv'
		f=open(x)
		csv_f=csv.reader(f)
		str1 = e1.get()
		header=next(csv_f)
		for row in csv_f:
			if(row[0] == str1.upper()):
				y= row[1]	
				break
		s = str(y)
		f1.write(s)
		f1.write('\n')	
		year = year +1	
	f1.close()
	data = np.loadtxt("data.txt")
	data1 = np.loadtxt("data1.txt")
	x=np.loadtxt("data.txt",unpack=True)
	y=np.loadtxt("data1.txt",unpack=True)
	plt.plot(x, y, linewidth=2.0)
	plt.title('Popularity of Name')
	plt.ylabel('Name Frequency')
	plt.xlabel('Year')
	plt.show()
def fun_5():
	entr=Tk()
	Label(entr,text='Enter Name').grid(row=0)
	Label(entr,text='Enter Year').grid(row=1)
	Label(entr,text='Male/Female').grid(row=2)
	global e1
	e1=Entry(entr)
	global e2
	e2=Entry(entr)
	global e3
	e3=Entry(entr)
	e1.grid(row=0,column=1)
	e2.grid(row=1,column=1)
	e3.grid(row=2,column=1)
	Button(entr,text='Exit',command=entr.destroy).grid(row=3,column=0,sticky=W,pady=4)
	Button(entr,text='Show',command=Graph).grid(row=3,column=1,sticky=W,pady=4)
	entr.mainloop()
def show():
	x=e1.get()
	y=e2.get()
	print("Top %s\nYear %s"%(x,y))
	fun1()
def show1():
	root = Tk()
	frame= Frame(root,width=240, height=60)
	thelable = Label(root,text = "Under Construction")
	button_1 = Button(root,text="Exit", command=root.destroy)
	thelable.pack()
	button_1.pack()
	root.mainloop()	
def show2():
	root = Tk()
	frame= Frame(root,width=240, height=60)
	thelable = Label(root,text = "Under Construction")
	button_1 = Button(root,text="Exit", command=root.destroy)
	thelable.pack()
	button_1.pack()
	root.mainloop()	
def fun5():
	entr=Tk()
	Label(entr,text='Enter Top').grid(row=0)
	Label(entr,text='Enter Year').grid(row=1)
	Label(entr,text='Male/Female/Both').grid(row=2)
	global e1
	e1=Entry(entr)
	global e2
	e2=Entry(entr)
	global e3
	e3=Entry(entr)
	e1.grid(row=0,column=1)
	e2.grid(row=1,column=1)
	e3.grid(row=2,column=1)
	Button(entr,text='Exit',command=entr.destroy).grid(row=3,column=0,sticky=W,pady=4)
	Button(entr,text='Show',command=fun1).grid(row=3,column=1,sticky=W,pady=4)
	entr.mainloop()
def fun1():
	x=(e3.get()) + '_cy' + (e2.get()) + '_top.csv'
	print x 
	f=open(x)
	csv_f=csv.reader(f)
	root = Tk()
	T = Text(root, width=40, height=60)
	S = Scrollbar(root)
	S.pack(side=RIGHT, fill=Y)
	T.pack(side=LEFT, fill=Y)
	S.config(command=T.yview)
	T.config(yscrollcommand=S.set)
	x=e1.get()
	for row in csv_f:
	 	y=row[2]
	 	y=y.replace("=","")
	 	if(y == "Position"):
	 		print "hello"
		else:
			if(int (y) <= int (x)):	
				T.insert(END,row)
				T.insert(END,'\n')		
	root.mainloop()	
def fun4():
	root = Tk()
	frame= Frame(root,width=240, height=60)
	thelable = Label(root,text = "MiniProject BETA Phase 1")  #creates label window
	button_1 = Button(root,text="Top Names", command=fun5)
	button_2 = Button(root,text="Graph", command=fun_5)
	button_3 = Button(root,text="About", command=show2)
	button_4 = Button(root,text="Exit", command=root.destroy)
	thelable.pack()
	button_1.pack()
	button_2.pack()
	button_3.pack()
	button_4.pack()
	frame.pack()
	root.mainloop()
#fun()	
#fun1()
#fun2()
fun4()
